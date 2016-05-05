import psutil
import os
import platform

# print(os.name)

# psutil.test()


class MemoryInfo:
    def __init__(self):
        self._fields = None

    def bytes2human(n):
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.1f%s' % (value, s)
        return "%sB" % n


    def print_tuple(nt):
        for name in nt._fields:
            value = getattr(nt, name)
            if name != 'percent':
                value = MemoryInfo.bytes2human(value)
            print('%-10s : %7s' % (name.capitalize(), value))


    @staticmethod
    def main():
        print('MEMORY\n------')
        MemoryInfo.print_tuple(psutil.virtual_memory())
        print('\nSWAP\n----')
        MemoryInfo.print_tuple(psutil.swap_memory())


class NetStat:

    import socket
    from socket import AF_INET
    from socket import SOCK_STREAM
    from socket import SOCK_DGRAM
    AD = "-"
    AF_INET6 = getattr(socket, 'AF_INET6', object())
    proto_map = {
        (AF_INET, SOCK_STREAM): 'tcp',
        (AF_INET6, SOCK_STREAM): 'tcp6',
        (AF_INET, SOCK_DGRAM): 'udp',
        (AF_INET6, SOCK_DGRAM): 'udp6',
}


    @staticmethod
    def main():
        import psutil
        templ = "%-5s %-30s %-30s %-13s %-6s %s"
        print(templ % (
            "Proto", "Local address", "Remote address", "Status", "PID",
            "Program name"))
        proc_names = {}
        for p in psutil.process_iter():
            try:
                proc_names[p.pid] = p.name()
            except psutil.Error:
                pass
        for c in psutil.net_connections(kind='inet'):
            laddr = "%s:%s" % c.laddr
            raddr = ""
            if c.raddr:
                raddr = "%s:%s" % c.raddr
            print(templ % (
                NetStat.proto_map[(c.family, c.type)],
                laddr,
                raddr or NetStat.AD,
                c.status,
                c.pid or NetStat.AD,
                proc_names.get(c.pid, '?')[:15],))


class IfConfig:
    import socket
    af_map = {
        socket.AF_INET: 'IPv4',
        socket.AF_INET6: 'IPv6',
        psutil.AF_LINK: 'MAC',
}

    duplex_map = {
        psutil.NIC_DUPLEX_FULL: "full",
        psutil.NIC_DUPLEX_HALF: "half",
        psutil.NIC_DUPLEX_UNKNOWN: "?",
}


    @staticmethod
    def main():
        stats = psutil.net_if_stats()
        for nic, addrs in psutil.net_if_addrs().items():
            if nic in stats:
                print("%s (speed=%sMB, duplex=%s, mtu=%s, up=%s):" % (
                    nic, stats[nic].speed, IfConfig.duplex_map[stats[nic].duplex],
                    stats[nic].mtu, "yes" if stats[nic].isup else "no"))
            else:
                print("%s:" % nic)
            for addr in addrs:
                print("    %-8s" % IfConfig.af_map.get(addr.family, addr.family), end="")
                print(" address   : %s" % addr.address)
                if addr.broadcast:
                    print("             broadcast : %s" % addr.broadcast)
                if addr.netmask:
                    print("             netmask   : %s" % addr.netmask)
                if addr.ptp:
                    print("             p2p       : %s" % addr.ptp)
            print("")


# noinspection PyMethodMayBeStatic
class DiskUsage:
    def bytes2human(n):
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.1f%s' % (value, s)
        return "%sB" % n


    @staticmethod
    def main():
        templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
        print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type", "Mount"))
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    # skip cd-rom drives with no disk in it; they may raise
                    # ENOENT, pop-up a Windows GUI error for a non-ready
                    # partition or just hang.
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            print(templ % (
                part.device,
                DiskUsage.bytes2human(usage.total),
                DiskUsage.bytes2human(usage.used),
                DiskUsage.bytes2human(usage.free),
                int(usage.percent),
                part.fstype, part.mountpoint))


def run_diagnostics():
    print()
    print('Operating System: ', platform.system())
    print('Kernel Release: ', platform.release())
    print()
    print('Disk Usage:')
    disk = DiskUsage
    disk.main()
    print()
    print('netstat')
    stats = NetStat
    stats.main()
    print()
    print('ifconfig')
    config = IfConfig
    config.main()
    info = MemoryInfo
    info.main()

run_diagnostics()