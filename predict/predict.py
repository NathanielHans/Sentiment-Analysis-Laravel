from flask import Flask, request, jsonify
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Pastikan Anda telah mengunduh resource NLTK yang dibutuhkan
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

word_replacements = {
    ' sih ': ' ',
    ' sm ': ' sama ',
    ' mba ': ' mbak ',
    ' aja ': ' saja ',
    ' aj ': ' saja ',
    ' tau ': ' tahu ',
    ' tp ': ' tapi ',
    ' gini ': ' begini ',
    ' org ': ' orang ',
    ' yg ': ' yang ',
    ' ya ': ' ',
    ' gak ': ' tidak ',
    ' ga ': ' tidak ',
    ' lu ': ' kamu ',
    ' bgt ': ' banget ',
    ' skr ': ' sekarang ',
    ' lg ': ' lagi ',
    ' knp ': ' kenapa ',
    ' jd ': ' jadi ',
    ' si ': ' ',
    ' udh ': ' sudah ',
    ' udah ': ' sudah ',
    ' klo ': ' kalau ',
    ' kalo ': ' kalau ',
    ' ama ': ' sama ',
    ' pake ': ' pakai ',
    ' nya ': ' ',
    ' ny ': ' ',
    ' lo ': ' kamu '
}

# Precompile regex for word replacements
replacements = re.compile('|'.join(r'\b%s\b' % re.escape(word) for word in word_replacements.keys()))

# Get Indonesian stopwords once
stop_words = set(stopwords.words('indonesian'))

# Create Sastrawi stemmer once
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def preprocessing(teks):
    # Membuat semua kata huruf kecil
    teks = teks.lower()
    teks = re.sub(r'\d+', '', teks)
    # Apply word replacements using regex
    teks = replacements.sub(lambda match: word_replacements[match.group(0)], teks)
    # Tokenisasi kata-kata
    kata_kunci = word_tokenize(teks)
    # Menghapus tanda baca dan stopwords
    kata_kunci = [kata for kata in kata_kunci if kata not in string.punctuation and kata not in stop_words]
    # Lematisasi kata-kata dengan Sastrawi
    kata_kunci = [stemmer.stem(kata) for kata in kata_kunci]
    return ' '.join(kata_kunci)

# Muat model dari file .sav
model = joblib.load('modelfix.joblib')
vectorizer = joblib.load('vectorizerfix.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.json['text']
        
        # Preprocessing teks
        preprocessed_text = preprocessing(text)
        preprocessed_text_vectorized = vectorizer.transform([preprocessed_text]).toarray()

        # Lakukan prediksi
        prediction = model.predict(preprocessed_text_vectorized)

        # Output hasil prediksi
        predict = prediction[0]

        return jsonify({'predict': predict})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
