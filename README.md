# Spell_Checker
This repository, spell checks using multiple libraries.
In this way, it is ensured that the wrong words written are corrected.
It provides users with the most convenient option by using multiple libraries.

# Libraries
- spaCy
- textblob
- pyspellchecker
# spaCy
spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython.
This package currently focuses on Out of Vocabulary (OOV) word or non-word error (NWE) correction using BERT model. The idea of using BERT was to use the context when correcting NWE.
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

```
# textblob
TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
## Usage
With the help of TextBlob.correct() method, we can get the corrected words if any sentence have spelling mistakes by using TextBlob.correct() method.
```python
from textblob import TextBlob
doc = TextBlob(text)
spell_check = doc.correct()

```
# pyspellchecker
## Install
```python
pip install pyspellchecker
```
## Usage
Finds words that may be misspelled. Displays the correct result and closest values. 
Used for words. It is not used for a sentence.
```python
from spellchecker import SpellChecker
spell = SpellChecker()
x = input()
misspelled = spell.unknown([x])

```
