"""
Odyssey Plots Library
===============================

A collection of text processing functions and utilities for analyzing literary texts,
with specific support for processing the Homeric epic poems like The Odyssey.

This module provides:
1. Text segmentation utilities for breaking texts into books/sections
2. DataFrame creation and manipulation functions for structured text analysis
3. Basic text statistics (lines, sentences, words counters)
4. Integration with e_chroma for consistent styling
5. Flexible etymology visualization for translator comparisons

Author: Daniel E. Barrera Rivera
Date: March 2025
Version: 1.0.0
"""

####################################################################################################
# Import Libraries
####################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Union, List, Tuple, Optional, Dict

# Try to import e_chroma for styling consistency
try:
    import e_chroma as chroma

    has_chroma = True
    # Get the color values from chroma's palette
    CHROMA_COLORS = list(chroma.color_palette.values())
except ImportError:
    has_chroma = False
    CHROMA_COLORS = None


####################################################################################################
# Module Introduction
####################################################################################################

print("* OZ is behind the curtain!")
print("\t »----> use oz.<func>")
if has_chroma:
    print("* Using e_chroma color palette for consistent styling")


####################################################################################################
# Styling Functions
####################################################################################################


def apply_custom_style(color_palette=None):
    """
    Apply custom style settings to the current plot

    Parameters:
    color_palette (list, optional): List of colors to use for plotting
    """
    # If we have e_chroma, use its style
    if has_chroma:
        plt.rcParams.update(chroma.danB_plotstyle)

    # Override color cycle if a custom palette is provided
    if color_palette:
        plt.rcParams["axes.prop_cycle"] = plt.cycler(color=color_palette)
    elif has_chroma:
        plt.rcParams["axes.prop_cycle"] = plt.cycler(color=CHROMA_COLORS)


####################################################################################################
# Etymology Visualization Functions
####################################################################################################


def plot_etymology_counts(
    df: pd.DataFrame,
    translator_name: str,
    book_range: Union[int, List[int], Tuple[int, int]] = 0,
    top_n: int = 10,
    figsize: Tuple[int, int] = (12, 8),
    color_palette=None,
):
    """
    Plot the etymology label counts for a specific translator and book(s).

    Parameters:
    df (DataFrame): The DataFrame containing the etymology data
    translator_name (str): The name of the translator to filter by
    book_range (int, list, or tuple): Book number(s) to plot:
        - If int: Plot a single book
        - If list: Plot specific books, e.g. [1, 3, 5]
        - If tuple of length 2: Plot range of books, e.g. (1, 5) for books 1 through 5
    top_n (int): Number of top etymologies to display
    figsize (tuple): Figure dimensions (width, height)
    color_palette (list, optional): Custom color palette to use

    Returns:
    matplotlib.figure.Figure: The created figure object
    """
    # Apply custom styling
    apply_custom_style(color_palette)

    # Filter for the specific translator
    translator_data = df[df["translator"] == translator_name]

    if len(translator_data) == 0:
        print(f"No data found for translator '{translator_name}'")
        print(f"Available translators: {df['translator'].unique()}")
        return None

    # Determine which books to plot
    books_to_plot = []

    if isinstance(book_range, int):
        # Single book
        books_to_plot = [book_range]
    elif isinstance(book_range, list):
        # List of specific books
        books_to_plot = book_range
    elif isinstance(book_range, tuple) and len(book_range) == 2:
        # Range of books (start, end)
        books_to_plot = list(range(book_range[0], book_range[1] + 1))
    else:
        print("Invalid book_range format. Use an integer, list, or tuple (start, end).")
        return None

    # Filter data for the requested books
    book_data = translator_data[translator_data["book_num"].isin(books_to_plot)]

    if len(book_data) == 0:
        print(
            f"No data found for translator '{translator_name}' with the specified book(s)"
        )
        avail_books = sorted(translator_data["book_num"].unique().tolist())
        print(f"Available books for this translator: {avail_books}")
        return None

    # Set up the figure
    n_books = len(book_data)
    fig, axes = plt.subplots(n_books, 1, figsize=(figsize[0], figsize[1] * n_books / 2))

    # If only one book, axes will not be an array
    if n_books == 1:
        axes = [axes]

    # Plot each book
    for i, (_, row) in enumerate(book_data.iterrows()):
        # Get book number
        book_num = row["book_num"]

        # Get etymology counts
        ety_counts = row["ety_label_counts"]

        # Convert dictionary to DataFrame for plotting
        ety_df = pd.DataFrame(list(ety_counts.items()), columns=["Etymology", "Count"])

        # Sort by count in descending order
        ety_df = ety_df.sort_values("Count", ascending=False)

        # Take top N etymologies
        if len(ety_df) > top_n:
            other_count = ety_df.iloc[top_n:]["Count"].sum()
            ety_df = ety_df.iloc[:top_n]
            ety_df = pd.concat(
                [
                    ety_df,
                    pd.DataFrame(
                        [["Other", other_count]], columns=["Etymology", "Count"]
                    ),
                ]
            )

        # Create the plot
        sns.barplot(x="Etymology", y="Count", data=ety_df, ax=axes[i])

        # Customize the plot
        axes[i].set_title(f"Book {book_num}: Etymology Distribution")
        axes[i].set_xlabel("Etymology Label")
        axes[i].set_ylabel("Word Count")

        # Add count labels on top of bars
        for j, v in enumerate(ety_df["Count"]):
            axes[i].text(j, v + 5, str(v), ha="center")

    # Add overall title
    if len(books_to_plot) == 1:
        book_str = f"Book {books_to_plot[0]}"
    else:
        book_str = f"Books {min(books_to_plot)}-{max(books_to_plot)}"

    plt.suptitle(
        f"Etymology Distribution in {translator_name}'s Translation ({book_str})",
        fontsize=16,
        y=1.02,
    )

    plt.tight_layout()
    return fig


