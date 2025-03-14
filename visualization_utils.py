# visualization_utils.py

import matplotlib.pyplot as plt
import seaborn as sns
import warnings

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
