# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: String Algorithms Bundle - Palindrome, flatten list, unique chars
# Difficulty: Easy | Frequency: ⭐⭐⭐⭐
# ═══════════════════════════════════════════════════════════════
#
# TIME COMPLEXITY: O(n) for most functions, O(n^2) for nested list flatten
# SPACE COMPLEXITY: O(n) for dictionaries and result lists
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: TEXT ANALYSIS & WORD PROCESSING                        ║
# ║  PURPOSE: Collection of fundamental string algorithms             ║
# ║  INCLUDES: Non-repeating character, palindrome, list flattening   ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
First Non-Repeating Character
Input: "aabbcde"
Output: "c"
"""

def first_non_repeating_character(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for key, values in char_count.items():
        if values == 1:
            return key
    return None

input_string = "aabbcde"
result = first_non_repeating_character(input_string)
print(f"The first non-repeating character in '{input_string}' is: {result}")

"""
Check Palindrome
Ignore spaces and case.
"""

def is_palindrome(s):
    cleaned_string = s.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

input_string = "one of these days"
result = is_palindrome(input_string)
print(f"Is the string '{input_string}' a palindrome? {result}")


"""
Input: [1, [2, [3, 4]], 5]
Output: [1, 2, 3, 4, 5]
"""

def flatten_list(nested_list):
    flat_list =[]
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(item)
        else:
            flat_list.append(item)
    return flat_list

print(flatten_list([1, [2, [3, 4]], 5]))

"""
Input:
[
 "INFO Start",
 "ERROR Failed",
 "ERROR123 Wrong",
 "CRITICAL ERROR"
]

Output:
[
 "ERROR Failed",
 "CRITICAL ERROR"
]
"""

import re
def filter_error_logs(logs):
    error_logs = []
    for log in logs:
        if re.match(r"^ERROR\b", log) or re.match(r"^CRITICAL\b", log):
            error_logs.append(log)
    return error_logs   

logs = [
 "INFO Start",
    "ERROR Failed",
    "ERROR123 Wrong",
    "CRITICAL ERROR"
]
filtered_logs = filter_error_logs(logs)
print("Filtered Logs:")
for log in filtered_logs:
    print(log)  

logs = [
    "ERROR: Failed to connect DB",
    "INFO: Job started",
    "ERROR: Timeout occurred",
    "WARNING: Disk space low",
    "ERROR: Failed to connect DB"
]

def count_error_occurrences(logs):
    result = {}
    for entry in logs:
        if entry.startswith("ERROR"):
            # substring_error = entry.split(":")[0]
            substring_message = entry.split(":")[1].strip()
            result[substring_message] = result.get(substring_message, 0) + 1
    return result

error_logs = count_error_occurrences(logs)

sorted = sorted(error_logs.items(), key=lambda x: x[1], reverse=True)[:2]
print("Error Occurrences:", sorted)
for error, count in sorted:
    print(f"{error}: {count}")

    





