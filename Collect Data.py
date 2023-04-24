import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

number_of_letters = 8
dataset_size = 100

cap = cv2.VideoCapture(0)
for i in range(number_of_letters):
    if not os.path.exists(os.path.join(DATA_DIR, str(i))):
            os.makedirs(os.path.join(DATA_DIR, str(i)))

    print(' Collecting data for class {}' .format(i))

    done= False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Press Q to start', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow ('Collect Data', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('Collect Data', frame)
        cv2.waitKey(1)
        cv2.imwrite(os.path.join(DATA_DIR, str(i), '{}.jpg'.format(counter)), frame)
        counter +=1


cap.release()
cv2.destroyAllWindows()

