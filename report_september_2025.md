# Measuring Translator Agency: 
# A Computational Analysis of 20th Century Odyssey Translations
---



## **1. Introduction**

The Odyssey's journey into English literature represents one of the most extensive translation traditions in literary history, with over eighty complete renderings produced since the epic first arrived in Britain in the Thirteenth Century. This remarkable corpus offers an unprecedented opportunity to examine how literary texts undergo transformation and naturalization within a target culture. Rather than viewing these translations as mere linguistic transfers, this study approaches them as a living network of texts that collectively shape and reshape the Homeric presence in English letters. 

This investigation addresses a fundamental question in translation studies: How does variation emerge in English translations of Homer's Odyssey? The question gains particular significance when considering translation as what Robinson (2016) terms a "negotiated space"—a dynamic intermediary zone where source language conventions, target language expectations, and translator agency intersect. Within this space, each translator navigates between fidelity to the ancient Greek text and conformity to contemporary cultural and linguistic norms, creating what Lefevere (1992, 1996) identifies as "transformative rewriting" that actively shapes literary canon formation.

The present study employs computational methods to analyze six twentieth and twenty-first century Odyssey translations spanning a full century (1919-2018), using Virginia Woolf's *The Voyage Out* (1915) as a prose baseline. This temporal range captures significant shifts in translation philosophy—from Murray's scholarly approach through the mid-century poetic experiments of Fitzgerald (the grand) and Lattimore (the vernacular), to the contemporary approaches of Fagles (the muscular), Wilson (the interpreter), and Green (the philologist). Each translation represents not merely a linguistic rendering but a cultural artifact embedded within its historical moment, potentially revealing measurable patterns of what I term "cultural sway" (represented here by evolving stylistic norms and translator’s agency).

#### *Hypothesis*
My hypothesis proposes that Odyssey translations exhibit measurable linguistic shifts over time reflecting evolving stylistic norms and translator agency (H₁), against the null hypothesis (H₀) that lexical, syntactic, and stylistic features remain stable across historical periods. This of course seems common sense, however, identifying and measuring the "cultural sway" means making it intelligeble. Thus cultural sway can create a new (quantitative) dimension of textual analysis. Through systematic examination of lexical diversity, word frequency distributions, content distinctiveness, and etymological preferences, this study seeks to quantify the often-intuited notion of translator "voice" and to identify whether diachronic patterns emerge from the accumulated "music" of retranslation.

The implications extend beyond translation studies. If quantifiable patterns exist, they would suggest that the English Odyssey tradition has developed its own internal dynamics, where later translators respond not only to Homer's Greek but to the accumulating English tradition itself—a phenomenon where the target language begins to function simultaneously as source culture: the target is the new source.

## **2. Data and Methods** 

### **2.1 Corpus Description**

The study corpus comprises seven texts: six English Odyssey translations and one baseline prose work. The translations span exactly one century, from Augustus Taber Murray's 1919 Loeb Classical Library edition (still used as textbook in some Classics departments) to Peter Green's 2018 long expected rendering. The selection criteria prioritized temporal distribution, translation philosophy diversity, and text availability in digital format (see Lexical of 20th century Odyssey translations (Part A): Token Distribution, a.k.a., Lexical A, section II, "The Texts").

Each text was obtained from authoritative digital sources or carefully digitalized by me: Murray from the Perseus Digital Library's Scaife Viewer, Fitzgerald from the Internet Archive, Green from EBSCO (with a digital license from Tübingen Univertsity), and contemporary translations from digital editions and scans (captured from an OCR to text Python script). Woolf's *The Voyage Out* (from Projet Gutenberg) serves as a baseline for contemporary English prose, providing a non-translation literary text against which to measure the distinctive features of translated (epic) discourse.


<img src=".Lexical/lexical_A01_plots/translator_color_mapping-lexical_A01.png" alt="Color Mapping" width="800"/>
Figure 1. Color Mapping of Translators.
Fixed color palette assigned to each translator, ensuring consistent visual identification across all plots and libraries throughout the analysis.

