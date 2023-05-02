import os
import cv2

# Define data directory, number of hand gestures, and dataset size
DATA_DIR = './data'
NUM_HAND_GESTURES = 11
DATASET_SIZE = 100

# Create data directory if it does not exist
os.makedirs(DATA_DIR, exist_ok=True)

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Loop through each hand gesture
for i in range(NUM_HAND_GESTURES):
    # Create directory for the current hand gesture if it does not exist
    os.makedirs(os.path.join(DATA_DIR, str(i)), exist_ok=True)
    print(f"Collecting data for class {i}")

    # Wait for user to press 'q' to start collecting images
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Press Q to start', (100,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Collect Data', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    # Collect dataset_size images for the current hand gesture
    for j in range(DATASET_SIZE):
        ret, frame = cap.read()
        cv2.imshow('Collect Data', frame)
        cv2.waitKey(1)
        cv2.imwrite(os.path.join(DATA_DIR, str(i), f"{j}.jpg"), frame)

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
