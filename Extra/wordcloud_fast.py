import sys
import os
import nltk
from wordcloud import WordCloud
from matplotlib import pyplot as plt


def main():
    # Check if a filename was provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python wordcloud_fast.py <text_file.txt>")
        sys.exit(1)

    # Get the input file path from command line argument
    filepath = sys.argv[1]

    # Check if file exists
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    # Read the input file
    try:
        with open(filepath, "r", encoding="utf-8-sig") as file:
            extracted_lines = file.readlines()
        text = "".join(extracted_lines)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Ensure stopwords are available
    nltk.download("stopwords", quiet=True)
    stopwords = set(nltk.corpus.stopwords.words("english"))

    # Create output directory for plots if it doesn't exist
    output_path_plots = "wordcloud_output"
    os.makedirs(output_path_plots, exist_ok=True)

    # Get base filename for output
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    output_file = f"{output_path_plots}/wordcloud_{base_filename}.png"

    # Generate the word cloud
    generate_wordcloud(text, output_file, f"WordCloud: {base_filename}")

    print(f"WordCloud successfully generated and saved to {output_file}")


def generate_wordcloud(text, output_file, title="WordCloud Visualization"):
    """
    Generate and save a word cloud from a given text.

    Parameters:
    - text (str): Input text for word cloud generation.
    - output_file (str): Path to save the wordcloud image.
    - title (str): Title for the visualization.
    """
    # Ensure stopwords are available
    nltk.download("stopwords", quiet=True)
    stopwords = set(nltk.corpus.stopwords.words("english"))

    # Initialize WordCloud with better aesthetics
    wc = WordCloud(
        max_words=150,  # Increased max words for richer visualization
        stopwords=stopwords,
        background_color="black",  # Clear background
        colormap="coolwarm",  # More visually appealing colors
        contour_color="black",  # Outline around words
        contour_width=1.5,
        width=800,
        height=400,
    )

    # Generate the word cloud
    wc.generate(text)

    # Plot the word cloud
    plt.figure(figsize=(12, 7), dpi=300)  # Higher resolution for clarity
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title, fontsize=16, fontweight="bold", pad=15)
    plt.savefig(output_file, bbox_inches="tight", dpi=300)  # Save the figure
    plt.close()  # Close the figure to avoid displaying it in non-interactive environments


if __name__ == "__main__":
    main()