The texts are segmented into 24 books, resulting in 168 analytical units (24 books × 7 texts). Initially, the translators' capitalization and punctuation were retained to preserve stylistic markers. However, all texts were individually preprocessed to address their specific requwerements. NLTK's and custom functions were used to tokenize the texts, and they were then converted to a standardized Pandas dataframe structure with columns for translator, book number, raw text, and tokens. 
This process followed the pipeline:
 »—raw—» clean—» normalize —» DATAFRAME —» EDA
Each step is documented in their discrete notebooks available in Github (5 steps x 7 authors = 35 notebooks).

### **2.2 Computational Methods**
Here I will describe the experiments in the summarizing notebooks `lexical_A02`and `lexical_B01`.
#### **2.2.1 Lexical Diversity Analysis**

Type-Token Ratio (TTR) served as the primary measure of lexical diversity, calculated as:

TTR = (Unique Words / Total Words) × 100

To address TTR's sensitivity to text length, I implemented three complementary approaches. Standard TTR was computed for each book independently. Standardized TTR (STTR) divided texts into 100-token segments, calculating mean TTR across segments. Moving-average TTR employed a 100-token sliding window to capture lexical variation through narrative progression.

A mixed-effects model was fitted using the *statsmodels* library, with translator as a fixed effect and book number as a random effect, accounting for the inherent variation in narrative content across the Odyssey's episodic structure.

#### **2.2.2 Zipf's Law Analysis**

Word frequency distributions were analyzed through *log-log* regression of rank-frequency relationships. For each translator's complete corpus, words were ranked by frequency and plotted on logarithmic scales. Linear regression in log-space yielded slope coefficients, with ideal Zipfian distribution presenting a slope of -1.0.

Bootstrap analysis (1,000 iterations) generated confidence intervals for slope estimates, enabling statistical comparison between translators. The Shapiro-Wilk test assessed distributional normality.

#### **2.2.3 TF-IDF Analysis**

Term Frequency-Inverse Document Frequency identified distinctive vocabulary for each translator. Documents were defined at the book level, with TF-IDF scores calculated using a custom function that calculates TF-IDF scores for a DataFrame with "book_id" and "tokens" columns returning a .copy DataFrame. The top 50 terms per translator were extracted for overlap analysis, visualized through heathmaps and Venn diagrams.

#### **2.2.4 Etymology Tracking**

Etymological analysis employed Gerard de Melo's Etymological Wordnet (2013), containing over 6 million etymological relationships. A custom recursive function traced each word of the Odysseys to its deepest etymological root, with cycle detection preventing infinite recursion. Words were categorized by language origin (Anglo-Saxon, Latin, Middle English, Old Norman, Ancient Greek, etc.).

Figure 2. Etymology Root Proportions (Anglo-Saxon vs. Latin).
Stacked bar chart showing the relative proportions of Anglo-Saxon and Latin word origins in each Odyssey translation. Distributions are normalized by token count per translator. The dashed line marks the Anglo-Saxon/Latin baseline derived from Fagles’ translation for reference.

Etymology distributions were normalized by token count and compared using cosine distance from mean distribution. Special attention was paid to the Anglo-Saxon versus Latin ratio as an indicator of stylistic register.

Figure 3. Etymology Stylistic Divergence (Anglo-Saxon vs. Latin).
Cosine distance of each translator’s Anglo-Saxon/Latin distribution from the mean distribution across all translations. Higher values indicate greater stylistic divergence in register, with respect to the balance between Anglo-Saxon and Latin roots.

### **2.3 Reproducibility**

