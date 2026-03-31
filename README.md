# Python Programs - Categorized Overview

## 📋 Project Structure and Categories

This workspace contains Python programs organized into **5 category-based folders**:

```
📦 program/
├── 📁 1_STRING_CHARACTER_PROCESSING/
│   ├── 01_anagram_grouping_program.py
│   ├── 02_character_frequency_program.py
│   ├── 03_occurrence_character_program.py
│   ├── 04_max_repeating_substring_program.py
│   └── 05_string_analysis_program.py
├── 📁 2_TEXT_ANALYSIS/
│   ├── 01_basic_string_algorithms_program.py
│   └── 02_most_frequent_words_program.py
├── 📁 3_DATA_STRUCTURES/
│   ├── 01_collections_demo_program.py
│   └── 02_employee_salary_program.py
├── 📁 4_ADVANCED_CONCEPTS/
│   ├── 01_decorator_example_program.py
│   └── 02_regular_expression_program.py
├── 📁 5_NLP/
│   ├── 01_spacy_nlp_program.py
│   └── 02_word2vec_embeddings_program.py
└── README.md (this file)
```

---

## 1️⃣ STRING & CHARACTER PROCESSING
**Folder:** `1_STRING_CHARACTER_PROCESSING/`
### Focus: Analyzing and manipulating strings and characters

#### **01_anagram_grouping_program.py**
- **Purpose**: Groups words that are anagrams of each other
- **Key Features**:
  - Uses sorting to find anagram patterns
  - Demonstrates `defaultdict` for efficient grouping
  - Includes dictionary sorting techniques
- **Example**: Groups ["listen", "silent", "enlist"] together based on sorted characters

#### **02_character_frequency_program.py**
- **Purpose**: Counts frequency of each character in a string
- **Use Case**: Character analysis with filtering
- **Key Features**:
  - Returns dictionary with character frequencies
  - Can filter characters appearing more than once
  - Sorts results alphabetically
- **Example**: "programming" → {'g': 2, 'm': 2, 'r': 2}

#### **03_occurrence_character_program.py**
- **Purpose**: Multiple string operations on characters
- **Key Algorithms**:
  - Find first non-repeating character
  - Find index of first non-repeating character
  - Find longest substring without repeating characters
- **Uses**: Counter from collections module for efficiency

#### **04_max_repeating_substring_program.py**
- **Purpose**: Finds maximum repeating substrings in a string
- **Algorithm**: Brute force substring generation and counting
- **Returns**: List of substrings with max frequency and the count
- **Example**: "abab" → Most repeating patterns and their counts

#### **05_string_analysis_program.py**
- **Purpose**: Multiple string and character analysis algorithms
- **Algorithms Included**:
  1. First non-repeating character detection
  2. Find index of first non-repeating character
  3. Find longest substring without repeating characters
- **Type**: Comprehensive string analysis with helper functions
- **Uses**: Counter from collections for efficient frequency counting

---

## 2️⃣ TEXT ANALYSIS & WORD PROCESSING
**Folder:** `2_TEXT_ANALYSIS/`
### Focus: Processing words and text content

#### **01_basic_string_algorithms_program.py**
- **Purpose**: Collection of fundamental string algorithms
- **Algorithms Included**:
  1. First non-repeating character detection
  2. Palindrome checker (case and space insensitive)
  3. Nested list flattening
- **Type**: Educational examples for string manipulation

#### **02_most_frequent_words_program.py**
- **Purpose**: Extracts and ranks most frequent words from reviews
- **Features**:
  - Removes punctuation using regex
  - Filters common stop words (is, the, a, an, etc.)
  - Sorts by frequency (descending) then alphabetically
  - Returns top K most frequent words
- **Use Case**: Sentiment analysis, content analysis

---

## 3️⃣ DATA STRUCTURES & COLLECTIONS
**Folder:** `3_DATA_STRUCTURES/`
### Focus: Advanced Python data structure usage

#### **01_collections_demo_program.py**
- **Purpose**: Demonstrates Python Collections module features
- **Topics Covered**:
  - `Counter`: Frequency counting with sorting capabilities
  - `defaultdict`: Automatic default values for missing keys
  - Dictionary sorting (by key and by value)
