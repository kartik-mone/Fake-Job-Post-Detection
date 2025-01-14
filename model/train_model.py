import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle
import os

# Load dataset
data_path = r'C:\Users\Karti\Documents\Projects\Fake Job Recuirment Prediction\fake_job_postings.csv'
data = pd.read_csv(data_path)

# Preprocessing (Handling missing values)
data.fillna('', inplace=True)

# Using relevant columns for text features (description, requirements, and benefits)
X = data['description'] + ' ' + data['requirements'] + ' ' + data['benefits']
y = data['fraudulent']

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X_transformed = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# Train model (SVM classifier)
model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# Save the model and vectorizer
model_path = r'C:\Users\Karti\Documents\Projects\Fake Job Recuirment Prediction\model\job_post_detector.pkl'
vectorizer_path = r'C:\Users\Karti\Documents\Projects\Fake Job Recuirment Prediction\model\vectorizer.pkl'

with open(model_path, 'wb') as f:
    pickle.dump(model, f)

with open(vectorizer_path, 'wb') as f:
    pickle.dump(vectorizer, f)
