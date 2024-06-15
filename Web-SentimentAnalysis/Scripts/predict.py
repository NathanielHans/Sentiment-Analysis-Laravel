import sys
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Pastikan Anda telah mengunduh resource NLTK yang dibutuhkan
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    
    # Tokenisasi
    word_tokens = word_tokenize(text)
    
    # Penghapusan stop words
    stop_words = set(stopwords.words('english'))
    filtered_text = [w for w in word_tokens if not w in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_text = [lemmatizer.lemmatize(word) for word in filtered_text]
    
    return ' '.join(lemmatized_text)

# Muat model dari file .sav
model = joblib.load('gnbModel.sav')
vectorizer = joblib.load('vectorizer.pkl')

# Ambil teks dari argument command line
text = sys.argv[1]

# Preprocessing teks
preprocessed_text = preprocess_text(text)
preprocessed_text_vectorized = vectorizer.transform([preprocessed_text]).toarray()

# Lakukan prediksi
prediction = model.predict(preprocessed_text_vectorized)

# Output hasil prediksi
print(prediction[0])
