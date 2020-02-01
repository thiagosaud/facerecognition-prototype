"""
THIS FILE WAS CREATED ESPECIALLY FOR DETECTION IN STATIC IMAGES.
AUTHOR: CODE DEVELOPED BY THIAGO DE BONIS CARVALHO SAAD SAUD
LINKEDIN: https://www.linkedin.com/in/thiagodebonisoficial/
IMPORTANT: READ README.MD FOR MORE CODE INFORMATION
"""
import cv2

# RETURN A PATH OF IMAGES
def getStaticImage():
    arrStaticImages = ['images\\static\\cats_and_dogs.jpg',
                       'images\\static\\crowd.jpg',
                       'images\\static\\group_of_peoples(1).jpg',
                       'images\\static\\group_of_peoples(2).jpg',
                       'images\\static\\group_of_peoples(3).jpg'
                       ]
    return arrStaticImages


# CV2 SETUP TO CLASSIFIER INITIALIZATION
classifier = cv2.CascadeClassifier('classifiers\\haar\\haarcascade_frontalface_default.xml')

# CV2 SETUP TO IMAGE INITIALIZATION
imageOriginal = cv2.imread(filename=getStaticImage()[1])
imageConverted = cv2.cvtColor(src=imageOriginal, code=cv2.COLOR_BGR2GRAY)

# CV2 SETUP TO CLASSIFIER DETECT
faceDetected = classifier.detectMultiScale(image=imageConverted, scaleFactor=1.1, minNeighbors=1, minSize=(30, 30))
facesMatrix = faceDetected
facesAmount = len(faceDetected)

# LOOP THROUGH FACES MATRIX
# A FACE MATRIX CAN CONTAINER 0..N FACE VECTORS
# EACH VECTOR WITHIN THE MATRIX IS REFERENCED TO A FACE
for (x, y, l, a) in facesMatrix:
    pointXY = (x, y)
    pointDrawing = (x + l, y + a)
    cv2.rectangle(img=imageOriginal, pt1=pointXY, pt2=pointDrawing, color=(0, 0, 255), thickness=2)
    cv2.putText(
        img=imageOriginal,
        text=f'X: {x}',
        org=(x, y + a + 20),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=1,
        color=(0, 0, 255)
    )
    cv2.putText(
        img=imageOriginal,
        text=f'Y: {y}',
        org=(x + 2, y + a + 40),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=1,
        color=(0, 0, 255)
    )

# CV2 SETUP TO IMAGE SHOW AND CLOSED (WAITKEY)
cv2.imshow("FACES FOUND", imageOriginal)
cv2.waitKey()
