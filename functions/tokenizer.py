# NLTK Pipeline for Tokenizing Text
# Includes lowercasing, tokenization, and stopword removal
# Customizable stopwords with inclusions and exclusions

import nltk
import pandas as pd
from tqdm.notebook import tqdm
import re
from typing import List, Callable, Union, Set, Optional

# Download necessary NLTK resources
print("Downloading NLTK resources...")
nltk.download('punkt_tab')
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
print("Download complete.")

class NLPPipeline:
    """
    A configurable NLP pipeline for linguistic text analysis.
    
    This class provides methods for text preprocessing, including:
    - Lowercasing
    - Tokenization using NLTK's word_tokenize
    - Stopword removal with customizable stopword lists
    """
    
    def __init__(self, language: str = 'english'):
        """
        Initialize the NLP pipeline.
        
        Args:
            language (str): Language for stopwords (default: 'english')
        """
        self.language = language
        self.stopwords = set(nltk.corpus.stopwords.words(language))
        self.custom_include: Set[str] = set()
        self.custom_exclude: Set[str] = set()
        self.update_stopwords()
    
    def update_stopwords(self) -> None:
        """
        Update the stopwords set based on custom inclusions and exclusions.
        """
        self.effective_stopwords = self.stopwords.copy()
        self.effective_stopwords |= self.custom_include
        self.effective_stopwords -= self.custom_exclude
    
    def customize_stopwords(self, include: Optional[Set[str]] = None, 
                           exclude: Optional[Set[str]] = None) -> None:
        """
        Customize the stopwords by including or excluding specific words.
        
        Args:
            include (Set[str], optional): Words to add to stopwords
            exclude (Set[str], optional): Words to remove from stopwords
        """
        if include:
            self.custom_include |= include
        if exclude:
            self.custom_exclude |= exclude
        self.update_stopwords()
        
        # Print summary of changes
        print(f"Stopwords customized:")
        if include:
            print(f"  Added: {include}")
        if exclude:
            print(f"  Removed: {exclude}")
        print(f"  Total stopwords: {len(self.effective_stopwords)}")
    
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
        return nltk.tokenize.word_tokenize(text)
    
    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """
        Remove stopwords from the list of tokens.
        
        Args:
            tokens (List[str]): List of tokens
            
        Returns:
            List[str]: Filtered list without stopwords
        """
        return [t for t in tokens if t.lower() not in self.effective_stopwords]
    
    def get_pipeline(self, lowercase: bool = True, 
                    tokenize: bool = True, 
                    remove_stops: bool = True) -> List[Callable]:
        """
        Get a customized processing pipeline.
        
        Args:
            lowercase (bool): Include lowercasing step
            tokenize (bool): Include tokenization step
            remove_stops (bool): Include stopword removal step
            
        Returns:
            List[Callable]: List of processing functions
        """
        pipeline = []
        if lowercase:
            pipeline.append(self.lowercase)
        if tokenize:
            pipeline.append(self.tokenize)
        if remove_stops:
            pipeline.append(self.remove_stopwords)
        return pipeline
    
    def process_text(self, text: str, pipeline: Optional[List[Callable]] = None) -> Union[str, List[str]]:
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
    
    def process_series(self, series: pd.Series, pipeline: Optional[List[Callable]] = None) -> pd.Series:
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
        
        tqdm.pandas(desc="Processing texts")
        return series.progress_apply(lambda x: self.process_text(x, pipeline))
    
    def process_dataframe(self, df: pd.DataFrame, text_column: str, 
                         result_column: str, pipeline: Optional[List[Callable]] = None) -> pd.DataFrame:
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

# Example usage

# Initialize the pipeline
nlp = NLPPipeline(language='english')

# Customize stopwords
nlp.customize_stopwords(
    include={'dear', 'regards', 'must', 'would', 'also'},
    exclude={'against'}
)

