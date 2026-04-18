# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Character Frequency - Count and analyze character frequencies
# Difficulty: Easy | Frequency: ⭐⭐⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: STRING & CHARACTER PROCESSING                          ║
# ║  PURPOSE: Count character frequency in strings                    ║
# ║  FEATURES: Filters characters appearing > once, alphabetic sort   ║
# ╚═══════════════════════════════════════════════════════════════╝


"""
    1. Character Frequency (Enhanced)

    Given a string, return a dictionary containing:

    frequency of each character

    but only for characters that appear more than once

    keys must be sorted alphabetically

    Example
    Input: "programming"
    Output: {'g': 2, 'm': 2, 'r': 2}

"""

""" 

    Output

    from collections import Counter
    example_string = "programming"
    string_frequency = Counter(example_string)

    result = {}
    result = {key: value for key, value in string_frequency.items() if value>1}
    sorted_dict = dict(sorted(result.items(),key = lambda x:x[0]))
    print(f"Here's final sorted result {sorted_dict}")

"""

"""
Question 2

Given a list of strings, group the strings that are anagrams of each other using a dictionary.

Example
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:

{
  "aet": ["eat", "tea", "ate"],
  "ant": ["tan", "nat"],
  "abt": ["bat"]
}

"""

"""
Approach !
result = {}
example_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
for word in example_list:
    sorted_word = "".join(sorted(word))
    if sorted_word in result:
        temp_list = result[sorted_word]
        temp_list.append(word)
        result[sorted_word] = temp_list
    else:
        result[sorted_word] =[word]


print(f"Here's analgram word {result}")

"""

"""
    Appraoch 2:

    from collections import defaultdict

    result = defaultdict(list)
    example_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for word in example_list:
        sorted_word = "".join(sorted(word))
        result[sorted_word].append(word)

    print(result)
"""


"""
    Most Common Word (Case-insensitive)

    Given a paragraph string, return the most frequent word, ignoring:

    punctuation

    case

    words shorter than 3 characters

"""

import re
from collections import Counter

sample_paragraph = "ram went to the market. The market was huge and the food was amazing."

cleaned = re.sub(r"[^a-zA-Z\s]", "", sample_paragraph)
words = cleaned.split()
filtered_words = [word.lower() for word in words if len(word) > 2]
frequency = Counter(filtered_words)
most_common = frequency.most_common(1)[0][0]

print("Filtered Words:", filtered_words)
print("Frequency:", frequency)
print("Most Common Word:", most_common)

import re

text = "My number is 9876543210"

match = re.search(r"\d+", text)
print(match)  # Output: 9876543210
print(match.group())  # Output: 9876543210







