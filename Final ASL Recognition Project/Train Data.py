import pickle
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

# Load data dictionary from data.pickle file
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Convert data and labels into numpy arrays
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split data into training and testing sets
x_train, x_test, y_learn, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Train a Support Vector Machines model
model = SVC()
model.fit(x_train, y_learn)

# Predict on the testing set
y_predict = model.predict(x_test)

# Compute the accuracy and confusion matrix of the model
score = accuracy_score(y_predict, y_test)
cm = confusion_matrix(y_test, y_predict)
print("Confusion matrix:")
print(cm)

# Print the accuracy
print('{}% of samples were classified'.format(score * 100))


# Save the trained model as a pickle file
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
