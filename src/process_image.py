import cv2
import numpy as np
import os
from skimage.transform import rotate
from deskew import determine_skew

class ProcessImage:

    def process(self, path_image):
        path_image = str(path_image)
        base_path = os.path.dirname(path_image)
        img = cv2.imread(path_image)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 3)
        img = cv2.fastNlMeansDenoising(img, None, 3, 7, 11)
        th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
        
        #th1 = rotate(th1, angle, resize=False) * 255
        th1 = self.__rotate(th1)

        root, _ = os.path.splitext(os.path.basename(path_image))

        paths = os.path.normpath(path_image)
        paths_dirs = paths.split(os.sep)
        direc = '{0}/../{1} (processadas)'.format(base_path, paths_dirs[-2])
        if not os.path.exists(direc):
            os.mkdir(direc)

        cv2.imwrite('{0}/{1}.jpg'.format(direc, root), th1.astype(np.uint8))
        
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

    def __rotate0(self, img):
        img_inv = cv2.bitwise_not(img)
        coords = np.column_stack(np.where(img_inv > 0))
        angle = -(cv2.minAreaRect(coords)[-1])
        print(angle)
        angle = determine_skew(img)
        print(angle)
        
        if (angle > -2):
            (h, w) = img.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        else:
            rotated = img

        return rotated
    