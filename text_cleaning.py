"""
This module provides text cleaning functions such as punctuation removal,
whitespace normalization, stopword removal, and Unicode normalization.
"""

import re
import string
import unicodedata

# from typing import List

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure necessary resources are downloaded
nltk.download("punkt")
nltk.download("stopwords")


def remove_punctuation(text: str) -> str:
    """Remove punctuation from the text."""
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_extra_whitespace(text: str) -> str:
    """Remove extra whitespaces from the text."""
    return re.sub(r"\s+", " ", text).strip()


def remove_stopwords(text: str, language: str = "english") -> str:
    """Remove stopwords from the text."""
    stop_words = set(stopwords.words(language))
    words = word_tokenize(text)
    return " ".join([word for word in words if word.lower() not in stop_words])


def normalize_unicode(text: str) -> str:
    """Normalize unicode characters to their closest ASCII representation."""
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")


def clean_text(
    text: str,
    remove_punct: bool = True,
    remove_ws: bool = True,
    remove_stops: bool = False,
    normalize: bool = False,
) -> str:
    """Apply multiple text cleaning functions based on given parameters."""
    if remove_punct:
        text = remove_punctuation(text)
    if remove_ws:
        text = remove_extra_whitespace(text)
    if remove_stops:
        text = remove_stopwords(text)
    if normalize:
        text = normalize_unicode(text)
    return text


if __name__ == "__main__":
    SAMPLE_TEXT = (
        "  Héllo! This is an example text, with punctuations and extra    spaces.  "
    )
    print(
        clean_text(
            SAMPLE_TEXT,
            remove_punct=True,
            remove_ws=True,
            remove_stops=True,
            normalize=True,
        )
    )
