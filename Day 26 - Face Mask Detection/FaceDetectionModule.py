import time
import cv2 as cv
import mediapipe as mp
import time



class FaceDetector:
    def __init__(self, minDetectionConfidence=0.5):
        self.minDetectionConfidence = minDetectionConfidence
        self.mpFaceDetection = mp.solutions.face_detection
        self.face = self.mpFaceDetection.FaceDetection(0.75)  # Min detection confidence
        self.mpDraw = mp.solutions.drawing_utils

    def findFaces(self,img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.face.process(imgRGB)
        bboxs=[]
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                confidence_score = detection.score
                h, w, c = img.shape
                bbxoc = detection.location_data.relative_bounding_box
                bbox = int(bbxoc.xmin*w), int(bbxoc.ymin*h), \
                    int(bbxoc.width*w), int(bbxoc.height*h)
                bboxs.append([id, bbox, confidence_score])

                if draw:
                    img = self.fancyDraw(img, bbox)
                    # cv.rectangle(img, bbox, (255,0,255), 2)
                cv.putText(img, f'{int(confidence_score[0]*100)}%', (bbox[0], bbox[1]-10), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,255), 2)
        return img, bboxs

    def fancyDraw(self, img, bbox, l=30, t=5):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        cv.rectangle(img, bbox, (255,0,255), 1)
        #Top Left Corner
        cv.line(img, (x,y), (x+l,y), (255,0,255), t)
        cv.line(img, (x,y), (x,y+l), (255,0,255), t)

        #Top Right Corner
        cv.line(img, (x1-l,y), (x1,y), (255,0,255), t)
        cv.line(img, (x1,y), (x1,y+l), (255,0,255), t)

        #Bottom Left Corner
        cv.line(img, (x,y1), (x+l,y1), (255,0,255), t)
        cv.line(img, (x,y1), (x,y1-l), (255,0,255), t)

        #Bottom Right Corner
        cv.line(img, (x1,y1), (x1-l,y1), (255,0,255), t)
        cv.line(img, (x1,y1), (x1,y1-l), (255,0,255), t)
        
        return img
    

def main():
    capture = cv.VideoCapture(1)
    ptime=0
    detector=FaceDetector()
    while True:
        isTrue, frame = capture.read()
        frame, bboxs =  detector.findFaces(frame)
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv.putText(frame, f'FPS: {str(int(fps))}', (10,70), cv.FONT_HERSHEY_PLAIN, 2, (255,255,0), 2)
        cv.imshow('Video', frame)   

        if cv.waitKey(20) & 0xFF==ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()


if __name__=='__main__':
    main()