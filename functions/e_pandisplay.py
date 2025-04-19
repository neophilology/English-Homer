"""
pandisplay module - Easy display configuration for pandas and other data libraries

This module provides simplified access to display configuration settings for pandas
and other data manipulation libraries.

Usage:
    import pandisplay as pan

    # Apply default settings
    pan.reset()

    # Apply specific configurations
    pan.wide()
    pan.compact()

    # Customize specific settings
    pan.max_rows(100)
    pan.float_precision(4)
"""

import pandas as pd

####################################################################################################
# Module Introduction
####################################################################################################

print("\n*Has Pan taken over?")
print("\t »----> use pan.<func>")

####################################################################################################
# Functions
####################################################################################################


def reset():
    """Reset pandas display options to module defaults (optimized for readability)"""
    pd.set_option("display.max_rows", 2000)
    pd.set_option("display.max_colwidth", 200)
    pd.set_option("display.precision", 2)
    pd.set_option("display.float_format", "{:.2f}".format)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)
    pd.set_option("colheader_justify", "left")
    print("✓ Yes, Pandas display set to e_pandisplay defaults!")
    print("\t »----> use pan.<func>")


def wide():
    """Configure pandas for wide display format"""
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)
    pd.set_option("display.expand_frame_repr", False)
    print("✓ Wide display format applied")


def compact():
    """Configure pandas for compact display format"""
    pd.set_option("display.max_rows", 50)
    pd.set_option("display.max_columns", 20)
    pd.set_option("display.width", 120)
    print("✓ Compact display format applied")


def max_rows(n):
    """Set maximum number of rows to display"""
    pd.set_option("display.max_rows", n)
    print(f"✓ Maximum rows set to {n}")


def max_cols(n=None):
    """Set maximum number of columns to display"""
    pd.set_option("display.max_columns", n)
    if n is None:
        print("✓ All columns will be displayed")
    else:
        print(f"✓ Maximum columns set to {n}")


def max_width(n=None):
    """Set maximum width for display"""
    pd.set_option("display.width", n)
    print(f"✓ Display width set to {n}")


def float_precision(n):
    """Set float precision and format"""
    pd.set_option("display.precision", n)
    pd.set_option("display.float_format", f"{{:.{n}f}}".format)
    print(f"✓ Float precision set to {n} decimal places")


def max_colwidth(n):
    """Set maximum column width before truncation"""
    pd.set_option("display.max_colwidth", n)
    print(f"✓ Maximum column width set to {n}")


def show_options():
    """Display current pandas display options"""
    options = {
        "display.max_rows": pd.get_option("display.max_rows"),
        "display.max_columns": pd.get_option("display.max_columns"),
        "display.max_colwidth": pd.get_option("display.max_colwidth"),
        "display.width": pd.get_option("display.width"),
        "display.precision": pd.get_option("display.precision"),
        "display.float_format": pd.get_option("display.float_format"),
        "colheader_justify": pd.get_option("colheader_justify"),
    }

    print("Current pandas display options:")
    for k, v in options.items():
        if k == "display.float_format" and v is not None:
            print(f"  {k}: <function>")
        else:
            print(f"  {k}: {v}")


# Apply default settings when imported
reset()
