import cv2
import os
import numpy

# CLASSIFIERS
eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50)
fisherface = cv2.face.FisherFaceRecognizer_create()

print('STARTING TRAINING!')

def getImageId():
    paths = [os.path.join('images\\samples', i) for i in os.listdir('images\\samples')]
    faces = []
    ids = []

    for pathImage in paths:
        imageFace = cv2.imread(pathImage)
        imageConverted = cv2.cvtColor(imageFace, cv2.COLOR_BGR2GRAY)
        ids.append(int(os.path.split(pathImage)[-1].split('.')[1]))
        faces.append(imageConverted)
    return numpy.array(ids), faces

ids, faces = getImageId()

eigenface.train(faces, ids)
eigenface.write('classifiers\\classifierEigenface.yml')

fisherface.train(faces, ids)
fisherface.write('classifiers\\classifierFisherface.yml')

print('SUCCESSFUL TRAINING!')