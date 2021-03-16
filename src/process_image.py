import cv2
import numpy as np

print(cv2.__version__)

class ProcessImage:

    def image_smoothening(self, img):
        ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
        ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        blur = cv2.GaussianBlur(th2, (1, 1), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return th3

    def remove_noise_and_smooth(self, file_name):
        #logging.info('Removing noise and smoothening image')
        img = cv2.imread(file_name)
        cv2.imshow('o', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('++++++++++++ ',file_name)
        print(img)
        aa = np.uint8
        bb = img.astype(aa)
        filtered = cv2.adaptiveThreshold(bb, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        img = self.image_smoothening(img)
        or_image = cv2.bitwise_or(img, closing)
        cv2.imshow('o', or_image) 
        return or_image