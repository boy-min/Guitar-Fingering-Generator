import cv2
import mediapipe as mp
import time
import numpy as np
from generator.hand import hand_detector as hd

class Hand :
    def __init__(self, size = 0, length = 0) :
        self.detector = hd.handDetector()
        self.__size = size
        self.__length = length

    def set(self) :

        pTime = 0
        cTime = 0
        cap = cv2.VideoCapture(0)
        get_hand = False
        length_queue = [ i for i in range(120)]
        hand_queue = [ [0, 0, 0, 0, 0, 0, 0, 0] for i in range(120)]
        list_of_features = [(4, 20),(2,4),(5,8),(9,12),(13,16),(17,20),(5,17), (0, 9)]
        
        self.__length = [22, 0, 0, 0, 0, 0, 0, 0]
        stand = 0
        text = "wait"
        
        while not get_hand:
            success, img = cap.read()
            img = self.detector.findHands(img)
            lmList = self.detector.findPosition(img)
     
            cTime = time.time()
            
            pTime = cTime
            try:
                idx = 1
                stand = hd.find_len(lmList[4], lmList[20])
                length_arr = [22, 0, 0, 0, 0, 0, 0, 0]
                for i, j in list_of_features[1:]:
                    length = hd.find_len(lmList[i], lmList[j])
                    length_arr[idx] = (length/stand) * self.__length[0]
                    idx += 1
                length_queue.append(stand/1000)
                length_queue.pop(0)

                hand_queue.append(length_arr)
                hand_queue.pop(0)
                if np.var(length_queue) < 50:
                    get_hand = True
                    text = "Done"
                elif np.var(length_queue) < 200:
                    text = "Ok"
                else:
                    text = "wait"
            except:
                pass

            cv2.putText(img, str(text), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 255), 3)
     
            cv2.imshow("Image", img)
            cv2.waitKey(1)
        self.__length[0] = 0
        for hand in hand_queue:
            for i, length in enumerate(hand):
                self.__length[i]+=length
        
        for i in range(len(self.__length)):
            self.__length[i]/=120
        print('ending detector')
        print(self.__length)
        cv2.destroyAllWindows()
        
    def get(self, key = None) :
        if key == None :
            return {'size' : self.__size, 'length' : self.__length}
        
        return {'size' : self.__size, 'length' : self.__length}.get(key)
