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
## Usage
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
```python
from spellchecker import SpellChecker
spell = SpellChecker()
x = input()
misspelled = spell.unknown([x])

```