- **Key Benefit**: High-performance alternatives to basic data structures
- **Use Case**: Efficient frequency analysis and grouping

#### **02_employee_salary_program.py**
- **Purpose**: Employee data filtering and sorting operations
- **Features**:
  - Filters employees by salary threshold
  - Sorts results by salary in descending order
  - Works with list of dictionaries
- **Type**: Real-world data manipulation example

---

## 4️⃣ ADVANCED PYTHON CONCEPTS
**Folder:** `4_ADVANCED_CONCEPTS/`
### Focus: Design patterns and advanced features

#### **01_decorator_example_program.py**
- **Purpose**: Demonstrates Python decorators
- **Patterns Shown**:
  - Decorators with parameters
  - Decorators without parameters
  - Decorators that modify function behavior
- **Use Case**: Function wrapping, logging, request processing
- **Example**: Decorator that adds "decorated" flag to request body

#### **02_regular_expression_program.py**
- **Purpose**: Regular expression pattern matching in Python
- **Features**:
  - Word boundary matching (\b)
  - Word extraction from text
  - Substitution and pattern filtering
- **Module Used**: `re` module
- **Use Case**: Text parsing, validation, data extraction

---

## 5️⃣ NATURAL LANGUAGE PROCESSING (NLP)
**Folder:** `5_NLP/`
### Focus: Advanced text analysis using NLP libraries

#### **01_spacy_nlp_program.py**
- **Purpose**: Natural Language Processing using spaCy library
- **Capabilities**:
  - Named Entity Recognition (NER)
  - Noun phrase extraction
  - Part-of-speech (POS) tagging
  - Verb extraction with lemmatization
  - Vector representations
- **Model Used**: en_core_web_sm (English model)
- **Requires**: `pip install spacy` and model download

#### **02_word2vec_embeddings_program.py**
- **Purpose**: Word embeddings using Google's pretrained Word2Vec model
- **Features**:
  - Loads pretrained Word2Vec vectors (300-dimensions)
  - Finds semantically similar words
  - Similarity scoring between words
- **Library**: gensim (Google News 300-dimensional model)
- **Use Case**: Word similarity, semantic analysis, embedding-based tasks
- **Note**: ~1.5GB download required (one-time)

---

## 📊 Quick Reference

| Category | Folder | Files | Purpose |
|----------|--------|-------|---------|
| String Processing | `1_STRING_CHARACTER_PROCESSING/` | 01_anagram_grouping_program.py, 02_character_frequency_program.py, 03_occurrence_character_program.py, 04_max_repeating_substring_program.py, 05_string_analysis_program.py | Character/string analysis |
| Text Analysis | `2_TEXT_ANALYSIS/` | 01_basic_string_algorithms_program.py, 02_most_frequent_words_program.py | Word extraction and processing |
| Data Structures | `3_DATA_STRUCTURES/` | 01_collections_demo_program.py, 02_employee_salary_program.py | Advanced data structure usage |
| Advanced Concepts | `4_ADVANCED_CONCEPTS/` | 01_decorator_example_program.py, 02_regular_expression_program.py | Python design patterns |
| NLP | `5_NLP/` | 01_spacy_nlp_program.py, 02_word2vec_embeddings_program.py | Natural language processing |

---

## 🔧 Dependencies Required

### Basic (No additional install):
- `collections` (standard library)
- `re` (standard library)

### For NLP:
```bash
pip install spacy
pip install gensim
python -m spacy download en_core_web_sm
```

---

## 💡 Learning Path Recommendation

1. **Start here**: 01_basic_string_algorithms_program.py, 02_character_frequency_program.py
2. **Then**: 01_collections_demo_program.py, 02_most_frequent_words_program.py
3. **Next**: 01_anagram_grouping_program.py, 03_occurrence_character_program.py
4. **Advanced**: 01_decorator_example_program.py, 02_regular_expression_program.py
5. **Expert**: 01_spacy_nlp_program.py, 02_word2vec_embeddings_program.py

---
