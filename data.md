# Data

## The Corpus
* **What**: Complete English translations of the Odyssey in txt format
* **Scope**: 15+ major translations spanning from 1615 (Chapman) to 2018 (Green)
* **Format**: UTF-8 encoded plain text files with consistent formatting
* **Processing**:
  - Cleaned of paratextual elements (introductions, notes, appendices)
  - Structurally normalized (book divisions, line breaks, paragraphs)
  - Semi-tagged using lightweight XML for character identifications, speeches, and epithets
  - Annotated with book/chapter markers for cross-translation alignment

## English Literature and Translations
* **What**: Comprehensive dataset of Homeric reception in English literature and translations
* **Structure**: CSV with metadata on each work
* **Data fields**:
  - `title`: string - Full title of the work
  - `author`: string - Translator or author name
  - `year`: integer - Publication year
  - `period`: string - Literary period (Renaissance, Victorian, Modern, etc.)
  - `span`: string - Complete/Partial translation or adaptation
  - `verse`: boolean - Whether in verse (true) or prose (false)
  - `publisher`: string - Publishing house
  - `edition`: string - Edition information
  - `source`: string - Greek source text used (if specified)
  - `language`: string - Original language of composition
  - `country`: string - Country of publication
  - `reception`: string - Brief classification of reception type (scholarly, popular, experimental)
  - `gender`: string - Translator/author gender
  - `academic`: boolean - Academic or non-academic background
  - `influence_score`: float - Metric of cultural influence (citations, reprints)

## Translations at a Glance
* **What**: Comparative metrics and key textual features across translations
* **Format**: CSV/JSON for structured comparison
* **Features**:
  - `title`: string - Translation title
  - `author`: string - Translator name
  - `year`: integer - Publication year
  - `first_lines_book_I` ... `first_lines_book_XXIV`: string - Opening lines of each book
  - Epithets by character (`epithet_Odysseus`, `epithet_Penelope`, etc.): dictionary - All epithets with frequencies
  - `num_lines`: integer - Total line count
  - `num_words`: integer - Total word count
  - `avg_sentence_length`: float - Average sentence length
  - `lexical_diversity`: float - Type-token ratio
  - `named_entities`: dictionary - Character name variants with frequencies
  - `speech_ratio`: float - Percentage of text in direct speech
  - `modernization_index`: float - Computed metric of contemporary language use
  - `network_density`: float - Density measure of character interaction network
  - `character_centrality`: dictionary - Eigenvector centrality scores for main characters

## Character Networks
* **What**: Extracted interaction data between characters
* **Format**: Edge list and node attributes in CSV/GEXF format
* **Features**:
  - `nodes`: Character identifiers with attributes (gender, mortality, divinity)
  - `edges`: Interactions between characters
  - `weight`: Frequency/intensity of interactions
  - `type`: Nature of relationship (familial, antagonistic, supportive)
  - `book`: Book number where interaction occurs
  - `initiator`: Which character initiates interaction

## Translation Computational Metrics
* **What**: Stylometric and linguistic analysis data
* **Format**: JSON with nested metrics
* **Features**:
  - Readability scores (Flesch-Kincaid, SMOG)
  - POS distribution
  - Sentiment analysis by book and character
  - Archaic language markers
  - Topic modeling results
  - Word embeddings for key concepts (nostos, xenia, etc.)