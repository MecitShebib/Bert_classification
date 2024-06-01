"""
spacy kütüphanesiyle metin özetleme fonkisyonları
"""

# NLP paketleri ve spacy kütüphanesi yüklenir
import spacy
from spacy.lang.tr import Turkish

# Türkçe dil modeli oluşturulur
nlp = Turkish()
nlp.add_pipe("sentencizer")  # Cümle ayırıcı eklenir

from spacy.lang.tr.stop_words import STOP_WORDS  # Türkçe stopword'ler yüklenir
from string import punctuation  # Noktalama işaretleri yüklenir
from heapq import nlargest  # En büyük n elemanı bulmak için heapq modülü yüklenir

# Metin özetleyici fonksiyonu tanımlanır
def text_summarizer(raw_docx):
    raw_text = raw_docx
    docx = nlp(raw_text)  # Metin işlenir
    stopwords = list(STOP_WORDS)  # Stopword'ler listeye dönüştürülür
    
    # Kelime frekansları oluşturulur
    word_frequencies = {}
    for word in docx:
        if word.text not in stopwords:  # Kelime stopword değilse
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1  # Kelime ilk kez görülüyorsa frekansını 1 yapar
            else:
                word_frequencies[word.text] += 1  # Daha önce görülen kelimenin frekansını artırır

    # Maksimum kelime frekansını bulur
    maximum_frequncy = max(word_frequencies.values())
    
    # Tüm kelimelerin frekanslarını maksimum frekansa bölerek normalleştirir
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequncy
    
    # Cümleleri token'lara böler
    sentence_list = [sentence for sentence in docx.sents]

    # Cümlelerin skorlarını saklamak için bir sözlük oluşturur
    sentence_scores = {}
    for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(" ")) < 30:  # Cümle 30 kelimeden kısa ise
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]  # İlk kez ekleniyorsa skoru belirler
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]  # Daha önce eklendiyse skorunu artırır

    # En yüksek skora sahip 7 cümleyi seçer
    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    
    # Seçilen cümleleri birleştirerek özet metni oluşturur
    final_sentences = [w.text for w in summarized_sentences]
    summary = " ".join(final_sentences)
    
    return summary  # Özet metni döner

