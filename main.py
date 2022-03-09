# import matplotlib
# matplotlib.use('TkAgg')
# import tkinter
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# image = mpimg.imread('group.jpeg')
# plt.imshow(image)
# plt.show()



import cv2
import dlib

img=cv2.imread('group.jpeg')

cv2.imshow('Image',img)
key=cv2.waitKey(1000)

hog_detector=dlib.get_frontal_face_detector()
faces_hog=hog_detector(img,1)
f1=[]

print('Location of faces:',faces_hog)

for face in faces_hog:
    x = face.left()
    y = face.top()
    w = face.right() - x
    h = face.bottom() - y
    f1.append(img[y:y+h,x:x+w,:])
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

for face in faces_hog:
    x = face.left()
    y = face.top()
    w = face.right() - x
    h = face.bottom() - y
    f1.append(img[y:y+h,x:x+w,:])
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow('Image',img)
key=cv2.waitKey(1000)


cv2.destroyAllWindows()