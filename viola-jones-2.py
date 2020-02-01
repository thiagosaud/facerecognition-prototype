"""
THIS FILE WAS CREATED ESPECIALLY FOR DETECTION IN REAL TIME.
AUTHOR: CODE DEVELOPED BY THIAGO DE BONIS CARVALHO SAAD SAUD
LINKEDIN: https://www.linkedin.com/in/thiagodebonisoficial/
IMPORTANT: READ README.MD FOR MORE CODE INFORMATION
"""
import cv2

# CV2 SETUP TO READ AN IMAGE OF A BUFFER IN MEMORY THROUGH THE SELECTED WEBCAM
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# CV2 SETUP TO CLASSIFIER INITIALIZATION
classifier = cv2.CascadeClassifier('classifiers\\haar\\haarcascade_frontalface_default.xml')

# INFINITE LOOP FOR WEBCAM
while True:
    # WEBCAM BUFFER RESTRUCTURING
    isConnected, videoFrameMatrix = webcam.read()
    if isConnected:
        # CLOSE WINDOW WHEN 'Q' KEY IS PRICED
        if cv2.waitKey(delay=1) == ord('q'):
            break

        # CV2 SETUP TO IMAGE INITIALIZATION
        videoFrameConverted = cv2.cvtColor(src=videoFrameMatrix, code=cv2.COLOR_BGR2GRAY)

        # CV2 SETUP TO CLASSIFIER DETECT
        faceDetected = classifier.detectMultiScale(videoFrameConverted, scaleFactor=2.3, minNeighbors=1, minSize=(30, 30))
        facesMatrix = faceDetected
        facesAmount = len(faceDetected)

        # LOOP THROUGH FACES MATRIX
        # A FACE MATRIX CAN CONTAINER 0..N FACE VECTORS
        # EACH VECTOR WITHIN THE MATRIX IS REFERENCED TO A FACE
        for (x, y, l, a) in facesMatrix:
            cv2.rectangle(img=videoFrameMatrix, pt1=(x, y), pt2=(x + l, y + a), color=(0, 0, 255), thickness=2)

        # CV2 SETUP TO IMAGE INITIALIZATION
        cv2.imshow(winname='OPEN WEBCAM', mat=videoFrameMatrix)
    else:
        print('WEBCAM IS NOT CONNECTED, TRYING TO CONNECT...')

# CV2 SETUP TO RELEASE VIDEO CAPTURE AND MEMORY
webcam.release()
cv2.destroyAllWindows()