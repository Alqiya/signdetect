""" import cv2 as cv # type: ignore
import os
import time
import uuid

IMAGES_PATH= "Tensorflow/workspace/images/collectedimages"
labels= ['help','ok','you','mine','say','equal']
number_imgs= 10

for label in labels:
    os.makedirs (f'Tensorflow/workspace/images/collectedimages//'+label)
    cap = cv.VideoCapture(0)
    print("collecting images for {}".format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret , frame = cap.read()# type: ignore
        imgnum= os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv.imwrite(imgnum, frame)
        cv.imshow('frame',frame)
        time.sleep(2)

        if cv.waitkey(1) & 0xFF==ord('q'):
            break
    cap.release() """


import cv2 as cv
import os
import time
import uuid

# Define the path to save images
IMAGES_PATH = "Tensorflow/workspace/images/collectedimages"
labels = ['help', 'ok', 'you', 'mine', 'say', 'equal']
number_imgs = 10

for label in labels:
    # Create a directory for each label if it doesn't already exist
    label_path = os.path.join(IMAGES_PATH, label)
    os.makedirs(label_path, exist_ok=True)

    cap = cv.VideoCapture(0)  # Open the webcam
    print("Collecting images for {}".format(label))
    time.sleep(5)  # Give the user time to prepare

    for imgnum in range(number_imgs):
        ret, frame = cap.read()  # Capture a frame
        if not ret:
            print("Failed to capture image. Exiting...")
            break

        img_name = os.path.join(label_path, '{}.jpg'.format(str(uuid.uuid1())))
        cv.imwrite(img_name, frame)  # Save the captured frame as an image
        cv.imshow('frame', frame)  # Display the captured frame

        time.sleep(2)  # Pause for 2 seconds between captures

        if cv.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break

    cap.release()  # Release the webcam

cv.destroyAllWindows()  # Close all OpenCV windows