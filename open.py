import cv2
import numpy as np
from PIL import Image
from keras import models
import tensorflow as tf

model = tf.keras.models.load_model("CNN.model")
video = cv2.VideoCapture(0)

while True:
        _, frame = video.read()

        im = Image.fromarray(frame, 'RGB')

        im = im.resize((170,170))
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)

        prediction = int(model.predict(img_array)[0][0])
        print(prediction)

        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()
