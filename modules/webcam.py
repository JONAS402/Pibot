import cv2
import sys


def webcam_detect():
    #cascPath = sys.argv[1]
    cascPath = 'modules/src/cascade_frontalface_webcam.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)
    print('Starting Facial Recognition...')
    video_capture = cv2.VideoCapture(-1)
    print('press q to close')
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=0
            # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('Exiting...')
            # video_capture.release()
            break

    # When everything is done, release the capture
    cv2.destroyAllWindows()
    video_capture.release()



# webcam_detect()