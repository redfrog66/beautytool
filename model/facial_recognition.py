import cv2
import matplotlib.pyplot as plt

# read in the image
imagePath = 'testpictures/alltimetester.jpg'

img = cv2.imread(imagePath)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# face detection 
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

face = face_classifier.detectMultiScale(
    gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# face features recognision
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

for (x, y, w, h) in face:
    face_roi = img[y:y+h, x:x+w]
    gray_face_roi = gray_img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(gray_face_roi)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face_roi, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Show the image with detected features
cv2.imshow('Facial Features Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# plt.figure(figsize=(20,10))
# plt.imshow(img_rgb)
# plt.show()
# plt.axis('off')