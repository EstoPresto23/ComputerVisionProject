import os
import pickle
import mediapipe as mp
import cv2

# initialize MediaPipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# define data directory path
DATA_DIR = './data'

data = [] # to store the landmarks data for each image
labels = [] # to store the corresponding label for each image
for dir_ in os.listdir(DATA_DIR): # loop over each directory in data directory
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)): # loop over each image in the directory
        data_aux = [] # to store the landmarks data for current image

        x_ = [] # to store the x coordinates of all landmarks in current image
        y_ = [] # to store the y coordinates of all landmarks in current image

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path)) # read the image
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # detect hands landmarks in the image
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                # calculate relative coordinates of all landmarks in the image
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            # store the landmarks data and label for current image
            data.append(data_aux)
            labels.append(dir_)

# save the data and labels as pickle file
f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
