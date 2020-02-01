"""
THIS FILE WAS CREATED ESPECIALLY FOR DETECTION IN STATIC IMAGES.
AUTHOR: CODE DEVELOPED BY THIAGO DE BONIS CARVALHO SAAD SAUD
LINKEDIN: https://www.linkedin.com/in/thiagodebonisoficial/
IMPORTANT: READ README.MD FOR MORE CODE INFORMATION
"""
import cv2
import numpy

sample, sampleNumber = 1, 25
width, height = 220, 220

classifierFace = cv2.CascadeClassifier('classifiers\\haar\\haarcascade_frontalface_default.xml')
classifierEye = cv2.CascadeClassifier('classifiers\\haar\\haarcascade_eye.xml')
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceName = input('ENTER THE NAME OF THE FACE OWNER: ')
faceId = input('ENTER THE UNIQUE ID FOR THIS FACE: ')

print("AFTER FACE DETECTION, CLICK 'Q' KEY TO SAVE IMAGE.")

while True:
    isConnected, image = webcam.read()
    imageConverted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facesDetected = classifierFace.detectMultiScale(imageConverted, scaleFactor=1.5, minSize=(150, 150))
    print(numpy.average(imageConverted))
    if isConnected:
        for (x, y, l, a) in facesDetected:
            cv2.rectangle(image, (x, y), (x + l, y + a), (0, 0, 255), 2)
            eyeFaceRegion = image[y:y + a, x:x +l]
            regionConverted = cv2.cvtColor(eyeFaceRegion, cv2.COLOR_BGR2GRAY)
            eyeDetected = classifierEye.detectMultiScale(regionConverted)

            for (eyeX, eyeY, eyeW, eyeH) in eyeDetected:
                cv2.rectangle(eyeFaceRegion, (eyeX, eyeY), (eyeX + eyeW, eyeY + eyeH), (0, 255, 0), 2)

                if cv2.waitKey(1) & 0XFF == ord('q'):
                    # average: 0 - 255
                    if numpy.average(imageConverted) > 85:
                        faceImage = cv2.resize(imageConverted[y:y + a, x:x + l], (height, width))
                        cv2.imwrite("images\\samples\\" + str(faceName) + "." + str(faceId) + "." + str(sample) + ".jpg", faceImage)
                        sample += 1
                        print("PHOTO " + str(sample) + " SUCCESSFULLY CAPTURED")

        cv2.imshow('FACE', image)
        cv2.waitKey(1)
        if (sample >= sampleNumber):
            break

print("SUCCESSFUL CAPTURED POSITIONS!")
webcam.release()
cv2.destroyAllWindows()
