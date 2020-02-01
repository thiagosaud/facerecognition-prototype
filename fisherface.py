import cv2
import os

classifierFace = cv2.CascadeClassifier("classifiers\\haar\\haarcascade_frontalface_default.xml")
fisherface = cv2.face.FisherFaceRecognizer_create(num_components=50, threshold=1)
fisherface.read("classifiers\\classifierFisherface.yml")

height, width = 220, 220
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    isConnected, image = webcam.read()

    if isConnected:
        imageConverted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faceDetected = classifierFace.detectMultiScale(imageConverted, scaleFactor=1.5, minSize=(30, 30))

        for (x, y, w, h) in faceDetected:
            faceImage = cv2.resize(imageConverted[y:y + h, x:x + w], (width, height))
            faceId, accuracy = fisherface.predict(faceImage)
            faceName = ''

            if faceId == 1:
                color = (0, 255, 51)
                faceName = 'THIAGO DE BONIS'
            elif faceId == 2:
                color = (0, 0, 255)
                faceName = 'JANE RICHA'
            else:
                color = (0, 0, 255)
                faceName = 'UNKNOWN'

            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, f'ID: {faceId}', (x, y + (h + 30)), cv2.FONT_HERSHEY_PLAIN, 1, color)
            cv2.putText(image, f'NAME: {faceName}', (x, y + (h + 50)), cv2.FONT_HERSHEY_PLAIN, 1, color)
            cv2.putText(image, f'ACCURACY: {accuracy}', (x, y + (h + 70)), cv2.FONT_HERSHEY_PLAIN, 1, color)

        cv2.imshow("FACE", image)
        if cv2.waitKey(1) == ord('q'):
            break
