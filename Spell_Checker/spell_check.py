# -*- coding: utf-8 -*-
"""
# Spacy
"""

!pip install contextualSpellCheck
import spacy
import contextualSpellCheck
import pandas as pd
nlp = spacy.load('en_core_web_sm')
contextualSpellCheck.add_to_pipe(nlp)

df = pd.read_csv('/content/document.txt',sep='\t')
df

def correction (text):
  doc = nlp(text)
  if doc._.performed_spellCheck==True:
    doc = nlp(text)
    print(f"Original: {doc}")
    print(f"True:{doc._.outcome_spellCheck}")
  else:
   print(f"True: {text}")

print("Write something.")
x = input()
correction(x)

df['sentence'].apply(lambda x: correction(''.join(x)))





"""# TexBlob"""

from textblob import TextBlob

def word (text):
  doc = TextBlob(text)
  spell_check = doc.correct()
  print(spell_check)

print("Write something.")
x = input()
word(x)

df['sentence'].apply(lambda x: word(''.join(x)))






"""#pyspellchecker"""

!pip install pyspellchecker
from spellchecker import SpellChecker

spell = SpellChecker()
print("write a word.")
x = input()
misspelled = spell.unknown([x])
 
for word in misspelled:
    print(spell.correction(word))
    print(spell.candidates(word))