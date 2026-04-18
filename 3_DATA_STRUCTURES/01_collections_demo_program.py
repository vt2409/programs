# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Collections Module - Counter and defaultdict utilities
# Difficulty: Easy | Frequency: ⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: DATA STRUCTURES & COLLECTIONS                          ║
# ║  PURPOSE: Demonstrate Python Collections module features          ║
# ║  INCLUDES: Counter (frequency), defaultdict (auto-create keys)    ║
# ╚═══════════════════════════════════════════════════════════════╝
# ╚═══════════════════════════════════════════════════════════════╝

"""
The Collection module in python is very high performance, easy to use and standarized data structure beyond the list, dict, tuple, set. Here's
Following example.
"""

#here's example of Counter


example_string = "oneeeoofthebest"
from collections import Counter

char_freq = Counter(example_string)
print(f"Here's string frequencey {char_freq}")

# let the sort the dict based on key
sorted_dict = dict(sorted(char_freq.items(), key= lambda x: x[0], reverse=True))

# let the sort the dict based on value
sorted_dict = dict(sorted(char_freq.items(), key= lambda x: x[1], reverse=True))
print(f"Here's sorted the dict {sorted_dict}")


"""
Here's another example of using defaultdict

Basically using the default we don't have create the key while the value. basically it's autocrate and doesn't throught the error in
case key doesn't exist?

"""


from collections import defaultdict

magic_dict = defaultdict(list)
magic_dict["fruit"].extend("apple")
magic_dict["fruit"].extend("banana")

# print(f"let the see output of using defaultdict {magic_dict.items()}")

d = defaultdict(list)
d["fruits"].append("apple")
d["fruits"].append("banana")
print(d)

"""
Output: 
    Here's string frequencey Counter({'e': 5, 'o': 3, 't': 2, 'n': 1, 'f': 1, 'h': 1, 'b': 1, 's': 1})
    Here's sorted the dict {'e': 5, 'o': 3, 't': 2, 'n': 1, 'f': 1, 'h': 1, 'b': 1, 's': 1}
    defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})
"""