All analyses were performed in Python 3.11.5 with documented package versions with all the libraries listed in a "environment.yml" file and a "functions" directory with my functions and plot customization parameters. All code repositories from experimentation to final colated notebooks are available at URL: https://github.com/neophilology/English-Homer (300+ files). Raw texts are accessible through their respective digital libraries. Random seeds were fixed at 42 for sampling operations and 1001 for bootstrap procedures.

Statistical significance was assessed at *α = 0.05* with Bonferroni correction for multiple comparisons where applicable.

## **3. Results**

### **3.1 Lexical Diversity Patterns**

#### **3.1.1 Type-Token Ratio Analysis**

Analysis of lexical diversity revealed substantial variation among translators (F-statistic = 18.6346, p < 0.001). Using Murray as a baseline (TTR = 46.796), each translation displayed a distinct lexical profile. Fitzgerald showed the greatest deviation (+7.515), with roughly 16% higher lexical diversity, followed closely by Woolf (+7.265). Wilson and Fagles formed a middle tier, each diverging moderately from the median in statistically similar ways (+4.596 and +4.520), despite their distinctive stylistic approaches and “voices.” Green displayed a smaller increase (+2.976), while Lattimore was the only translator with lower lexical diversity than Murray (-2.635), consistent with his aim of “naturalizing” Homer through a prose-like verse translation (Carolyn Clark, Best American Poetry, 2020).

A mixed-effects model, controlling for book-level variation, confirmed the significance of these differences (all p < 0.001). The relatively high group variance (11.459) suggests that certain sections of the Odyssey—especially Books 9–12, which recount Odysseus’s fantastical tales—tend to display divergent lexical patterns across translations regardless of translator.
Pairwise comparisons with Bonferroni correction identified significant differences between multiple translator pairs. Effect size analysis using Cohen's d revealed large effects (|d| > 0.8) for comparisons involving Woolf with all translators, medium effects (0.5 < |d| < 0.8) for Murray comparisons, and small effects (|d| < 0.2) among the contemporary translator triad of Fagles, Wilson, and Green.

#### **3.1.2 Moving-Average TTR Analysis**

A moving-average TTR with a 100-token window revealed dynamic patterns of lexical variation across the Odyssey’s narrative progression. Unlike static measures, this approach captures the sequential flow of the text, showing how translators adjust their vocabulary density in response to narrative shifts.

Contemporary translators (Wilson, Fagles, Green) display strikingly similar lexical density trajectories across books, suggesting a convergence in modern translation practices. Earlier translators, by contrast, exhibit greater divergence, reflecting more individualized stylistic choices.

Figure 4 provides an overview of all translators across the 24 books. Despite stylistic and temporal differences, nearly all translations remain within the lexical density range established by Woolf, underscoring a shared constraint on lexical diversity.

A more focused comparison of Lattimore, Fagles, Fitzgerald, and Murray highlights distinct stylistic groupings (Figure 5). The poetic translators, Fagles and Fitzgerald, align closely with each other, maintaining consistently higher lexical density. By contrast, the prose-oriented translations of Lattimore (prose-like verse) and Murray (prose) form a parallel pair with lower density. This pairing effect illustrates how even a simple measure like moving-average TTR can capture both translator agency and the stylistic coherence of different translation strategies.

Figure 4. Moving-Average TTR Across 24 Books (All Translators).
Line plot of moving-average TTR (100-token window) for all translations of the Odyssey. Despite differences in style and era, most translators remain within the lexical density range established by Woolf, highlighting broad stylistic convergence across the corpus.
Figure 5. Moving-Average TTR Comparison of Selected Translators.
Lexical diversity trajectories for Lattimore, Fagles, Fitzgerald, and Murray across the 24 books. The poetic translators (Fagles, Fitzgerald) cluster closely together with higher lexical density, while the prose-oriented translators (Lattimore, Murray) track each other at lower levels, illustrating how moving-average TTR reveals both stylistic agency and translator consistency.



### **3.2 Word Frequency Distributions**

#### **3.2.1 Zipf's Law Adherence**

