import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from snowballstemmer import TurkishStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

# Verisetini oku
df = pd.read_excel('/Users/MK/Desktop/test_verisi.xlsx')
# Metni temizleme fonksiyonu
def metni_temizle(metin):
    # Tüm harfleri küçük harfe çevir
    metin = metin.lower()
    # Noktalama işaretlerini kaldır
    metin = re.sub(r'[^\w\s]', '', metin)
    # Rakamları kaldırma
    metin = re.sub(r'\d+', '', metin)
    # Birden fazla boşlukları tek boşlukla değiştir
    metin = re.sub(r'\s+', ' ', metin)
    # Metinden başlangıçtaki ve sondaki boşlukları kaldır
    metin = metin.strip()
    return metin
# Metni temizle
df['metin'] = df['metin'].apply(metni_temizle)
# Temizlenmiş metni Excel dosyasına yaz
df.to_excel("/Users/MK/Desktop/temizlenmis_test_verisi.xlsx", index=False)

