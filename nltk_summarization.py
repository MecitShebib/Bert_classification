"""
nltk kütüphanesiyle metin özetleme fonkisyonları
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq


def nltk_summarizer(raw_text):
    # Türkçe stopword (durdurma kelimeleri) listesini yükler
    stopWords = set(stopwords.words("turkish"))

    # Kelime frekanslarını saklamak için bir sözlük oluşturur
    word_frequencies = {}
    
    # Ham metni kelimelere böler ve her kelimenin frekansını hesaplar
    for word in nltk.word_tokenize(raw_text):
        if word not in stopWords:  # Stopword değilse
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1  # Kelime ilk kez görülüyorsa frekansını 1 yapar
            else:
                word_frequencies[word] += 1  # Daha önce görülen kelimenin frekansını artırır

    # Maksimum kelime frekansını bulur
    maximum_frequncy = max(word_frequencies.values())
    
    # Tüm kelimelerin frekanslarını maksimum frekansa bölerek normalleştirir
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequncy

    # Ham metni cümlelere böler
    sentence_list = nltk.sent_tokenize(raw_text)
    
    # Cümlelerin skorlarını saklamak için bir sözlük oluşturur
    sentence_scores = {}
    
    # Her cümledeki kelimeleri dolaşır ve kelime frekanslarına göre cümle skorlarını hesaplar
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(" ")) < 30:  # Cümle 30 kelimeden kısa ise
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]  # İlk kez ekleniyorsa skoru belirler
                    else:
                        sentence_scores[sent] += word_frequencies[word]  # Daha önce eklendiyse skorunu artırır

    # En yüksek skora sahip 7 cümleyi seçer
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    # Seçilen cümleleri birleştirerek özet metni oluşturur
    summary = " ".join(summary_sentences)
    return summary  # Özet metni döner