def plot_etymology_comparison(
    df: pd.DataFrame,
    translators: List[str],
    book_num: int = 1,
    top_n: int = 10,
    figsize: Tuple[int, int] = (14, 10),
    color_palette=None,
):
    """
    Compare etymology distributions between different translators for a specific book.

    Parameters:
    df (DataFrame): The DataFrame containing the etymology data
    translators (list): List of translator names to compare
    book_num (int): The book number to analyze
    top_n (int): Number of top etymologies to display
    figsize (tuple): Figure dimensions (width, height)
    color_palette (list, optional): Custom color palette to use

    Returns:
    matplotlib.figure.Figure: The created figure object
    """
    # Apply custom styling
    apply_custom_style(color_palette)

    # Set up the figure
    fig, axes = plt.subplots(len(translators), 1, figsize=figsize)

    # If only one translator, axes will not be an array
    if len(translators) == 1:
        axes = [axes]

    # For each translator, plot their etymology distribution
    for i, translator in enumerate(translators):
        # Filter data
        translator_data = df[
            (df["translator"] == translator) & (df["book_num"] == book_num)
        ]

        if len(translator_data) == 0:
            axes[i].text(
                0.5,
                0.5,
                f"No data for {translator}, Book {book_num}",
                ha="center",
                va="center",
                fontsize=14,
            )
            axes[i].set_title(f"{translator}'s Translation (No Data)")
            continue

        # Get etymology counts
        ety_counts = translator_data.iloc[0]["ety_label_counts"]

        # Convert to DataFrame for plotting
        ety_df = pd.DataFrame(list(ety_counts.items()), columns=["Etymology", "Count"])
        ety_df = ety_df.sort_values("Count", ascending=False)

        # Take top N etymologies
        if len(ety_df) > top_n:
            other_count = ety_df.iloc[top_n:]["Count"].sum()
            ety_df = ety_df.iloc[:top_n]
            ety_df = pd.concat(
                [
                    ety_df,
                    pd.DataFrame(
                        [["Other", other_count]], columns=["Etymology", "Count"]
                    ),
                ]
            )

        # Plot
        sns.barplot(x="Etymology", y="Count", data=ety_df, ax=axes[i])

        # Customize
        axes[i].set_title(f"{translator}'s Translation")
        axes[i].set_xlabel("Etymology Label")
        axes[i].set_ylabel("Word Count")

        # Add count labels
        for j, v in enumerate(ety_df["Count"]):
            axes[i].text(j, v + 5, str(v), ha="center")

    # Overall title
    plt.suptitle(f"Etymology Comparison for Book {book_num}", fontsize=16, y=1.02)
    plt.tight_layout()

    return fig


