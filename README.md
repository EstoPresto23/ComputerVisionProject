# ComputerVisionProject
ASL teacher

ASL Tutor Draft
Name, Date of Notes

Julian Johnson, 3/12/23
Run program through Jupyter notebook. 
Current issue is potentially outdated mediapipe.python.solutions.holistic FACE_CONNECTIONS attribute being updated to FACEMESH_TESSELATION.
more testing on this to follow. 
Program built up to neural network. 
Is able to use webcam on windows systems and track the landmarks on a human face, pose, left and right hands
Current code set for ASL's "hello," "thanks," and "I love you," visible under Folder setup comment. 
LSTM chosen as model because requires less parameters than other neural networks 

Julian Johnson, 4/8/23
added create_gesture_data.py, cvproject.py (empty for now), datalfair_trainCNN.py, model_for_gesture.py
reference: https://data-flair.training/blogs/sign-language-recognition-python-ml-opencv/

this ref solves a few earlier problems- no dependence on mediapipe, compatible with 3.11, and uses .py instead of jupyter files. 

will be performing most calculations & such on native machine, compatibility seems fine with python 3.11. Updating filepaths and have folders setup to train the CNN model. 

Expected elements of dictionary:
Letters
Following Words:
Me, you, we, and 
