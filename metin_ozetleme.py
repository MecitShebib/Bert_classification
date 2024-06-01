"""
Tkinter kütüphanesiyle arayüz
"""

# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog

# NLP Pkgs
from spacy_summarization import text_summarizer
from gensim.summarization import summarize
from nltk_summarization import nltk_summarizer
from bert_classification import main

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

# Structure and Layout
window = Tk()
window.title("Metin özetleme")
window.geometry("780x600")
window.config(background="black")

style = ttk.Style(window)
style.configure(
    "lefttab.TNotebook",
    tabposition="wn",
)


# TAB LAYOUT
tab_control = ttk.Notebook(window, style="lefttab.TNotebook")

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Ana":^20s}')
tab_control.add(tab2, text=f'{"Dosya":^19s}')
tab_control.add(tab3, text=f'{"URL":^20s}')
tab_control.add(tab4, text=f'{"Karşılaştırıcı":^18s}')
tab_control.add(tab5, text=f'{"Hakkında":^16s}')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 20},

label1 = Label(tab1, text="Özetleyici",font=font, padx=10, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text="Dosya işleme",font=font, padx=10, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text="URL",font=font, padx=10, pady=5)
label3.grid(column=0, row=0)

label3 = Label(tab4, text="Özetleyicileri karşılaştır",font=font, padx=10, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab5, text="Hakkında",font=font, padx=5, pady=5)
label4.grid(column=0, row=0)

tab_control.pack(expand=1, fill="both")

