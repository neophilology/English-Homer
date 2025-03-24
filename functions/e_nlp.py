"""_summary_

Returns:
    _type_: _description_
"""

####################################################################################################
# Import Libraries
####################################################################################################

import re
import string
from typing import List, Callable, Union, Set, Optional

# import numpy as np
import pandas as pd

from tqdm.notebook import tqdm

tqdm.pandas()

import nltk


####################################################################################################
# Import Libraries
####################################################################################################

print("Functions for NLP are live! use e.<function> to call them.")


####################################################################################################
# # Split the text into books
####################################################################################################
def string_into_books(text, book_breaker):
    """
    Split a string into books/sections based on a pattern.

    Args:
        text (str): Text to process
        book_breaker (str): Pattern that indicates the start of a new book/section

    Returns:
        list: List of strings, where each string contains the content for one book/section
    """
    books = re.split(rf"{book_breaker}\s", text)
    # Remove the first element (it's empty or contains text before the first "Book")
    if books[0].strip() == "":
        books = books[1:]  #
        print(len(books))
    else:
        print("Warning: There was text before the first 'Book'")
    return books


def list_into_books(lines_list, book_breaker):
    """
    Split a list of strings into books/sections based on a pattern,
    excluding the lines that contain the book_breaker pattern.

    Args:
        lines_list (list): List of strings to process
        book_breaker (str): Pattern that indicates the start of a new book/section

    Returns:
        list: List of lists, where each inner list contains lines for one book/section
    """
    books = []
    current_book = []

    for line in lines_list:
        if line.strip().startswith(book_breaker):
            # If we already have content in current_book, save it and start a new one
            if current_book:
                books.append(current_book)
                current_book = []

        else:
            # Add the line to the current book
            current_book.append(line)

    # if there's content, add the last book
    if current_book:
        books.append(current_book)

    return books


####################################################################################################
# Populate Odyssey DF
####################################################################################################


def book_into_df(author, year, title, list_books):
    """
    Splits a list_books into rows and creates a DataFrame.
    Args:
    list_books (list): The full text of the Odyssey
    author (str): Author name
    year (str): Publication year
    title (str): Book title
    Returns:
    pd.DataFrame: DataFrame with columns for author, year, title, book_num, and text
    """
    data = []

    for i, book_text in enumerate(list_books, 1):  # Start counting from 1
        data.append(
            {
                "author": author,
                "year": year,
                "title": title,
                "book_num": i,
                "text": book_text,
            }
        )

    # Create the DataFrame from the data
    df = pd.DataFrame(data)

    return df


####################################################################################################
# Count Lines
####################################################################################################
def count_lines(text):
    """Function to count lines in a text by the number of newline characters.

    Args:
        text (list or str): The text as a list of lines or a string.

    Returns:
        int: The number of lines in the text.
    """
    if isinstance(text, list):  # Check if it's a list of lines
        return len(text)  # Return the number of lines

    if isinstance(text, float) and pd.isna(text):  # Check for NaN values
        return 0  # Return 0 for NaN values

    if not isinstance(text, str):  # Check for unexpected data types
        return 0  # Return 0 for unexpected data types

    return text.count("\n") + 1  # Count the number of newline characters


####################################################################################################
#  Count sentences
####################################################################################################


def count_sentences(text):
    """Function to count sentences in a text.

    Args:
        text (list or str): The text as a list of lines or a string.

    Returns:
        int: The number of sentences in the text.
    """
    if isinstance(text, list):
        text = " ".join(text)  # Convert list of lines into a single string

    if isinstance(text, float) and pd.isna(text):  # Check for NaN values
        return 0

    if not isinstance(text, str):  # Check for unexpected data types
        return 0

    return len(re.findall(r"[.!?]+", text))  # Count sentence endings


####################################################################################################
# Count words
####################################################################################################


def count_words(text):
    """Count the number of words in a text.

    Args:
        text (list or str): The text as a list of lines or a string.

    Returns:
        int: The number of words in the text.
    """
    if isinstance(text, list):
        text = " ".join(text)  # Convert list of lines into a single string

    if isinstance(text, float) and pd.isna(text):  # Check for NaN values
        return 0

    if not isinstance(text, str):  # Check for unexpected data types
        return 0

    return len(re.findall(r"\b\w+\b", text))  # Count words


####################################################################################################
# Remove newline characters in a list of strings
####################################################################################################


def remove_newline_character(text_list):
    """Remove extra newlines from a list of strings.

    Args:
        text_list (list): A list of text lines.

    Returns:
        list: The list with extra newlines removed within each line.
    """
    return [
        re.sub(r"\n+", "", line) for line in text_list
    ]  # Apply to each element in the list


####################################################################################################
# Boolean check for missing values, columns and shape
####################################################################################################


