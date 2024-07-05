from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize SVM classifier
clf = SVC(kernel='linear')

# Number of epochs
num_epochs = 10

# Training loop for each epoch
print(f'Starting training with {num_epochs} epochs.')
for epoch in range(num_epochs):
    # Fit the model for this epoch
    clf.fit(X_train, y_train)

    # Predict on the test data
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Print accuracy for this epoch
    print(f'Epoch {epoch+1}/{num_epochs} - Accuracy on test set: {accuracy:.2f}')

# Final accuracy after training
final_accuracy = accuracy_score(y_test, clf.predict(X_test))
print(f'Final accuracy after training: {final_accuracy:.2f}')
