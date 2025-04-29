from flask import Flask, render_template, request, jsonify
import re
import string
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('/Users/md.jubayerhossain/Documents/salauddion/emotion_classifier_model.pkl')
vectorizer = joblib.load('/Users/md.jubayerhossain/Documents/salauddion/tfidf_vectorizer.pkl')

# Emotion Mapping
emotion_mapping = {0: 'anger', 1: 'fear', 2: 'joy', 3: 'love', 4: 'sad', 5: 'suprise'}

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r'\d+', '', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words)

# Home page (optional)
@app.route('/')
def home():
    return "🎉 Emotion detection API is running!"

# 🔍 POST API: Predict Emotion
@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    user_input = data.get('text_input', '')
    
    clean_input = preprocess_text(user_input)
    input_vec = vectorizer.transform([clean_input])
    predicted_label = model.predict(input_vec)[0]
    predicted_emotion = emotion_mapping[predicted_label]
    
    feedback = {
        'anger': "😡 Oh, you sound angry. Take a deep breath. I'm here for you!",
        'fear': "😨 It seems you're scared. Everything will be okay, stay strong!",
        'joy': "😊 You seem happy! That's wonderful! Keep smiling!",
        'love': "💖 Awww, you are feeling love! Spread the positivity!",
        'sad': "😢 I'm sorry you're feeling sad. Remember, tough times don't last.",
        'suprise': "😲 You sound surprised! Hope it’s a good surprise!"
    }

    return {
        'emotion': predicted_emotion,
        'feedback': feedback[predicted_emotion]
    }

# 🧪 Simple GET Test
@app.route('/api/test', methods=['GET'])
def api_test():
    return jsonify({'status': 'API is working!'})

# Run server
if __name__ == '__main__':
    app.run(debug=True)