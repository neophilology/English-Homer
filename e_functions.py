import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import regex as re
import nltk

# nltk.download('stopwords')


def e_tokenize(text):
    """
    Given a string,
    returns a list of string tokens.
    """
    return re.findall(r"[\w-]*\p{L}[\w-]*", text)


def e_clean(text):
    """
    Given a text, cleans.
    """
    # turn to lower case
    text = text.lower()
    # tags like <tab>
    text = re.sub(r"<[^<>]*>", " ", text)
    # markdown URLs like [Some text](https://....)
    text = re.sub(r"\[([^\[\]]*)\]\([^\(\)]*\)", r"\1", text)
    # text or code in brackets like [0]
    text = re.sub(r"\[[^\[\]]*\]", " ", text)
    # standalone sequences of specials, matches &# but not #cool
    text = re.sub(r"(?:^|\s)[&#<>{}\[\]+|\\:-]{1,}(?:\s|$)", " ", text)
    # standalone sequences of hyphens like --- or ==
    text = re.sub(r"(?:^|\s)[\-=\+]{2,}(?:\s|$)", " ", text)
    # new line
    text = re.sub(r"\n", " ", text)
    # underscores
    text = re.sub(r"_", " ", text)
    # genitive: backslash and apostrophe
    text = re.sub(r"\'", " ", text)
    # text = re.sub(r'([.\(\)\!\?\-\\\/\,])', r' \1 ', text)
    # sequences of white spaces
    text = re.sub(r"\s+", " ", text)
    # Replace ips
    text = re.sub(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", " _ip_ ", text)
    # Isolate punctuation
    text = re.sub(r"([.\(\)\!\?\-\\\/\,])", r" \1 ", text)
    # Remove some special characters
    text = re.sub(r"([\;\:\|•«®\n])", " ", text)
    # Replace numberals and symbols with spell out words
    text = text.replace("&", " and ")
    text = text.replace("@", " at ")
    text = text.replace("0", " zero ")
    text = text.replace("1", " one ")
    text = text.replace("2", " two ")
    text = text.replace("3", " three ")
    text = text.replace("4", " four ")
    text = text.replace("5", " five ")
    text = text.replace("6", " six ")
    text = text.replace("7", " seven ")
    text = text.replace("8", " eight ")
    text = text.replace("9", " nine ")
    text = text.replace("10", " ten ")
    return text.strip()


def e_remove_stop(tokens):
    """
    Removes stopwordsin set nltk.corpus.stopwords.words('english').
    """
    stopwords = set(nltk.corpus.stopwords.words("english"))
    include_stopwords = {"would"}  # add as needed
    exclude_stopwords = {"against"}  # add as needed

    stopwords |= include_stopwords  # set: union
    stopwords -= exclude_stopwords  # set: difference

    return [t for t in tokens if t.lower() not in stopwords]


# PIPELINE
pipeline = [e_clean, e_tokenize, e_remove_stop]


def e_process_tokens(text, pipeline):
    """
    Given a list of functions processes a text sequentially.
    """
    tokens = text
    for process in pipeline:
        tokens = process(tokens)
    return tokens