# Create a sample dataframe
sample_texts = [
    "Hello world! This is a test. Against all odds.",
    "Dear reader, you must consider this example would also be useful.",
    "Literary analysis requires careful attention to detail and context."
]
sample_df = pd.DataFrame({'text': sample_texts})

# Process with default pipeline (lowercase → tokenize → remove stopwords)
processed_df = nlp.process_dataframe(sample_df, 'text', 'tokens')

# Display results
print("\nProcessed DataFrame:")
for i, row in processed_df.iterrows():
    print(f"\nText: {row['text']}")
    print(f"Tokens: {row['tokens']}")

# Example with custom pipeline (only tokenize, no lowercase or stopword removal)
custom_pipeline = nlp.get_pipeline(lowercase=False, remove_stops=False)
tokenized_df = nlp.process_dataframe(sample_df, 'text', 'raw_tokens', pipeline=custom_pipeline)

print("\n\nTokenized only DataFrame:")
for i, row in tokenized_df.iterrows():
    print(f"\nText: {row['text']}")
    print(f"Raw tokens: {row['raw_tokens']}")

********************************************************************************************************************

import nltk
import re
from tqdm import tqdm
import pandas as pd

# Download necessary NLTK resources
nltk.download("stopwords", quiet=True)

# Initialize stopwords
stopwords = set(nltk.corpus.stopwords.words("english"))

# Custom stopword handling
include_stopwords = {"dear", "regards", "must", "would", "also"}
exclude_stopwords = {"against"}
stopwords |= include_stopwords
stopwords -= exclude_stopwords


def tokenize(text):
    """
    Tokenize text using regex pattern that handles alphanumeric tokens with hyphens
    and ensures at least one letter character is present.

    Args:
        text (str): Input text to tokenize

    Returns:
        list: List of tokens
    """
    if not isinstance(text, str):
        return []
    return re.findall(r"[\w-]*\p{L}[\w-]*", text)


def remove_stop(tokens):
    """
    Remove stopwords from the token list.

    Args:
        tokens (list): List of tokens

    Returns:
        list: Filtered list of tokens without stopwords
    """
    return [t for t in tokens if t.lower() not in stopwords]


def print_tokens(tokens):
    """
    Print tokens joined with a pipe character.

    Args:
        tokens (list): List of tokens to print
    """
    print("|".join(tokens))


def prepare(text, pipeline):
    """
    Apply a series of transformations to text.

    Args:
        text (str): Input text
        pipeline (list): List of functions to apply in sequence

    Returns:
        list/str: Processed text after applying all transformations
    """
    result = text
    for transform in pipeline:
        try:
            result = transform(result)
        except Exception as e:
            print(f"Error applying {transform.__name__}: {e}")
            # Continue with partial result instead of failing
    return result


# Define the processing pipeline
pipeline = [lambda x: x.lower() if isinstance(x, str) else "", tokenize, remove_stop]


# Apply the pipeline to the dataframe with progress bar
def process_dataframe(df, text_column="text", token_column="tokens"):
    """
    Process a dataframe by applying the NLP pipeline to a text column.

    Args:
        df (pandas.DataFrame): Input dataframe
        text_column (str): Column containing text to process
        token_column (str): Column name for storing processed tokens

    Returns:
        pandas.DataFrame: Processed dataframe
    """
    # Check if text column exists
    if text_column not in df.columns:
        raise ValueError(f"Column '{text_column}' not found in dataframe")

    # Apply the pipeline with progress tracking
    tqdm.pandas(desc="Processing text")
    df[token_column] = df[text_column].progress_apply(prepare, pipeline=pipeline)

    return df


# Example usage
if __name__ == "__main__":
    # Create a sample dataframe
    sample_df = pd.DataFrame(
        {"text": ["Hello world! This is a test.", "Another example with stopwords."]}
    )

    # Process the dataframe
    processed_df = process_dataframe(sample_df)

    # Display results
    print(processed_df)
