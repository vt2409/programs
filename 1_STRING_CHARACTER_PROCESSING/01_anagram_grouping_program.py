# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Group Anagrams - Classify words that are anagrams of each other
# Difficulty: Medium | Frequency: ⭐⭐⭐⭐
# ═══════════════════════════════════════════════════════════════
#
# TIME COMPLEXITY: O(n * k log k) - n words, k avg word length, sorting each word
# SPACE COMPLEXITY: O(n * k) - Storing n words with avg length k
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: STRING & CHARACTER PROCESSING                          ║
# ║  PURPOSE: Group anagrams together                                 ║
# ║  ALGORITHM: Sort characters in each word to find anagram patterns ║
# ╚═══════════════════════════════════════════════════════════════╝

words = ["listen", "silent", "enlist", "rat", "tar", "art", "hello", "world"]
Excepted_output = {
    "eilnst": ["listen", "silent", "enlist"],
    "art": ["rat", "tar", "art"],
    "ehllo": ["hello"],
    "dlorw": ["world"]
}

"""
Here's common approach of solutions:
"""
result = {}
for word in words:
    sort_word = "".join(sorted(word,reverse=False))
    if sort_word in result:
        temp = result[sort_word]
        temp.append(word)
        result[sort_word]=temp
    else:
        result[sort_word]=[word]

for key, value in result.items():
    print(f"{key}: {value}")


"""
Here's most efficient approach solution
"""
from collections import defaultdict
result = defaultdict(list)

for word in words:
    key = "".join(sorted(word))
    result[key].append(word)

for key, value in result.items():
    print(f"{key}: {value}")


"""
Sort the dict
"""

sorted_dict = dict(sorted(result.items(),reverse=False))
sorted_dict1= dict(sorted(result.items(), key=lambda x: x[0]))
print(f"Here's sorted dict {sorted_dict}")
print(f"Here's sorted dict {sorted_dict1}")
