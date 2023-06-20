from cv2 import imread, cvtColor, COLOR_BGR2RGB
import face_recognition

def processImg(imgPath1, imgPath2):
    img1 = imread(imgPath1)
    img2 = imread(imgPath2)

    img1rgb = cvtColor(img1, COLOR_BGR2RGB)
    img2rgb = cvtColor(img2, COLOR_BGR2RGB)

    img1encoded = face_recognition.face_encodings(img1rgb)[0]
    img2encoded = face_recognition.face_encodings(img2rgb)[0]

    return face_recognition.compare_faces([img1encoded], img2encoded)