def check_df(df):
    """
    Check for missing values, columns and shape of a DataFrame.
    """
    if df.isna().sum().sum() == 0:
        print("No missing values")
    else:
        for col in df.columns:
            if df[col].isna().sum() > 0:
                print(f"Missing values in {col}")
    print("\ndf columns:", df.columns, "\n\nShape:", df.shape)


####################################################################################################
# NLTK Pipeline for Tokenizing Text
####################################################################################################

# NLTK Pipeline for Tokenizing Text
# Includes lowercasing, tokenization, and stopword removal
# Customizable stopwords with inclusions and exclusions


# Download necessary NLTK resources
print("Downloading NLTK resources...")
nltk.download("punkt_tab")
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
print("Download complete.")


##############################################
# NLPPipeline Class
##############################################
class NLPPipeline:
    """
    A configurable NLP pipeline for linguistic text analysis.

    This class provides methods for text preprocessing, including:
    - Lowercasing
    - Tokenization using NLTK's word_tokenize
    - Punctuation removal with customizable punctuation sets
    - Stopword removal with customizable stopword lists
    """

    def __init__(self, language: str = "english"):
        """
        Initialize the NLP pipeline.

        Args:
            language (str): Language for stopwords (default: 'english')
        """
        self.language = language
        self.stopwords = set(nltk.corpus.stopwords.words(language))
        self.custom_include_stopwords: Set[str] = set()
        self.custom_exclude_stopwords: Set[str] = set()
        self.update_stopwords()

        # Initialize punctuation set with string.punctuation
        self.default_punctuation = set(string.punctuation)
        self.keep_punctuation: Set[str] = set()
        self.punctuation_to_remove: Set[str] = set()
        self.update_punctuation()

    def update_stopwords(self) -> None:
        """
        Update the stopwords set based on custom inclusions and exclusions.
        """
        self.effective_stopwords = self.stopwords.copy()
        self.effective_stopwords |= self.custom_include_stopwords
        self.effective_stopwords -= self.custom_exclude_stopwords

    def update_punctuation(self) -> None:
        """
        Update the punctuation set based on custom inclusions and exclusions.
        """
        self.effective_punctuation = self.default_punctuation.copy()
        self.effective_punctuation -= self.keep_punctuation
        self.effective_punctuation |= self.punctuation_to_remove

    def customize_stopwords(
        self, include: Optional[Set[str]] = None, exclude: Optional[Set[str]] = None
    ) -> None:
        """
        Customize the stopwords by including or excluding specific words.

        Args:
            include (Set[str], optional): Words to add to stopwords
            exclude (Set[str], optional): Words to remove from stopwords
        """
        if include:
            self.custom_include_stopwords |= include
        if exclude:
            self.custom_exclude_stopwords |= exclude
        self.update_stopwords()

        # Print summary of changes
        print(f"Stopwords customized:")
        if include:
            print(f"  Added: {include}")
        if exclude:
            print(f"  Removed: {exclude}")
        print(f"  Total stopwords: {len(self.effective_stopwords)}")

    def customize_punctuation(
        self, keep: Optional[Set[str]] = None, remove: Optional[Set[str]] = None
    ) -> None:
        """
        Customize the punctuation handling by specifying characters to keep or remove.

        Args:
            keep (Set[str], optional): Punctuation characters to keep
            remove (Set[str], optional): Additional characters to remove
        """
        if keep:
            self.keep_punctuation |= keep
        if remove:
            self.punctuation_to_remove |= remove
        self.update_punctuation()

        # Print summary of changes
        print(f"Punctuation customized:")
        if keep:
            print(f"  Keeping: {keep}")
        if remove:
            print(f"  Additional removals: {remove}")
        print(
            f"  Punctuation to be removed: {''.join(sorted(self.effective_punctuation))}"
        )

    def lowercase(self, text: str) -> str:
        """
        Convert text to lowercase.

        Args:
            text (str): Input text

        Returns:
            str: Lowercase text
        """
        if not isinstance(text, str):
            return ""
        return text.lower()

    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize text using NLTK's word_tokenize.

        Args:
            text (str): Input text

        Returns:
            List[str]: List of tokens
        """
        if not isinstance(text, str):
            return []
        text = text.replace("—", " ").replace("–", " ")
        return nltk.tokenize.word_tokenize(text)

    def remove_punctuation(self, tokens: List[str]) -> List[str]:
        """
        Remove punctuation from tokens or filter out punctuation-only tokens.

        Args:
            tokens (List[str]): List of tokens

        Returns:
            List[str]: Tokens with punctuation removed
        """
        # Create a translation table for punctuation removal
        punct_table = str.maketrans("", "", "".join(self.effective_punctuation))

        # Apply translation to each token and filter out empty tokens
        cleaned_tokens = []
        for token in tokens:
            cleaned = token.translate(punct_table)
            if cleaned:  # Only add non-empty tokens
                cleaned_tokens.append(cleaned)

        return cleaned_tokens

    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """
        Remove stopwords from the list of tokens.

        Args:
            tokens (List[str]): List of tokens

        Returns:
            List[str]: Filtered list without stopwords
        """
        return [t for t in tokens if t.lower() not in self.effective_stopwords]

    def get_pipeline(
        self,
        lowercase: bool = True,
        tokenize: bool = True,
        remove_punctuation: bool = True,
        remove_stops: bool = True,
    ) -> List[Callable]:
        """
        Get a customized processing pipeline.

        Args:
            lowercase (bool): Include lowercasing step
            tokenize (bool): Include tokenization step
            remove_punctuation (bool): Include punctuation removal step
            remove_stops (bool): Include stopword removal step

        Returns:
            List[Callable]: List of processing functions
        """
        pipeline = []
        if lowercase:
            pipeline.append(self.lowercase)
        if tokenize:
            pipeline.append(self.tokenize)
        if remove_punctuation:
            pipeline.append(self.remove_punctuation)
        if remove_stops:
            pipeline.append(self.remove_stopwords)
        return pipeline

    def process_text(
        self, text: Union[str, List[str]], pipeline: Optional[List[Callable]] = None
    ) -> Union[str, List[str]]:
        """
        Process a single text (or list of texts) through the pipeline.

        Args:
            text (str or List[str]): Text or list of strings to process
            pipeline (List[Callable], optional): Custom pipeline to use

        Returns:
            Union[str, List[str]]: Processed text or tokens
        """
        if isinstance(text, list):  # If input is a list, join it into a single string
            text = " ".join(text)

        if pipeline is None:
            pipeline = self.get_pipeline()

        result = text
        for transform in pipeline:
            try:
                result = transform(result)
            except Exception as e:
                print(f"Error applying {transform.__name__}: {e}")
        return result

    def process_series(
        self, series: pd.Series, pipeline: Optional[List[Callable]] = None
    ) -> pd.Series:
        """
        Process a pandas Series of texts through the pipeline with progress bar.

        Args:
            series (pd.Series): Series containing texts
            pipeline (List[Callable], optional): Custom pipeline to use

        Returns:
            pd.Series: Series with processed texts/tokens
        """
        if pipeline is None:
            pipeline = self.get_pipeline()

        return series.apply(lambda x: self.process_text(x, pipeline))

    def process_dataframe(
        self,
        df: pd.DataFrame,
        text_column: str,
        result_column: str,
        pipeline: Optional[List[Callable]] = None,
    ) -> pd.DataFrame:
        """
        Process a dataframe by applying the pipeline to a text column.

        Args:
            df (pd.DataFrame): Input dataframe
            text_column (str): Column containing texts to process
            result_column (str): Column name for storing processed results
            pipeline (List[Callable], optional): Custom pipeline to use

        Returns:
            pd.DataFrame: Processed dataframe
        """
        if text_column not in df.columns:
            raise ValueError(f"Column '{text_column}' not found in dataframe")

        result_df = df.copy()
        result_df[result_column] = self.process_series(df[text_column], pipeline)
        return result_df


##################################################
# End of NLPPipeline Class
##################################################
# Initialize the pipeline
nlp = NLPPipeline(language="english")

# Customize stopwords
nlp.customize_stopwords(
    include={
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "'",
        "n",
        "'and",
    },
    exclude={""},
)
# Customize punctuation
nlp.customize_punctuation(
    keep={"-", ""},  # Keep hyphens and apostrophes
    remove={
        r"…",
        "—",
        "”",
        "’",
        "“",
        "‘",
        "-",
        "\\",
    },  # Additional characters to remove
)

# Process with default pipeline (lowercase -> tokenize -> remove punctuation -> remove stopwords)
# df = nlp.process_dataframe(df, 'text', 'tokens')
# df['num_tokens'] = df['tokens'].map(len)


####################################################################################################
# Populate Odyssey DF
####################################################################################################


####################################################################################################
# Populate Odyssey DF
####################################################################################################


####################################################################################################
# Populate Odyssey DF
####################################################################################################


####################################################################################################
# Populate Odyssey DF
####################################################################################################


####################################################################################################
# Populate Odyssey DF
####################################################################################################


####################################################################################################
# Populate Odyssey DF
####################################################################################################


####################################################################################################
# Populate Odyssey DF
####################################################################################################


####################################################################################################
# Populate Odyssey DF
####################################################################################################


####################################################################################################
# Populate Odyssey DF
####################################################################################################
