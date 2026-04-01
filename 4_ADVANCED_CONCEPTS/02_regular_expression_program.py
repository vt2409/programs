# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Company: [COMPANY_NAME]
# Problem: Regular Expressions - Pattern matching and text manipulation
# Difficulty: Medium | Frequency: ⭐⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: ADVANCED PYTHON CONCEPTS                               ║
# ║  PURPOSE: Regular expression pattern matching and manipulation    ║
# ║  FEATURES: Word boundaries, word extraction, text substitution    ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
Here's regular expression in python. Regular expressions are a powerful tool for matching patterns in strings. They allow you to search, match, and manipulate strings based on specific patterns.
In Python, the `re` module provides functions for working with regular expressions. Here are some common functions and their usage:


"""

"word Boundardies: \b"
import re

# Example: Finding all words in a string
text = "Hello, world! This is a regular expression example."
# words = re.findall(r'\b\w+\b', text)

words = re.findall(r"\b\w+\b", text)
print(words)  # Output: ['Hello', 'world', 'This', 'is',

# words = re.sub(r"[^a-zA-Z\s]", "", text
#                )
# print(words.split())  # Output: Hello world This is a regular expression example
