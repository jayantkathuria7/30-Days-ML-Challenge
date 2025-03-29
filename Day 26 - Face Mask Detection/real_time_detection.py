import FaceDetectionModule as fdm
from tensorflow.keras.models import load_model
import numpy as np
import mediapipe as mp
import cv2 as cv

model = load_model('cnn_model.keras')

labels_dict={0:'Mask', 1:'No Mask'}
color_dict={0:(0,255,0), 1:(255,0,0)}
capture = cv.VideoCapture(1)

detector = fdm.FaceDetector()

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame, bboxs =  detector.findFaces(frame)
    print("bboxs:", bboxs)
    print("Type of bboxs[0][1]:", type(bboxs[0][1]))
    print("bboxs[0][1]:", bboxs[0][1])

    x, y, h, w = bboxs[0][1]
    face_img = gray[y:y+w,x:x+w]
    resized = cv.resize(face_img, (100,100))/255
    reshaped = np.reshape(resized, (1,100,100,1))
    result = model.predict(reshaped)

    label = np.argmax(result)

    cv.putText(frame, labels_dict[label], (x+w-50, y+h+10), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,255,255))

    cv.imshow('Video', frame)   

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()
