import sys

import numpy as np
import cv2

im = cv2.imread('../Imagenes/descarga.png')
# im = cv2.imread('./Imagenes/imagen.png')
im3 = im.copy()

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

#################      Now finding Contours         ###################
image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

samples = np.empty((0, 100))
crops = []
j = 0
for cnt in contours:
    if cv2.contourArea(cnt) > 50:
        [x, y, w, h] = cv2.boundingRect(cnt)

        if h > 28:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi = thresh[y:y + h, x:x + w]
            roismall = cv2.resize(roi, (10, 10))
            cv2.imshow('norm', roi)
            crops.append(roi)
            key = cv2.waitKey(0);
            #
            # if key == 27:  # (escape to quit)
            #     sys.exit()
            # elif key in keys:
            #     responses.append(int(chr(key)))
            # sample = roismall.reshape((1, 100))
            # samples = np.append(samples, sample, 0)

x = 0  # largo
y = 0  # alto

for i in crops:
    x += len(i[0])
    y += len(i)

j = 0
x = x / len(crops)
y = y / len(crops)
for i in crops:
    print  len(i[0]), len(i)
    if ((len(i[0]) >= x and len(i[0]) <= x + (x * 0.25)) or (len(i) >= y and len(i) <= y + (y * 0.25))):
        cv2.imwrite('./crops/' + str(j) + '.png', i)
        j += 1
print "-----------------------"
print x, y
# print y, y+(y*0.5)

cv2.waitKey(0);
# responses = np.array(responses, np.float32)
# responses = responses.reshape((responses.size, 1))
# print "training complete"
#
# np.savetxt('generalsamples.data', samples)
# np.savetxt('generalresponses.data', responses)
