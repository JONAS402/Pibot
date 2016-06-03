<!DOCTYPE html>
<html>
<body>

<?php
echo "<h2> Pibot audio fingerprinting database.</h2>";
echo "enter password: ";

$servername = "localhost";
$username = "username";
$password = "password";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
?>

</body>
