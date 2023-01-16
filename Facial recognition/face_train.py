import os, cv2
import numpy as np
from PIL import Image
import pickle

print("Loading image dataset...")
base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "images")
face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt2.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()

curr_id = 0
label_id = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_path):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            print(label_id)
            if label in label_id:
                pass
            else:
                label_id[label] = curr_id
                curr_id += 1
            id = label_id[label]
            pil_image = Image.open(path).convert("L")
            size_image = (550, 500)
            final_image = pil_image.resize(size_image, Image.LANCZOS)
            image_array = np.array(final_image, "uint8")
            # print(image_array)
            faces = face_cascade.detectMultiScale(image_array, 1.1, 4)
            for (x, y, w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id)

with open("labels.txt", 'wb') as f:
    pickle.dump(label_id, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")
