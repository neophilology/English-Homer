# visualization_utils.py

import matplotlib.pyplot as plt
import seaborn as sns
import warnings


def setup_visualization_params():
    """
    Set up matplotlib and seaborn visualization parameters for consistent
    styling across notebooks.

    Returns:
        list: Color palette for easy access in notebooks
    """
    # Suppress all warnings
    warnings.filterwarnings("ignore")

    # Set seaborn style
    sns.set_style("whitegrid")

    # Define color palette
    # astroblue   orange   genoa      carrot    tawny     neptune    SELAGO    mako    black
    colors = [
        "#003D59",
        "#FD6626",
        "#177070",
        "#FB871D",
        "#641B5E",
        "#86C3BC",
        "#F5E1FD",
        "#414A4F",
        "k",
    ]

    # Define plot style parameters
    plot_style = {
        "figure.figsize": (12, 7),
        "axes.labelsize": "large",  # fontsize for x and y labels
        "axes.titlesize": "large",  # fontsize for title
        "axes.titleweight": "bold",  # font type for title
        "xtick.labelsize": "large",  # fontsize for x ticks
        "ytick.labelsize": "small",  # fontsize for y ticks
        "grid.color": "k",  # grid color
        "grid.linestyle": ":",  # grid line style
        "grid.linewidth": 0.2,  # grid line width
        "font.family": "Times New Roman",  # font family
        "grid.alpha": 0.5,  # transparency of grid
        "figure.dpi": 300,  # figure display resolution
        "savefig.bbox": "tight",  # tight bounding box
        "savefig.pad_inches": 0.4,  # padding to use when saving
        "axes.titlepad": 15,  # title padding
        "axes.labelpad": 8,  # label padding
        "legend.borderpad": 0.6,  # legend border padding
        "axes.prop_cycle": plt.cycler(color=colors),  # color cycle
    }

    # Apply style parameters
    plt.rcParams.update(plot_style)

    return colors


def create_figure(width=12, height=7):
    """
    Create a new figure with the project's styling.

    Args:
        width (int, optional): Figure width in inches. Defaults to 12.
        height (int, optional): Figure height in inches. Defaults to 7.

    Returns:
        tuple: Figure and axis objects
    """
    fig, ax = plt.subplots(figsize=(width, height))
    return fig, ax


def save_figure(fig, filename, dpi=300, bbox_inches="tight", pad_inches=0.4):
    """
    Save figure with consistent parameters.

    Args:
        fig: Matplotlib figure object
        filename (str): Output filename (with path)
        dpi (int, optional): Resolution. Defaults to 300.
        bbox_inches (str, optional): Bounding box setting. Defaults to 'tight'.
        pad_inches (float, optional): Padding. Defaults to 0.4.
    """
    fig.savefig(filename, dpi=dpi, bbox_inches=bbox_inches, pad_inches=pad_inches)
    print(f"Figure saved to {filename}")


# For direct access to colors in notebooks
COLORS = [
    "#003D59",  # astroblue
    "#FD6626",  # orange
    "#177070",  # genoa
    "#FB871D",  # carrot
    "#641B5E",  # tawny
    "#86C3BC",  # neptune
    "#F5E1FD",  # SELAGO
    "#414A4F",  # mako
    "k",  # black
]


# EXAMPLE USAGE IN NOTEBOOK
"""
%matplotlib inline
import sys
import os
import matplotlib.pyplot as plt  

# Add the directory containing visualization_utils.py to path
sys.path.append("/path/to/modules")

# Import the module
import visualization_utils as viz

# Set up visualization parameters
colors = viz.setup_visualization_params()

# Create a standard figure
fig, ax = viz.create_figure()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title("My Plot")

# Create a custom-sized figure
fig, ax = viz.create_figure(width=16, height=9)

# Ensure COLORS exists and is accessible
if hasattr(viz, "COLORS") and len(viz.COLORS) > 2:
    plt.plot([1, 2, 3], [4, 5, 6], color=viz.COLORS[2])  # Use color safely
else:
    print("Warning: viz.COLORS is not defined correctly.")

# Save the figure
viz.save_figure(fig, "my_analysis_plot.png")
"""
