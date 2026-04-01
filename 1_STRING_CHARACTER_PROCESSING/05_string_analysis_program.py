# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Company: [COMPANY_NAME]
# Problem: String Analysis - Multiple character/string algorithms
# Difficulty: Easy | Frequency: ⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: STRING & CHARACTER PROCESSING                          ║
# ║  PURPOSE: Multiple character/string analysis algorithms           ║
# ║  INCLUDES: Non-repeating char, char index, longest substring      ║
# ╚═══════════════════════════════════════════════════════════════╝

"Find First Non-Repeating character!"

example_string = "aabbcdd"
from collections import Counter
def find_non_repeating_character(s):
    char_count = Counter(s)
    for char in s:
        if char_count[char] == 1:
            return char
    return None
result = find_non_repeating_character(example_string)
print(f"The first non-repeating character in '{example_string}' is: {result}")

"""
I'll use a hash map to count frequency of each character, then iterate through the string again to find the first character with count 1.
"""


def find_non_repeating_character_index(s):
    char_count = Counter(s)
    for index,char in enumerate(s):
        if char_count[char] ==1:
            return index 
    return None
result_index = find_non_repeating_character_index(example_string)   
print(f"The index of the first non-repeating character in '{example_string}' is: {result_index}")

"""
Explaination: I'll use the hashmap to count the frequency of each character, then iterate through the string again to find the index using enumerate that will return index number of string character.
"""

"""
Find the longest substring without repeating characters!


"""
string = "abcabcbb"
original_string = ""
for i in range(len(string)):
    temp_set = set()
    current_string = ""
    
    for j in range(i,len(string)):
        if string[j] in temp_set:
            break
        
        temp_set.add(string[j])
        current_string += (string[j])
        if len(current_string) > len(original_string):
            original_string = current_string
print(original_string)