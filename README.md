# Spell_Checker
This repository, spell checks using multiple libraries.
In this way, it is ensured that the wrong words written are corrected.
It provides users with the most convenient option by using multiple libraries.
It achieves the correct result by taking input from the user or uploading a file.

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
Checking of spelling is a basic requirement in any text processing or analysis. The python package pyspellchecker provides us this feature to find the words that may have been mis-spelled and also suggest the possible corrections.
## Install
First, we need to install the required package using the following command in our python environment.
```python
pip install pyspellchecker
```
## Usage
Now we see below how the package is used to point out the wrongly spelled words as well as make some suggestions about possible correct words.
Finds words that may be misspelled. Displays the correct result and closest values. 
Used for words. It is not used for a sentence.
```python
from spellchecker import SpellChecker
spell = SpellChecker()
x = input()
misspelled = spell.unknown([x])

```