All translations demonstrated strong adherence to Zipf's Law with remarkably high fit quality (R² ≈ 0.98 for all translators). Log-log regression slopes ranged from -0.865 (Fitzgerald) to -0.997 (Lattimore), with ideal Zipfian distribution at -1.0.

Figure 6. Zipf’s Law Across Translators.
Log-log plot of word frequency versus rank for each Odyssey translation. All translators closely follow Zipf’s Law (R² ≈ 0.98), though with slight individual trajectories. Regression slopes range from -0.865 (Fitzgerald) to -0.997 (Lattimore), with the ideal Zipfian distribution corresponding to -1.0.

Bootstrap analysis (1,000 iterations) generated 95% confidence intervals revealing overlapping ranges for most translators. Fitzgerald showed the shallowest slope (95% CI: -1.1289, -1.1016), suggesting slightly weaker Zipfian adherence, while Lattimore's slope most closely approximated the theoretical ideal (95% CI: -1.2633, -1.2255).

Despite only marginal variation in individual slope values, a one-way ANOVA detected statistically significant differences among translators (F = inf, p = ~0). These results confirm that all translations adhere closely to the expected Zipfian distribution, maintaining a natural linguistic flow.

Figure 7. Comparison of Zipfian Slopes Across Translators.
Scatterplot of log-log regression slopes for each translator, estimated per book of the Odyssey. Fagles, Green, and Wilson cluster closely together, reflecting parallel Zipfian patterns, while Lattimore and Fitzgerald exhibit the greatest divergence, marking the extremes of translation style within the corpus.

### **3.3 Content Distinctiveness**

TF-IDF analysis identified both shared core vocabulary and translator-specific lexical choices. Across all translations, 37 terms emerged as consistently important, forming a stable semantic core of the Odyssey in English. Individual translators demonstrated 8-15 unique high-importance terms not prominent in other translations.

Overlap analysis revealed clustering patterns: Wilson-Fagles demonstrated the highest term overlap (73%), while Murray-Wilson showed the lowest (41%). The contemporary translator triad (Wilson, Fagles, Green) shared 62% of their top terms, suggesting convergent approaches to key concept representation.

Figure 8. Venn Diagram of Top 50 TF-IDF Terms for Wilson, Fagles, and Green.
The overlap highlights both a shared semantic core and translator-specific lexical emphases. Wilson and Fagles exhibit the highest overlap (73%), while Murray and Wilson share the least (41%). The contemporary translators (Wilson, Fagles, Green) collectively share 62% of their top terms, indicating convergent strategies in rendering key concepts of the Odyssey.

### **3.4 Etymological Preferences**

#### **3.4.1 Etymology Distribution Analysis**

Etymology tracking successfully assigned roots to 97.69% of unique tokens, with 2.31% resulting in circular references. The dominant etymological categories across all translations were English (eng), Middle English (enm), Anglo-Saxon (ang), and Latin (lat), collectively accounting for over 85% of traced roots.

When filtering for non-English roots to examine deeper etymological preferences, significant variation emerged. The Anglo-Saxon to Latin ratio revealed distinct stylistic registers: Wilson demonstrated the strongest Anglo-Saxon preference (see Figure 9), while Fagles showed the highest Latin usage among translators (23% of filtered roots).

Figure 9. Etymology Proportions by Translator.
Stacked bar chart showing the relative contributions of Anglo-Saxon, Latin, Middle English, and other etymological categories across translations. Filtering for non-English roots highlights stylistic differences: Wilson exhibits the strongest Anglo-Saxon preference, whereas Fagles relies most heavily on Latin, reflecting distinct lexical registers among translators.

#### **3.4.2 Etymology-Based Clustering**

Cosine distance from the mean etymological distribution highlights stylistic divergence among translators. Woolf is the most distinctive, with a distance of 0.01745, followed by Wilson (0.00121). Lattimore (0.00072) and Green (0.00061) form a moderately aligned pair, while Fitzgerald (0.00044) and Fagles (0.00006) are closest to the mean distribution, indicating high conformity with the overall etymological pattern. Murray (0.00035) also lies near the mean, slightly farther than Fagles but closer than Lattimore or Green.

