"""
e_chroma: A Custom Visualization Module
===========================

A visualization utility module with custom styles, color palettes,
and figure saving functionality for consistent and aesthetically
pleasing data visualizations.

This module provides:
1. A predefined color palette with named colors
2. Custom Matplotlib plot style settings
3. A utility function for saving figures with consistent parameters

The module leverages Matplotlib and Seaborn for visualization capabilities.

Example:
    >>> import e_chroma as chroma
    >>> # Create a plot with the custom style
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], [4, 5, 6])
    >>> chroma.save_figure(fig, "my_plot", format="pdf")

Author: Daniel E. Barrera-Rivera
Date: March 2025
Version: 1.0.0
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Default output path
output_path_plots = "./Homer_xplots/"


def set_output_path(path):
    """
    Set the output path for saving figures.

    Args:
        path (str): Path where figures will be saved

    Returns:
        None
    """
    global output_path_plots
    output_path_plots = path
    os.makedirs(os.path.dirname(output_path_plots), exist_ok=True)
    print(f"Output path set to: {output_path_plots}")


# Set Seaborn style
# sns.set_style("whitegrid")
print("\n* Got some chroma in your soma, Oma!")
print("\t »----> use chroma.save_figure(fig, 'my_plot')")
print(f"Default output path: {output_path_plots}")

####################################################################################################
# Color Palette Definition
####################################################################################################

# Define a named color palette dictionary
color_palette = {
    "astroblue": "#003D59",
    "orange": "#FD6626",
    "genoa": "#177070",
    "carrot": "#FB871D",
    "tawny": "#641B5E",
    "neptune": "#86C3BC",
    "jazzberry": "#B0124D",
    "mako": "#414A4F",
    "black": "k",
    "lavender": "#F5E1FD",
}

####################################################################################################
# Plot Style Configuration
####################################################################################################

# Custom Matplotlib settings using the dictionary
danB_plotstyle = {
    "figure.figsize": (12, 7),
    "axes.labelsize": "large",
    "axes.titlesize": "large",
    "axes.titleweight": "bold",
    "xtick.labelsize": "large",
    "ytick.labelsize": "small",
    "grid.color": "k",
    "grid.linestyle": ":",
    "grid.linewidth": 0.2,
    "font.family": "Times New Roman",
    "grid.alpha": 0.5,
    "figure.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.4,
    "axes.titlepad": 15,
    "axes.labelpad": 8,
    "legend.borderpad": 0.6,
    "axes.prop_cycle": plt.cycler(
        color=list(color_palette.values())
    ),  # Use dictionary values for cycling colors
}

# Apply the settings
plt.rcParams.update(danB_plotstyle)

####################################################################################################
# Figure Saving Utility
####################################################################################################


def save_figure(
    fig, filename, dpi=400, format="png", bbox_inches="tight", pad_inches=0.4
):
    """
    Save the given Matplotlib figure with specific parameters.

    This function ensures consistent figure saving across the project with
    predefined default parameters for high-quality output.

    Args:
        fig (matplotlib.figure.Figure): The figure to save.
        filename (str): File path or name (without extension).
        dpi (int, optional): Dots per inch for resolution (default: 300).
        format (str, optional): File format extension (default: "png").
        bbox_inches (str, optional): Bounding box setting (default: "tight").
        pad_inches (float, optional): Padding around the figure (default: 0.4).

    Returns:
        None: The function prints a confirmation message after saving.

    Example:
        >>> fig, ax = plt.subplots()
        >>> ax.plot([1, 2, 3], [4, 5, 6])
        >>> save_figure(fig, "my_plot", format="pdf")
    """
    global output_path_plots

    # Ensure filename doesn't have format extension already
    if filename.endswith(f".{format}"):
        filename = filename[: -len(f".{format}")]

    # Create full path
    full_path = os.path.join(output_path_plots, f"{filename}.{format}")

    # Ensure the output directory exists
    os.makedirs(output_path_plots, exist_ok=True)

    fig.savefig(
        full_path,
        dpi=dpi,
        format=format,
        bbox_inches=bbox_inches,
        pad_inches=pad_inches,
    )
    print(f"Figure saved as {full_path} at {dpi} DPI")


####################################################################################################
# Usage Examples
####################################################################################################

# Example usage:
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3], [4, 5, 6])
# save_figure(fig, "my_plot", dpi=300, format="pdf")

####################################################################################################
# Helper Functions (Add any additional visualization functions below)
####################################################################################################

# Future functions can be added here
