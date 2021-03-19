import cv2
import numpy as np
import os
from datetime import datetime

class ProcessImage:

    def process(self, path_image):
        path_image = str(path_image)
        base_path = os.path.dirname(path_image)
        img = cv2.imread(path_image)
        print(path_image)

        img = cv2.medianBlur(img, 3)
        _, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        root, _ = os.path.splitext(os.path.basename(path_image))

        paths = os.path.normpath(root)
        paths_dirs = paths.split(os.sep)
        print('ppppppppppp',paths_dirs[-1])
        direc = '{}/../{1} (processadas)'.format(base_path, paths_dirs[-1])
        if not os.path.exists(direc):
            os.mkdir(direc)
        now = datetime.timestamp(datetime.now())
        cv2.imwrite('{0}/../{1} (processadas)/{2} ({3}).jpg'.format(base_path, paths_dirs[-1], root, now), th1)
        
        return th1

    def image_smoothening(self, img):
        ret1, th1 = cv2.threshold(img, cv2.THRESH_BINARY, 255, cv2.THRESH_BINARY)
        ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        blur = cv2.GaussianBlur(th2, (1, 1), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return th3

    def remove_noise_and_smooth(self, file_name):
        img = cv2.imread(file_name, 0)
        filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        img = self.image_smoothening(img)
        or_image = cv2.bitwise_or(img, closing)
        cv2.imwrite('C:\\Users\\savio\Desktop\\folhas confusas - Copia\\2020.11.18 0003.2020\\b.jpg', or_image)
        return or_image