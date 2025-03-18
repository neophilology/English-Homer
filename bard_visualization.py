import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set_style("whitegrid")

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
