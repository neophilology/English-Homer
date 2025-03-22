"""_summary_

Returns:
    _type_: _description_
"""

####################################################################################################
# Import Libraries
####################################################################################################

import re

# import numpy as np
import pandas as pd


# import nltk


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
# Populate Odyssey DF
####################################################################################################


def before_after_transformation(text_list, start_idx, end_idx, process_func):
    """
    Extracts a section of text between two indices in a list of strings
    and compares before/after transformation.

    Args:
        text_list (list): A list of strings representing lines of text.
        start_idx (int): The index where the extraction should start.
        end_idx (int): The index where the extraction should end.
        process_func (function): A function that processes the extracted section.

    Returns:
        None: Prints the before/after transformation results.
    """
    # Validate indices
    if not (0 <= start_idx < len(text_list)) or not (0 <= end_idx < len(text_list)):
        print("Error: Indices out of range.")
        return

    if start_idx >= end_idx:
        print("Error: Start index must be before end index.")
        return

    # Extract the section
    section = " ".join(
        text_list[start_idx : end_idx + 1]
    )  # Join selected lines into a single string

    # Process the section
    processed_section = process_func(section)

    # Print results
    print("Original section:\n")
    print(section)
    print("\n\nProcessed section:\n")
    print(processed_section)


# Example usage with a list of text lines
# Apply function with start and end index
# before_after_transformation(text_lines, 3, 6, normalize_text)

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
