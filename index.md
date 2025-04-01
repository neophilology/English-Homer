![Homer's Living Network Banner](./assets/images/neoPHilology-BANNER-wLogo.png)

# Homer's Living Network

**Daniel Barrera Rivera**

## Exploring the Homeric Rhizome Across English Translations of the Odyssey

Welcome to the digital home of "Homer's Living Network," a digital humanities project analyzing how Homer's Odyssey has been reimagined across centuries, becoming part of the English literary tradition.

## Project Overview

This research begins by focusing on translation. It traces the evolution of the Homeric networks from the first English translation in 1615 to contemporary renderings, using computational methods to reveal how translators have transformed the ancient epic for English-speaking audiences.

By combining data science with traditional philology and cultural studies, the patterns that have shaped our understanding of Homer's world reflect how we have shaped Homer in return.

Here is the project's tree layout: [project_structure.txt](./project_structure.txt) (57 directories, 235 files). 


<img src="./assets/images/Aga_mask.png" alt="Agamemnon Gold Mask" width="600"/>

## Project Navigation

### **Experiments** (Work-In-Progress)

Here is the first batch of dedicated experiments with statistical tests for my selection of six modern translators: "AT_Murray", "Fitzgerald", "Lattimore", "Fagles", "Wilson", "Green". 

– [**Type-Token Ratio**](https://nbviewer.org/github/neophilology/English-Homer/blob/main/Six_XXth_Lexical/Six_XX_GRUFF_TTR.ipynb)

– [**Zipf's Law**](https://nbviewer.org/github/neophilology/English-Homer/blob/main/Zipf_Six_Modern/Zipf_Six_Modern_SKIMMED.ipynb)

– [**Token Frequency-Inverse Document Frequency (TFIDF)**](https://nbviewer.org/github/neophilology/English-Homer/blob/main/tfidf_Six_Mo/tfidf_Six_Mo.ipynb)

– [**Etymology A** (preliminary)](https://nbviewer.org/github/neophilology/English-Homer/blob/main/Etymology_Six_Modern.ipynb)

– [**Etymology B**](https://nbviewer.org/github/neophilology/English-Homer/blob/main/Etymology_Six_Modern/Etymology_Six_Modern_B.ipynb)


#### Early Experiments 
Here is the minimum viable product (MVP) to try out if the research approach works:

- [**The Notebook!** - MVP Lexical Analysis](https://nbviewer.org/github/neophilology/English-Homer/blob/main/MVP_Green-Wilson/MVP_Lexical.ipynb)

It focuses on statistical analysis and lexical diversity of the best contemporary translations of the Odyssey:
- Peter Green, 2018, University of California Press
- Emily Wilson, 2017, W.W. Norton & Company

**NB:** The texts are not distributed or collected here in any manner.

### The Exploratory Notebooks WIll be Here



In here you can find notebooks for preprocessing, like pruning the text and normalizing it:

- [Cleaners](#) *(coming soon)*
- [Normalizers](#) *(coming soon)*
- [Dataframers](#) *(coming soon)*

### Documentation

- [Project Description](./README.md) - An introduction to our research goals and methodology
- [Research Questions](./research-questions.md) - The core inquiries driving our analysis
- [Research Design](./ResearchDesign.md) - Our methodological approach and analytical framework
- [Data Overview](./data.md) - Documentation of our translation corpus and datasets
- [Corpus Schema](./XML-schema-corpus.md) – Describes the structure of selected translations

## Latest Updates
- **April 1st, 2025**: Four experiments for six modern Odysseys: 
    * odysseys = ["AT_Murray", "Fitzgerald", "Lattimore", "Fagles", "Wilson", "Green"]
    * experiments = ["TTR", "Zipf", "TFIDF", Etymology"]
    *plus:* Lots of plots, EDA per translator, carpel tunnel from the mouse and a hunch on my back.

- **March 16th, 2025**: Project is live!

## About the Project

This research is being conducted as part of a dissertation at the University of Tübingen, combining approaches from computational linguistics, classical reception studies, and translation theory.

The project aims to demonstrate how computational methods can reveal patterns in literary and cultural history that effectively transform our concept of tradition––that living story that keeps telling and retelling our story.

## Contact

<img src="./assets/images/Dan_BW02.png" alt="Daniel Barrera Rivera" width="200"/>

For questions, collaboration requests, or more information:

- Email: [neophilology@gmail.com](mailto:neophilology@gmail.com)
- GitHub: [https://github.com/neophilology](https://github.com/neophilology)

## Future Commits (I'm only Human, Not procrastinating)

- [Network Visualizations](./visualizations.md) - Interactive character networks by translation era
- [Translation Timeline](./timeline.md) - Chronology of English Odyssey translations
- [Preliminary Findings](./findings.md) - Initial results and observations

## Explore the Data

- [Translation Comparison Tool](./tools/translation-comparison.html) - Compare epithets and speech patterns
- [Character Centrality Dashboard](./tools/character-centrality.html) - Track importance of characters over time
- [Translation Network Gallery](./gallery.md) - Visual representations of each translation's network
- [Data Repository](https://github.com/neophilology/homers-living-network) - Access our code and datasets