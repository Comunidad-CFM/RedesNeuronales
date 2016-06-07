import cv2
from Crop import Crop

class Crops():
    def __init__(self, imagen):
        self.im = cv2.imread(imagen)
        self.gray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        self.blur = cv2.GaussianBlur(self.gray, (5, 5), 0)

        self.thresh = cv2.adaptiveThreshold(self.gray, 255, 1, 1, 11, 2)
        self.image, self.contours, self.hierarchy = cv2.findContours(self.thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        self.crops = []
        self.images = []


    def sortCrops(self):
        length = len(self.crops)
        temp = 0

        for i in range(0, length):
            for j in range(0, length - 1):
                if (self.crops[j].id > self.crops[j + 1].id):
                    temp = self.crops[j]
                    self.crops[j] = self.crops[j + 1]
                    self.crops[j + 1] = temp

            length -= 1

    def cutImage(self):
        for cnt in self.contours:
            if cv2.contourArea(cnt) > 50:
                [x, y, w, h] = cv2.boundingRect(cnt)

                if h > 28:
                    cv2.rectangle(self.im, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    roi = self.thresh[y:y + h, x:x + w]
                    self.crops.append(Crop(roi, cnt[0][0][0]))

    def getAverage(self):
        x = 0
        y = 0

        for i in self.crops:
            x += len(i.img[0])
            y += len(i.img)

        x = x / len(self.crops)
        y = y / len(self.crops)

        return x, y

    def canInsert(self, img):
        for crop in self.crops:
            if (img.id > crop.id - 10) and (img.id < crop.id + 10):
                return False

        self.crops.append(img)
        return True

    def binarization(self):
        for crop in self.crops:
            print 'ID:',crop.id
            print 'Len:',len(crop.img)
            print '1:', crop.img[0]


    def filterCrops(self):
        self.cutImage()
        self.sortCrops()
        j = 0
        x, y = self.getAverage()

        for i in self.crops:
            if (len(i.img[0]) >= x and len(i.img[0]) <= x + (x * 0.25)) or (len(i.img) >= y and len(i.img) <= y + (y * 0.25)):
                self.images.append(i)

        self.crops = []

        for i in self.images:
            if self.canInsert(i):
                i = cv2.resize(i.img, (50, 100))
                cv2.imwrite('./crops/' + str(j) + '.png', i)
                j += 1

        self.binarization()

        print "-----------------------"
        print x, y
        #cv2.waitKey(0);
