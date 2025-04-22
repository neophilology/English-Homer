# Results log

Here are the results of the final project data science for linguist analyzing Odysseys of the 20th and 21st Century, i.e., translations of Homer's Odyssey to English by Augustus Taber Murray, Robert Fitzgerald, Richmond Latimore, Robert Fagles, Emily Wilson, and Peter Green. For baseline I'm using Virginia Woolf's *The Voyage Out*. 


## Lexical comparisons and metrics

The results on this section belong to the lexical_A02.ipynb notebook. This is the part one of the project, dealing with TTR, Zipf's Law, and TF-IDF analysis of the Odysseys.

### Verbosity/conciseness based on normalized difference of number of words vs. tokens

Most verbose translator (relative): AT_Murray (56.81%)
Most concise translator (relative): Fagles (50.48%)

### Token-word ratio per translator

Baseline translator: Woolf with a ratio of 0.46
translator
AT_Murray    0.43
Fagles       0.50
Fitzgerald   0.49
Green        0.47
Lattimore    0.44
Wilson       0.49
Woolf        0.46

### TTR: Shapiro-Wilks for Normality distribution

All the Odysseys are NORMALLY distributed. In contrast, Woolf's novel is NOT normally distributed.

Shapiro-Wilk test for 
AT_Murray's data: T-statistic=0.9797, p-value=0.8908
AT_Murray's TTR data is NORMALLY distributed.

Shapiro-Wilk test for 
Fitzgerald's data: T-statistic=0.9861, p-value=0.9769
Fitzgerald's TTR data is NORMALLY distributed.

Shapiro-Wilk test for 
Lattimore's data: T-statistic=0.9664, p-value=0.5792
Lattimore's TTR data is NORMALLY distributed.

Shapiro-Wilk test for 
Fagles's data: T-statistic=0.9492, p-value=0.2606
Fagles's TTR data is NORMALLY distributed.

Shapiro-Wilk test for 
Wilson's data: T-statistic=0.9715, p-value=0.7034
Wilson's TTR data is NORMALLY distributed.

Shapiro-Wilk test for 
Green's data: T-statistic=0.9645, p-value=0.5361
Green's TTR data is NORMALLY distributed.

Shapiro-Wilk test for 
Woolf's data: T-statistic=0.8847, p-value=0.0103
Woolf's TTR data is NOT normally distributed.

### TTR: One-way ANOVA

There are statistically **significant differences in TTR** among the translators.
F-statistic: 18.6346, P-value: 0.0000


### TTR: Pairwise t-tests with Bonferroni correction

**Where the difference is SIGNIFICANT:**

AT_Murray vs Fitzgerald: Diff = -7.5148, p = 0.0000 - SIGNIFICANT
AT_Murray vs Fagles: Diff = -4.5204, p = 0.0007 - SIGNIFICANT
AT_Murray vs Wilson: Diff = -4.5955, p = 0.0003 - SIGNIFICANT
AT_Murray vs Woolf: Diff = -7.2653, p = 0.0010 - SIGNIFICANT
Fitzgerald vs Lattimore: Diff = 10.1503, p = 0.0000 - SIGNIFICANT
Fitzgerald vs Green: Diff = 4.5391, p = 0.0014 - SIGNIFICANT
Lattimore vs Fagles: Diff = -7.1559, p = 0.0000 - SIGNIFICANT
Lattimore vs Wilson: Diff = -7.2310, p = 0.0000 - SIGNIFICANT
Lattimore vs Green: Diff = -5.6112, p = 0.0000 - SIGNIFICANT
Lattimore vs Woolf: Diff = -9.9008, p = 0.0000 - SIGNIFICANT

**Where the difference is NOT significant:**
AT_Murray vs Lattimore: Diff = 2.6355, p = 0.2486 - NOT significant
AT_Murray vs Green: Diff = -2.9757, p = 0.0865 - NOT significant
Fitzgerald vs Fagles: Diff = 2.9944, p = 0.1204 - NOT significant
Fitzgerald vs Wilson: Diff = 2.9193, p = 0.1190 - NOT significant
Fitzgerald vs Woolf: Diff = 0.2495, p = 1.0000 - NOT significant
Fagles vs Wilson: Diff = -0.0751, p = 1.0000 - NOT significant
Fagles vs Green: Diff = 1.5447, p = 1.0000 - NOT significant
Fagles vs Woolf: Diff = -2.7449, p = 1.0000 - NOT significant
Wilson vs Green: Diff = 1.6198, p = 1.0000 - NOT significant
Wilson vs Woolf: Diff = -2.6698, p = 1.0000 - NOT significant
Green vs Woolf: Diff = -4.2896, p = 0.2428 - NOT significant