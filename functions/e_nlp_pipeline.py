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

print('Pipiline live! use e.NLPPipeline(language="english")')


####################################################################################################
# NLTK Pipeline for Tokenizing Text
####################################################################################################

# Includes lowercasing, tokenization, and stopword removal
# Customizable stopwords with inclusions and exclusions

# Download necessary NLTK resources
print("Downloading NLTK resources...")
nltk.download("punkt_tab")
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
print("Download complete.")


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
        self, text: str, pipeline: Optional[List[Callable]] = None
    ) -> Union[str, List[str]]:
        """
        Process a single text through the pipeline.

        Args:
            text (str): Text to process
            pipeline (List[Callable], optional): Custom pipeline to use

        Returns:
            Union[str, List[str]]: Processed text or tokens
        """
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
        Process a pandas Series of texts through the pipeline.

        Args:
            series (pd.Series): Series containing texts
            pipeline (List[Callable], optional): Custom pipeline to use

        Returns:
            pd.Series: Series with processed texts/tokens
        """
        if pipeline is None:
            pipeline = self.get_pipeline()

        tqdm.pandas(desc="Processing texts")
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

        # Ensure pipeline is assigned
        if pipeline is None:
            pipeline = (
                self.get_pipeline()
            )  # Fetch the default pipeline if none is provided

        # Check again to avoid NoneType errors
        if not pipeline:
            print("Warning: Pipeline is empty. No processing will be applied.")
            return df.copy()

        # Print pipeline steps in a human-readable format
        print("\nProcessing pipeline steps:")
        print(" → ".join([func.__name__ for func in pipeline]))

        result_df = df.copy()
        result_df[result_column] = self.process_series(df[text_column], pipeline)

        return result_df


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
