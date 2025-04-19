from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
import os

def train_model(X_train, y_train, save_dir='model'):
    # Create model directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Create and train the pipeline
    vectorizer = TfidfVectorizer()
    classifier = RandomForestClassifier()
    
    # Fit vectorizer and transform training data
    X_train_vectorized = vectorizer.fit_transform(X_train)
    
    # Train classifier
    classifier.fit(X_train_vectorized, y_train)
    
    # Save both vectorizer and classifier
    joblib.dump(vectorizer, os.path.join(save_dir, 'vectorizer.pkl'))
    joblib.dump(classifier, os.path.join(save_dir, 'classifier.pkl'))
    
    return vectorizer, classifier

def load_models(model_dir='model'):
    vectorizer = joblib.load(os.path.join(model_dir, 'vectorizer.pkl'))
    classifier = joblib.load(os.path.join(model_dir, 'classifier.pkl'))
    return vectorizer, classifier

def train_from_csv(csv_path, test_size=0.2, random_state=44):
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Split into features (X) and labels (y)
    X = df['email'].values
    y = df['type'].values
    
    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Train and save the models
    vectorizer, classifier = train_model(X_train, y_train)
    
    # Evaluate the model
    X_test_vectorized = vectorizer.transform(X_test)
    accuracy = classifier.score(X_test_vectorized, y_test)
    print(f"Model accuracy : {accuracy:.2f}")
    
    return vectorizer, classifier, (X_test, y_test)

