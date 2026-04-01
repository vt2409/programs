# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Company: [COMPANY_NAME]
# Problem: First Non-Repeating Character - Find and index first unique char
# Difficulty: Easy | Frequency: ⭐⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: STRING & CHARACTER PROCESSING                          ║
# ║  PURPOSE: Character occurrence analysis and substring operations  ║
# ║  INCLUDES: Non-repeating char, longest substring, frequency count ║
# ╚═══════════════════════════════════════════════════════════════╝

# Character Frequency - Count occurrence of each character
# Input: example_string = "tomavikvikastomar"
# Output: dict = {'a':5, 'b':4, ...}

"""
Here's the programming question!
Input: example_string = "tomavikvikastomar"
Output dict = {'a':5,b:4}
"""



def count_frequency(example_string):
    result = {}
    for char in example_string:
        result[char] = result.get(char,0) + 1
    return result

example_string = "aabcc"
print(f"Here's the output of character frequency {count_frequency(example_string)}")

