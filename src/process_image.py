import cv2
import numpy as np
import os
#from deskew import determine_skew

class ProcessImage:

    # Criar imagem
    def create_image(self, image, directory):
        dir_ = os.path.dirname(directory)
        if not os.path.exists(dir_):
            os.makedirs(dir_, exist_ok=True)
        cv2.imwrite(directory, image)
        print(directory)

    def process(self, path_image):
        path_image = str(path_image)
        
        img = cv2.imread(path_image)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 3)
        img = cv2.fastNlMeansDenoising(img, None, 3, 7, 11)
        th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        #th1 = self.__rotate(th1)

        return th1.astype(np.uint8)

    def __rotate(self, img):
        angle = determine_skew(img)
        print(angle)

        img_inv = cv2.bitwise_not(img)
        coords = np.column_stack(np.where(img_inv > 0))
        angle = -(cv2.minAreaRect(coords)[-1])
        print(angle)
        if angle < -50:
            angle = angle + 90
        print(angle)

        
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    