# Project Journal

This is a learning log. The entries are insights into the process, lessons and mistakes.

I'll try to keep some keywords in each log to identify the area of each entry:
- #file_management
- #eda
- #nlp
- #writing
- #stats
- #viz
- #workflow
- #documentation
- #model_training
- #evaluation
- #data_cleaning
- #preprocessing
- #deployment
- #ethics

## March 8

### Text Normalization Strategy #data_cleaning #nlp #file_management
Managed to clean Wilson and Green's translations but found out that I may need to do a new folder with "normalizers", in which all that is left is text:
- Only English characters
- Eliminate line numbering and books' indicators
- Delete footnotes numbers
- lower case

### Normalization Decision Log #workflow #documentation
Decision to create separate normalization scripts rather than embedding normalization in the main processing pipeline. This will allow for:
- Better version control of normalization strategies
- Ability to easily compare results with different normalization approaches
- Cleaner codebase with separation of concerns

### Text Cleaning Considerations #nlp #preprocessing
Important considerations for future text normalization steps:
- Keep original files intact and create new versions to preserve source material
- Document each transformation with examples (before/after)
- Consider how normalization might affect certain analyses (e.g., lowercasing removes named entity information)
- Create a reversible process where possible to trace processing decisions

### Next Steps #workflow
- [ ] Create a normalization config file to track parameters
- [ ] Build evaluation metrics to assess normalization quality
- [ ] Consider how to handle edge cases (e.g., hyphenated words, contractions)
- [ ] Test normalization on a small sample before applying to full corpus

## Best Practices for NLP Projects

### Data Management #file_management #documentation
- Use consistent file naming conventions (e.g., `{source}_{date}_{version}.txt`)
- Maintain a data registry documenting source, version, and modifications
- Create checkpoints after significant transformations
- Store raw data separately and never modify it directly

### Preprocessing Pipeline #nlp #workflow
- Build modular preprocessing steps that can be run independently
- Log preprocessing decisions and parameters
- Consider creating a preprocessing report with statistics before/after each step
- Test preprocessing on small samples before running on full dataset

### EDA Best Practices #eda #viz
- Start with basic corpus statistics (token counts, vocabulary size, etc.)
- Visualize token distributions across documents
- Look for anomalies in the data early (outlier documents, unexpected patterns)
- Save EDA outputs in a dedicated folder with descriptive names

### Model Development #model_training #evaluation
- Start simple and establish baselines before complex models
- Document hyperparameters and random seeds
- Track evaluation metrics across experiments
- Consider both quantitative metrics and qualitative analysis

### Philological Considerations #nlp #ethics
- Be mindful of linguistic and cultural context when interpreting results
- Document assumptions about language and text that inform your analysis
- Consider how computational methods might misrepresent nuanced textual features
- Complement computational analysis with traditional close reading where appropriate