PCA of etymology-weighted TF-IDF scores revealed three distinct clusters:
- **Cluster 1**: Fitzgerald, Fagles, Wilson, Murray (main group)
- **Cluster 2**: Lattimore, Green (outlier pair)
- **Cluster 3**: Woolf (isolated baseline)

Figure 10. PCA of Etymology-Weighted TF-IDF Scores Across Translators.
Scatterplot of principal components derived from etymology-weighted TF-IDF scores, illustrating stylistic divergence among translators. Woolf is the most distinctive (cosine distance = 0.01745), followed by Wilson (0.00121). Lattimore and Green form a moderately aligned pair, while Fitzgerald and Fagles remain closest to the mean distribution. Murray also lies near the mean, slightly farther than Fagles, highlighting both convergence and variation in etymological patterns across translations.

## **4. Discussion**

### **4.1 Translator Agency Within Cultural Constraints**

The results provide compelling evidence for measurable translator agency operating within linguistic and cultural constraints. The significant variation in lexical diversity (ranging from Lattimore's -2.635 to Fitzgerald's +7.515 relative to Murray) cannot be attributed to random variation or temporal factors alone. Lattimore and Fitzgerald both wrote in the 1960’s, which dismisses a dominant historical sway. Instead, these differences reflect conscious stylistic choices—and translators reacting to other translator’s version—that persist throughout each translator's work, as evidenced by the consistency in moving-average TTR patterns.

The mixed-effects model's revelation of substantial book-level variance (11.459) while maintaining translator-specific effects suggests that translators respond differently to narrative demands. Books 9-12, containing Odysseus's tales of monsters (Polyphemus, Scylla, Lestregones) and magic (Circe, Calypso, Hermes), elicit greater lexical variation across all translations, yet each translator's distinctive approach remains identifiable. This finding supports Robinson's (2016) concept of translation as "negotiated space," where individual agency operates within structural constraints.

Etymology analysis provides perhaps the most revealing window into unconscious translator preferences. Wilson's Anglo-Saxon preference aligns with her stated goal of "contemporary clarity," suggesting that accessibility drives not just vocabulary choice but deeper linguistic register. Conversely, Fagles's higher Latin usage, despite critical praise for his "rapidity" and correspondence to Homer's style, reveals how classical register can paradoxically serve modernizing aims.

### **4.2 Challenging the Diachronic Hypothesis**

The study's most surprising finding is the absence of clear chronological progression across the century-long span. The hypothesis of measurable diachronic shifts (H₁) receives only partial support. While significant variations exist among translations, these variations cluster by translator philosophy rather than temporal period. For example, Murray and Wilson’s translations were written 100 years apart, and showed the lowest overlapping TF-IDF top terms, but still share 41% and the trend does not continue with Green, conteporary to Wilson’s version. Evenmore, the three-way clustering of contemporary translators (Wilson, Fagles, Green) in TF-IDF overlap and moving-average TTR might initially suggest temporal influence. However, etymology analysis disrupts this pattern: Wilson diverges significantly from her contemporaries in Anglo-Saxon preference, while Fagles aligns more closely with earlier translators in Latin usage. This suggests that individual translator agenda—whether feminist revisioning (Wilson), musical recreation (Fagles), or philological precision (Green)—exerts stronger influence than temporal literary norms.

The universal adherence to Zipf's Law across all translations, with no significant slope differences despite individual variations, indicates that certain fundamental linguistic patterns transcend both time and translator preference. This finding suggests that the constraints of natural English expression may be more powerful than either cultural evolution or individual style.

### **4.3 Evidence for an English Odyssey Network**

