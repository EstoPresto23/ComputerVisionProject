import random
import cv2
import hand_detection_lib as handlib
import os

detector = handlib.handDetector()
cam = cv2.VideoCapture(0)

def draw_results(frame, user_draw):
    # Random cases from the Computer
    com_draw = random.randint(0,2)

    # Draw, input texts for user_draw
    frame = cv2.putText(frame, 'You', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2, cv2.LINE_AA)

    s_img = cv2.imread(os.path.join("pics", str(user_draw) + ".png"))
    x_offset = 50
    y_offset = 100
    frame[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img

    # Draw, input texts for com_draw (Computer)
    frame = cv2.putText(frame, 'Computer', (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    s_img = cv2.imread(os.path.join("pics",str(com_draw) + ".png"))
    x_offset = 300
    y_offset = 100
    frame[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img

    # Check and output the results, need to be fixed for different resolution
    if user_draw == com_draw:
        result="DRAW!"
    elif (user_draw==0) and (com_draw==1):
        result="YOU WIN!"
    elif (user_draw==1) and (com_draw==2):
        result="YOU WIN!"
    elif (user_draw==2) and (com_draw==0):
        result="YOU WIN!"
    else:
        result="YOU LOSE!"

    frame = cv2.putText(frame, result, (10, 550), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 255), 2, cv2.LINE_AA)


while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)

    # Import pics into detector
    frame, hand_lms = detector.findHands(frame)
    n_fingers = detector.count_finger(hand_lms)

    user_draw = -1 # 0: Paper, 1: Rock, 2: Scissors
    if n_fingers==0:
        user_draw = 1
    elif n_fingers==2:
        user_draw = 2
    elif n_fingers ==5:
        user_draw = 0
    elif n_fingers!=-1:
        print(" Only accept Rock - Paper - Scissors")
    else:
        print("No hand is detected")

    key = cv2.waitKey(1)

    cv2.imshow("Rock-Paper-Scissors", frame)
    if key==ord("q"): #press q to quit
        break
    elif key == ord(" "): #play by using spacebar
        draw_results(frame, user_draw)
        cv2.imshow("Rock-Paper-Scissors", frame)
        cv2.waitKey()


cam.release()
cv2.destroyAllWindows()