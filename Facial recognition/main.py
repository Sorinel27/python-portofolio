import numpy as np
import cv2, random, pickle, dlib
import face_train

print("Loading successful!")
choice = input("Hello!\nWelcome to the facial recognition system :-).\nPlease specify your input (image or webcam): ")
if choice == 'webcam':
    video_capture = cv2.VideoCapture(0)
    video_is_on = True
    face_cascade = cv2.CascadeClassifier(
        'C:/Users/Sorin/PycharmProjects/freeCodeCamp/test program/data/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")
    landmark_detector = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    with open("labels.pickle", 'rb') as file:
        original = pickle.load(file)
        labels = {value: key for key, value in original.items()}
        file.close()

    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    while video_is_on:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + h, y + w), random_color, 2)
            gray_roi = gray[y:y + h, x:x + w]
            color_roi = frame[y:y + h, x:x + w]
            id, conf = recognizer.predict(gray_roi)
            if conf >= 45 or conf <= 95:
                cv2.putText(frame, f'{labels[id]}', (x + h, y + w), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                            cv2.LINE_AA)
            landmarks = landmark_detector(color_roi, dlib.rectangle(0, 0, w, h))
            for landmark in landmarks.parts():
                cv2.circle(frame, (x + landmark.x, y + landmark.y), 2, (0, 255, 0), -1)
        cv2.imshow('Face', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    video_capture.release()
    # Destroy all windows
    cv2.destroyAllWindows()
elif choice == "image":
    k = input("Type the absolute path below(ex: C:/Users/Sorin/PycharmProjects/face_detect/image.jpg):\n")
    try:
        #C:/Users/Sorin/PycharmProjects/face_recon/full.jpg
        img = cv2.imread(f'{k}')
        face_cascade = cv2.CascadeClassifier(
            'C:/Users/Sorin/PycharmProjects/freeCodeCamp/test program/data/haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainer.yml")
        landmark_detector = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

        with open("labels.txt", 'rb') as f:
            original = pickle.load(f)
            labels = {value: key for key, value in original.items()}
            f.close()

        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + h, y + w), random_color, 2)
            gray_roi = gray[y:y + h, x:x + w]
            color_roi = img[y:y + h, x:x + w]
            id, conf = recognizer.predict(gray_roi)
            print(f'{id} : {conf}')
            if conf >= 45 or conf <= 95:
                cv2.putText(img, f'{labels[id]}', (x, y + w), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            landmarks = landmark_detector(color_roi, dlib.rectangle(0, 0, w, h))
            for landmark in landmarks.parts():
                cv2.circle(img, (x + landmark.x, y + landmark.y), 2, (0, 255, 0), -1)
        cv2.imshow('Face', img)
        cv2.waitKey(0)
        # Destroy all windows
        cv2.destroyAllWindows()
    except:
        print("Path error!")