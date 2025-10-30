import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

def train_model():
    """Trains a Naive Bayes classifier on the training data."""
    df = pd.read_csv('threat_analyzer/data/training_data.csv')
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['threat_type'], test_size=0.2, random_state=42)

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    joblib.dump(model, 'threat_analyzer/threat_classifier.pkl')
    print("Model trained and saved to threat_classifier.pkl")

def classify_text(text):
    """Classifies the given text using the trained model."""
    model = joblib.load('threat_analyzer/threat_classifier.pkl')
    return model.predict([text])[0]

if __name__ == '__main__':
    train_model()
