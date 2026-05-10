"""

"""

string = "abcabcbb"

def find_longest_string_len(string: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(string)):
        
        while string[right] in char_set:
            char_set.remove(string[left])
            left += 1
        
        char_set.add(string[right])
        max_length = max(max_length, right-left+1)
    return max_length
    
print(find_longest_string_len(string))

def find_longest_unique_string(string: str) -> str:
    char_set = set()
    longest_substring = ""
    left = 0
    for right in range(len(string)):

        while string[right] in char_set:
            char_set.remove(string[left])
            left+=1

        char_set.add(string[right])
        current_substing = string[left:right+1]
        if len(current_substing) > len(longest_substring):
            longest_substring = current_substing

    return longest_substring
print(find_longest_unique_string(string))
