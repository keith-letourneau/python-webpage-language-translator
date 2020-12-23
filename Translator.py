#!/usr/bin/env python
# coding: utf-8

# # <center> English to Russian Translator </center>
# 
# This script will translate English text to Russian text and save output to .txt file.

#create russian translator function
from google_trans_new import google_translator  
 
def russian_trans(str):
 translator = google_translator() 
 translated = translator.translate(str, lang_src='en', lang_tgt='ru')
 return str + ' // ' + translated

russian_trans("Let's drink some wine!")


#create a list of translations
ru_text = []

ru_text.append(russian_trans('Tonight we drink bourbon!'))
ru_text.append(russian_trans('I passed all my classes and exams.'))
ru_text.append(russian_trans('My water heater is broken.'))
ru_text.append(russian_trans('Where is the bathroom?'))

for trans in ru_text:
    print(trans)


#save translations to .txt file
with open(r'C:\Users\keith\OneDrive\Desktop\Python Scripts\Russian Translations.txt', 'w', 
          encoding="utf-8") as my_file:
    my_file.write('Common Phrases in Russian!' + '\n' + '\n')
    for trans in ru_text:
        my_file.write(trans + '\n')


#lets also get pronounciations
def russian_pronounce(str):
    pronounce = translator.translate(str, lang_src='en', lang_tgt='ru', pronounce=True)
    return pronounce[2] + ' // ' + str

russian_pronounce('It is snowing outside.')

ru_pronounce = []

ru_pronounce.append(russian_pronounce('Lets go snowboarding.'))
ru_pronounce.append(russian_pronounce('Jazz is my favorite music.'))
ru_pronounce.append(russian_pronounce('I can play guitar'))
ru_pronounce.append(russian_pronounce('My brother is very strong.'))

for trans in ru_pronounce:
    print(trans)


# # <center>Translate French News Website to English</center>
# 
# This script with translate h1,h2,h3 tags to English, place into list and save as .txt file.


#translate French news website headlines to English
import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from pandas import DataFrame

url = 'https://www.monde-diplomatique.fr/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

news = []

for heading in soup.find_all(["h1", "h2", "h3"]):
    news.append(heading.text.strip())

translator = google_translator()

df = DataFrame(news,columns=['French'])
df['English'] = df['French'].apply(translator.translate, lang_src='fr', 
                                                         lang_tgt='en')
df.head(5)


#turn translations into a list and save to .txt file
fr_headlines = df['English'].values.tolist()

for headline in range(5):
    print(fr_headlines[headline])
    
with open(r'C:\Users\keith\OneDrive\Desktop\Python Scripts\French Headlines.txt', 'w', 
          encoding="utf-8") as my_file:
    my_file.write('French Headlines from Today' + '\n' + '\n')
    for headline in fr_headlines:
        my_file.write(headline + '\n')

