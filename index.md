![Homer's Living Network Banner](./assets/images/neoPHilology-BANNER-wLogo.png)

# Homer's Living Network

**Daniel Barrera Rivera**

## Exploring the Homeric Rhizome Across English Translations of the Odyssey

Welcome to the digital home of "Homer's Living Network," a digital humanities project analyzing how Homer's Odyssey has been reimagined across centuries in the English literary tradition.

## Project Overview

This research begins by focusing on translation. It traces the evolution of the Homeric networks from the first English translation in 1615 to contemporary renderings, using computational methods to reveal how translators have transformed the ancient epic for English-speaking readers.

<img src="./assets/images/Aga_mask.png" alt="Agamemnon Gold Mask" width="600"/>

## Project Navigation

Here is the project's tree layout: [project_structure.txt](./project_structure.txt) (wonderers beware: there are 76 directories, 339 files). 

### **Dr. Dellert, here are the Latest Notebooks**

Presently, the project is in the lexical analysis stage almost completed. It is distributed in two notebooks.  

- **Lexical A** includes the TTR, Zipf's Law, and TF-IDF analysis:  

    * [Lexical/lexical_A02.ipynb](https://nbviewer.org/github/neophilology/English-Homer/blob/main/Lexical/lexical_A02.ipynb)

- **Lexical B** is all about etymologies:    
 
    * [Lexical/lexical_B01.ipynb](https://nbviewer.org/github/neophilology/English-Homer/blob/main/Lexical/lexical_B01.ipynb)   

### Notes on the project

The results are not exactly what I expected to have so far but is not for lack of trying and effort—I'm guessing sometimes you have to argue the case with no other smoking gun than p-values. The lack of univocal, "in your face" results likely stems from:

- The long-term nature of this project
- My inexperience in the field
- The trial-and-error nature of NLP experiments involving:
  - Learning to deal with setbacks
  - Redesigning approaches
  - Pivoting when necessary
  - Persevering through challenges

However, I believe the state of the research, as a final term project, is at a presentable level: it is ample but focused and in well enough shape to be read and graded by a (patient) expert. Having said that, even if harsh and drenching, your feedback will be like rain on a dry field—the rain is always unprejudiced and welcomed here.

#### Some Caveats

- **Statistical challenges**: I struggled most with statistical testing and inferences (and got lost more times than I dare to tell)
- **Visualization focus**: I "wasted" lots of time on fancy visualizations (though visualization is a task that I enjoyed)
- **Pre-processing**: All pre-processing can be consulted in the GitHub repo. I didn't include the cleaning of texts in the final notebooks as every text demanded different preprocessing
- **Length constraints**: In consideration with your time, I have edited a lot of material but still came up short with notebooks that are too long
  - Some PDF exports already made for 80 pages per notebook
  - Given this and the fact that most of the project is still in its infancy, I didn't write a full report of the results
  - Discussion of results is included within the notebooks
  - If needed for clarification, proper scientific research style, or other criteria, I can write a comprehensive report






### **OLD Experiments** (Work-In-Progress)

Here is the first batch of dedicated experiments with statistical tests for my selection of six modern translators: "AT_Murray", "Fitzgerald", "Lattimore", "Fagles", "Wilson", "Green". 

– [**Type-Token Ratio**](https://nbviewer.org/github/neophilology/English-Homer/blob/main/Lex_Six_Mo-03_31_25/TTR_Six_Mo-03_31_25.ipynb)

– [**Zipf's Law**](https://nbviewer.org/github/neophilology/English-Homer/blob/main/Lex_Six_Mo-03_31_25/Zipf_Six_Mo-03_31_25.ipynb)

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