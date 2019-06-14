#coding: utf-8
import cv2

cascade_file = "../../../Anaconda3/Library/etc/haarcascades/haarcascade_frontalface_alt.xml"
image_file = '../new/before.jpg'
print(image_file)

img =  cv2.imread(image_file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.png", gray)

cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(gray, minSize=(150, 150))

if len(face_list) == 0:
  print("Fail recognise")
  quit()

for (x, y, w, h) in face_list:
  print('facepoint=', x, y, w, h)
  color = (0, 0, 225)
  pen_w = 8
  cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w)

cv2.imwrite("after.jpg", img)