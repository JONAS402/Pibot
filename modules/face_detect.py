import cv2

# Get user supplied values
# import sys
# imagePath = sys.argv[1]
# cascPath = sys.argv[2]


def face_detect(imagePath):
    cascPath = 'modules/src/cascade_frontalface_default.xml'


    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        # flags = cv2.cv.HAAR_SCALE_IMAGE
        flags=0
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Faces found", image)
    print('q to close')
    if cv2.waitKey(0) & 0xFF == ord('q'):
        print('closing file...')
        cv2.destroyAllWindows()


# USAGE #currently only works from src folder move in file to src before face_detect
# imagePath = input('enter a file to face detect: ')
# imagePath = 'src/abba.png'
# face_detect(imagePath)