def get_summary():
    raw_text = str(entry.get("1.0", tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = "\nSummary:{}".format(final_text)
    tab1_display.insert(tk.END, result)
    

def classification():
    raw_text = str(entry.get("1.0", tk.END))
    tahmin_sonucu = main(raw_text)
    categories_label.config(text="Kategoriler: " + tahmin_sonucu)

# Clear entry widget
def clear_text():
    entry.delete("1.0", END)


def clear_display_result():
    tab1_display.delete("1.0", END)


# Clear Text  with position 1.0
def clear_text_file():
    displayed_file.delete("1.0", END)
    categories_label.config(text="Kategoriler: ")


# Clear Result of Functions
def clear_text_result():
    tab2_display_text.delete("1.0", END)


# Clear For URL
def clear_url_entry():
    url_entry.delete(0, END)


def clear_url_display():
    tab3_display_text.delete("1.0", END)


# Clear entry widget
def clear_compare_text():
    entry1.delete("1.0", END)


def clear_compare_display_result():
    tab4_display.delete("1.0", END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
    file1 = tkinter.filedialog.askopenfilename(
        filetypes=(("Text Files", ".txt"), ("All files", "*"))
    )
    with open(file1, encoding="utf-8") as file:
        read_text = file.read()
    displayed_file.insert(tk.END, read_text)


def get_file_summary():
    raw_text = displayed_file.get("1.0", tk.END)
    final_text = text_summarizer(raw_text)
    result = "\nSummary:{}".format(final_text)
    tab2_display_text.insert(tk.END, result)


# URL'den Metin Al
def get_text():
    url = str(url_entry.get())
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    fetched_text = " ".join(map(lambda p: p.text, soup.find_all("p")))
    url_display.insert(tk.END, fetched_text)


def get_url_summary():
    raw_text = url_display.get("1.0", tk.END)
    final_text = text_summarizer(raw_text)
    result = "\nÖzetlemek:\n{}".format(final_text)
    tab3_display_text.insert(tk.END, result)


# COMPARER FUNCTIONS


def use_spacy():
    raw_text = str(entry1.get("1.0", tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = "\nSpacy Summary:{}\n".format(final_text)
    tab4_display.insert(tk.END, result)


def use_nltk():
    raw_text = str(entry1.get("1.0", tk.END))
    final_text = nltk_summarizer(raw_text)
    print(final_text)
    result = "\nNLTK Summary:{}\n".format(final_text)
    tab4_display.insert(tk.END, result)


def use_gensim():
    raw_text = str(entry1.get("1.0", tk.END))
    final_text = summarize(raw_text)
    print(final_text)
    result = "\nGensim Summary:{}\n".format(final_text)
    tab4_display.insert(tk.END, result)

# MAIN NLP TAB
l1 = Label(tab1, text="Özetlemek için metni girin")
l1.grid(row=1, column=0)

entry = Text(tab1, height=10)
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# BUTTONS
button1 = Button(
    tab1, text="Sıfırla", command=clear_text, width=12, bg="#03A9F4", fg="#fff"
)
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(
    tab1, text="Özetlemek", command=get_summary, width=12, bg="#03A9F4", fg="#fff"
)
button2.grid(row=4, column=1, padx=10, pady=10)

button2 = Button(
    tab1, text="Sınıflandır", command=classification, width=12, bg="#03A9F4", fg="#fff"
)
button2.grid(row=5, column=1, padx=10, pady=10)

button3 = Button(
    tab1,text="Sonucu temizle",command=clear_display_result,width=12,bg="#03A9F4",fg="#fff",
)
button3.grid(row=5, column=0, padx=10, pady=10)

# Display Screen For Result
tab1_display = Text(tab1, height=10)
tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Text categories
categories_label = Label(tab1, text="Kategoriler:")
categories_label.grid(row=6, column=1, padx=5, pady=5)


# FILE PROCESSING TAB
l1 = Label(tab2, text="özetlemek için dosyayı açın")
l1.grid(row=1, column=1)

displayed_file = ScrolledText(tab2, height=7)  # Initial was Text(tab2)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0 = Button(tab2, text="dosya aç", width=12, command=openfiles, bg="#03A9F4", fg="#fff")
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="sıfırla ", width=12, command=clear_text_file, bg="#03A9F4", fg="#fff")
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(
    tab2, text="özetleme", width=12, command=get_file_summary, bg="#03A9F4", fg="#fff"
)
b2.grid(row=3, column=2, padx=10, pady=10)

b3 = Button(tab2, text="Sonucu temizle", width=12, command=clear_text_result, bg="#03A9F4", fg="#fff")
b3.grid(row=5, column=1, padx=10, pady=10)

b4 = Button(tab2, text="kapat", width=12, command=window.destroy, bg="#03A9F4", fg="#fff")
b4.grid(row=5, column=2, padx=10, pady=10)

# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, height=10)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)


# URL TAB
l1 = Label(tab3, text="Özetlemek için URL girin")
l1.grid(row=1, column=0)

raw_entry = StringVar()
url_entry = Entry(tab3, textvariable=raw_entry, width=50)
url_entry.grid(row=1, column=1)

# BUTTONS
button1 = Button(
    tab3, text="Sıfırla", command=clear_url_entry, width=12, bg="#03A9F4", fg="#fff"
)
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(
    tab3, text="metin almak", command=get_text, width=12, bg="#03A9F4", fg="#fff"
)
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(
    tab3,
    text="Sonucu temizle",
    command=clear_url_display,
    width=12,
    bg="#03A9F4",
    fg="#fff",
)
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(
    tab3, text="Özetleme", command=get_url_summary, width=12, bg="#03A9F4", fg="#fff"
)
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For Result
url_display = ScrolledText(tab3, height=10)
url_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)


tab3_display_text = ScrolledText(tab3, height=10)
tab3_display_text.grid(row=10, column=0, columnspan=3, padx=5, pady=5)


# COMPARER TAB
l1 = Label(tab4, text="Özetlemek için metni girin")
l1.grid(row=1, column=0)

entry1 = ScrolledText(tab4, height=10)
entry1.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

# BUTTONS
button1 = Button(
    tab4, text="Sıfıla", command=clear_compare_text, width=12, bg="#03A9F4", fg="#fff"
)
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab4, text="SpaCy", command=use_spacy, width=12, bg="#03A9F4", fg="#fff")
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(
    tab4,
    text="Sonucu temizle",
    command=clear_compare_display_result,
    width=12,
    bg="#03A9F4",
    fg="#fff",
)
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab4, text="NLTK", command=use_nltk, width=12, bg="#03A9F4", fg="#fff")
button4.grid(row=4, column=2, padx=10, pady=10)

button4 = Button(
    tab4, text="Gensim", command=use_gensim, width=12, bg="#03A9F4", fg="#fff"
)
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For Result
tab4_display = ScrolledText(tab4, height=15)
tab4_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)


# About TAB
about_label = Label(
    tab5,
    text="Otomatik metin özetleme V.0.0.1\nMecit ŞEBİB 170419931\nProje-1\nDr.Öğr.Üyesi Eyüp Emre ÜLKÜ",
    font=font,
    pady=5,
    padx=5,
)
about_label.grid(column=0, row=1)

window.mainloop()
