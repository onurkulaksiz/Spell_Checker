# Spell_Checker
This repository, spell checks using multiple libraries.
In this way, it is ensured that the wrong words written are corrected.
It provides users with the most convenient option by using multiple libraries.

# Libraries
- spaCy
- textblob
- pyspellchecker
# spaCy
## Install
```python
pip install contextualSpellCheck
```
## Usage
```python
import spacy
import contextualSpellCheck
nlp = spacy.load('en_core_web_sm')
contextualSpellCheck.add_to_pipe(nlp)

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
```