def plot_etymology_heatmap(
    df: pd.DataFrame,
    translator_name: str,
    book_range: Union[Tuple[int, int], List[int]] = (1, 24),
    top_n: int = 10,
    figsize: Tuple[int, int] = (12, 10),
    cmap: str = None,
):
    """
    Create a heatmap showing etymology distributions across multiple books for a translator.

    Parameters:
    df (DataFrame): The DataFrame containing the etymology data
    translator_name (str): The name of the translator to analyze
    book_range (tuple or list): Range of books to include:
        - If tuple of length 2: (start, end) for book range
        - If list: Specific books to include
    top_n (int): Number of top etymologies to include
    figsize (tuple): Figure dimensions (width, height)
    cmap (str, optional): Colormap to use (e.g., "Blues", "YlOrRd")
                         If None and e_chroma is available, uses a colormap
                         based on e_chroma's color palette

    Returns:
    matplotlib.figure.Figure: The created figure object
    """
    # Apply custom styling (don't pass color_palette since heatmap uses cmap)
    apply_custom_style()

    # Determine colormap
    if cmap is None:
        if has_chroma:
            # Use the first color from chroma's palette
            base_color = CHROMA_COLORS[0]
            cmap = "Blues"  # Default fallback
        else:
            cmap = "Blues"

    # Filter for the translator
    translator_data = df[df["translator"] == translator_name]

    if len(translator_data) == 0:
        print(f"No data found for translator '{translator_name}'")
        print(f"Available translators: {df['translator'].unique()}")
        return None

    # Determine which books to plot
    if isinstance(book_range, tuple) and len(book_range) == 2:
        books_to_plot = list(range(book_range[0], book_range[1] + 1))
    elif isinstance(book_range, list):
        books_to_plot = book_range
    else:
        print(
            "Invalid book_range format. Use a tuple (start, end) or a list of specific books."
        )
        return None

    # Filter for those books
    book_data = translator_data[translator_data["book_num"].isin(books_to_plot)]

    if len(book_data) == 0:
        print(f"No data found for the specified books")
        avail_books = sorted(translator_data["book_num"].unique().tolist())
        print(f"Available books for {translator_name}: {avail_books}")
        return None

    # First, identify the overall top N etymologies across all selected books
    all_etymologies = {}

    for _, row in book_data.iterrows():
        ety_counts = row["ety_label_counts"]
        for ety, count in ety_counts.items():
            if ety in all_etymologies:
                all_etymologies[ety] += count
            else:
                all_etymologies[ety] = count

    top_etymologies = sorted(all_etymologies.items(), key=lambda x: x[1], reverse=True)[
        :top_n
    ]
    top_ety_labels = [ety[0] for ety in top_etymologies]

    # Create a matrix for the heatmap
    heatmap_data = []
    book_labels = []

    for _, row in book_data.sort_values("book_num").iterrows():
        book_num = row["book_num"]
        book_labels.append(f"Book {book_num}")

        ety_counts = row["ety_label_counts"]
        row_data = [ety_counts.get(ety, 0) for ety in top_ety_labels]
        heatmap_data.append(row_data)

    # Convert to numpy array for heatmap
    heatmap_array = np.array(heatmap_data)

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Create heatmap
    sns.heatmap(
        heatmap_array,
        annot=True,
        fmt="d",
        cmap=cmap,
        xticklabels=top_ety_labels,
        yticklabels=book_labels,
        ax=ax,
    )

    # Customize
    ax.set_xlabel("Etymology")
    ax.set_ylabel("Book")
    plt.title(f"Etymology Distribution for {translator_name}'s Translation")
    plt.tight_layout()

    return fig


def save_with_chroma(fig, filename, **kwargs):
    """
    Save a figure using e_chroma.save_figure if available, otherwise use plt.savefig

    Parameters:
    fig (matplotlib.figure.Figure): The figure to save
    filename (str): The filename to save to (without extension)
    **kwargs: Additional arguments to pass to the save function
    """
    if has_chroma:
        # Use chroma's save_figure function
        chroma.save_figure(fig, filename, **kwargs)
    else:
        # Fall back to standard matplotlib savefig
        format = kwargs.get("format", "png")
        dpi = kwargs.get("dpi", 300)
        bbox_inches = kwargs.get("bbox_inches", "tight")
        pad_inches = kwargs.get("pad_inches", 0.4)

        fig.savefig(
            f"{filename}.{format}",
            format=format,
            dpi=dpi,
            bbox_inches=bbox_inches,
            pad_inches=pad_inches,
        )
        print(f"Figure saved as {filename}.{format}")


# Example usage:
# Single book: plot_etymology_counts(odyssey_df, "Murray", book_range=1)
# Multiple specific books: plot_etymology_counts(odyssey_df, "Murray", book_range=[1, 5, 9])
# Range of books: plot_etymology_counts(odyssey_df, "Murray", book_range=(1, 5))
#
# Compare translators: plot_etymology_comparison(odyssey_df, ["Murray", "Butler", "Pope"], book_num=1)
#
# Create heatmap: plot_etymology_heatmap(odyssey_df, "Murray", book_range=(1, 24))
#
# Save with chroma: save_with_chroma(fig, "my_etymology_plot", format="pdf")
