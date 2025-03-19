# Description: Random functions that I use frequently


# Boolean check for missing values in df
if df.isna().sum().sum() == 0:
    print("No missing values")
else:
    for col in df.columns:
        if df[col].isna().sum() > 0:
            print(f"Missing values in {col}")


# Inverse document frequency (IDF) is a measure of how unique a word is across documents.
# Words that appear in many documents have low IDF, while words that appear in few documents have high IDF.
# This can be useful for identifying keywords or important terms in a collection of texts.
def compute_idf(df, column="tokens", preprocess=None, min_df=2):
    """A fucntion to compute the inverse document frequency (IDF) of tokens in a data frame.

    Args:
        df (_type_):
        column (str, optional): _description_. Defaults to 'tokens'.
        preprocess (_type_, optional): _description_. Defaults to None.
        min_df (int, optional): _description_. Defaults to 2.
    """

    def update(doc):
        tokens = doc if preprocess is None else preprocess(doc)
        counter.update(set(tokens))

    # count tokens
    counter = Counter()
    df[column].progress_map(update)

    # create data frame and compute idf
    idf_df = pd.DataFrame.from_dict(counter, orient="index", columns=["df"])
    idf_df = idf_df.query("df >= @min_df")
    idf_df["idf"] = np.log(len(df) / idf_df["df"]) + 0.1
    idf_df.index.name = "token"
    return idf_df


from collections import Counter  ###


def count_words(df, column="tokens", preprocess=None, min_freq=2):

    # process tokens and update counter
    def update(doc):
        tokens = doc if preprocess is None else preprocess(doc)
        counter.update(tokens)

    # create counter and run through all data
    counter = Counter()
    df[column].progress_map(update)

    # transform counter into data frame
    freq_df = pd.DataFrame.from_dict(counter, orient="index", columns=["freq"])
    freq_df = freq_df.query("freq >= @min_freq")
    freq_df.index.name = "token"

    return freq_df.sort_values("freq", ascending=False)


freq_df = count_words(df)
freq_df.head(30)

from collections import Counter

counter = Counter()
df["tokens"].map(counter.update)
keywords = [word for word, count in counter.most_common(10)]
keywords_count = counter.most_common(10)
print(keywords)
print(keywords_count)

# finding a token in token columns
token = "penelope"
penelopes = df["tokens"].map(lambda tokens: token in tokens).sum()
penelopes
