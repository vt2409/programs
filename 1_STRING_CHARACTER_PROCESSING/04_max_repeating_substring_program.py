# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Maximum Repeating Substring - Find most frequent substrings
# Difficulty: Medium | Frequency: ⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: STRING & CHARACTER PROCESSING                          ║
# ║  PURPOSE: Find maximum repeating substrings in a string           ║
# ║  ALGORITHM: Brute force substring generation and counting         ║
# ╚═══════════════════════════════════════════════════════════════╝

from collections import Counter

string = "abab"

def max_repeating_substrings(s, min_len=1):
    """Return (list_of_substrings_with_max_count, count).

    Args:
        s (str): input string
        min_len (int): minimum substring length to consider
    """
    n = len(s)
    if n == 0 or min_len > n:
        return [], 0

    counts = Counter()
    for i in range(n):
        for j in range(i + min_len, n + 1):
            counts[s[i:j]] += 1

    max_count = max(counts.values())
    result = [sub for sub, cnt in counts.items() if cnt == max_count]
    return result, max_count


if __name__ == "__main__":
    print(max_repeating_substrings(string))