The 41-73% range in TF-IDF term overlap between translator pairs provides quantitative support for the proposed "English Odyssey network." The consistently higher overlap among contemporary translators (62% shared terms) versus cross-temporal pairs suggests that recent translators engage not only with Homer's Greek but with the accumulated English tradition.

The identification of 37 core terms shared across all translations indicates the emergence of a stable English Odyssey vocabulary—lexical items that have become essential to the epic's expression in English regardless of translation philosophy. This finding supports Lefevere's (1992) notion of translation as "transformative rewriting" that shapes canon formation, here manifesting as a crystallized semantic core.

### **4.4 Methodological Insights and Limitations**

The multi-method approach proved essential for capturing different dimensions of translator variation. While TTR effectively measured surface lexical diversity, etymology analysis revealed deeper, potentially unconscious linguistic preferences. The complementary nature of these findings—surface diversity not predicting etymological preference—highlights the complexity of translation style.

Several limitations constrain interpretation. The 2.31% circular reference rate in etymology tracking, while acceptable, may introduce systematic bias if certain word types are disproportionately affected. The choice of Woolf as a prose baseline, while providing valuable contrast, cannot fully represent contemporary non-translated English literature. Most significantly, the sample of six translations, though spanning a century, cannot capture the full complexity of the 80+ English Odysseys.

The unexpected clustering of Lattimore and Green, separated by five decades yet showing similar etymological profiles and lexical patterns, raises questions about whether certain translation approaches recur cyclically rather than evolving linearly. This finding warrants expansion to the full corpus of English Odysseys.

5. Conclusions
5.1 Key Findings
This computational analysis reveals three primary insights. First, translator agency operates through measurable linguistic dimensions—lexical diversity ranges from Lattimore's -2.635 to  Fitzgerald's +7.515 relative to Murray's baseline, while etymological preferences diverge significantly from mean distributions (see Lexical B, cells 34-5). Second, translations cluster by philosophical approach/translator’s agenda rather than temporal period: Wilson-Fagles-Green form a contemporary triad in TF-IDF overlap (62-73%) yet diverge radically in etymology. Third, unconscious cultural positioning manifests through etymological substrate—Wilson's Anglo-Saxon preference aligns with stated accessibility goals, while Fagles's Latinate tendency brings a new color to the critical reception praising his "clear simplicity, luminous and unsentimental" style (Richard Jenkyns, "Heroic Enterprise").

This project, as a proof of concept, successfully demonstrates that statistical lexical analysis and distant etymological readings can capture, albeit slightly, significant differences in translations that aid in classification and understanding how the target language creates a visible pattern through data science. This result encourages expanding the scope, experimenting with new methods, and utilizing a larger sample. Only through a substantial corpus will diachronic or cyclic patterns be revealed or dismissed statistically. However, once these patterns are established, a comprehensive model of 400 years of Odyssey translations in English will emerge.
5.2 Answering Research Questions
Variation emerges primarily through lexical selection rather than syntactic architecture—all translations maintain Zipfian distributions (R² ≈ 0.98) despite individual stylistic differences. Translator agency proves strongest in etymological preference and vocabulary richness, operating within constraints of natural English expression. The mixed-effects model successfully captures individual innovation while accounting for book-level narrative variance (group variance 11.459). Crucially, the hypothesized diachronic progression finds no support—translator philosophy trumps chronology.
5.3 Future Directions
Expanding to the complete 80+ translation corpus would test whether these patterns hold across the full English Homer tradition, including the recent translation by Mendelsohn (2025). Syntactic complexity measures—parse tree depth, clause embedding—could reveal structural variation invisible to lexical analysis. Developing algorithmic "fingerprints" combining multiple metrics might enable automatic translator identification, validating my agency measurements.
A new question emerges from the rejection of h1, if there is no clear diachronic sway, does that mean that the Odyssey is treated as an atemporal text, as a text that is referencing lexically a time out of the narrator’s present? and what role archaism play in this?
kt