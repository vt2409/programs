# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Company: Epsilon
# Problem: Two Sum - Find indices of two numbers that add up to target
# Difficulty: Easy | Frequency: ⭐⭐⭐⭐⭐ (Very Common)
# ═══════════════════════════════════════════════════════════════

# ╔═════════════════════════════════════════════════════════════╗
# ║  CATEGORY: LIST MANIPULATION                                 ║
# ║  PURPOSE: Find two indices where elements sum to target       ║
# ║  COMPLEXITY: O(n) time, O(n) space - OPTIMAL                 ║
# ╚═════════════════════════════════════════════════════════════╝

sequence = [5,4,2,6,1]
target = 6


def find_target_sum_index(sequence, target):
    """
    Find two indices whose values sum to target using hash map.

    Time Complexity: O(n) - single pass through the list
    Space Complexity: O(n) - hash map stores elements

    Args:
        sequence: List of integers
        target: Target sum value

    Returns:
        Tuple of (index1, index2) or None if not found
    """
    num_map = {}  # Map: {number -> index}

    for i, num in enumerate(sequence):
        complement = target - num

        # Check if complement exists in map
        if complement in num_map:
            return (num_map[complement], i)  # Return indices

        # Store current number and its index
        num_map[num] = i

    return None  # No pair found


# Test cases
result = find_target_sum_index(sequence, target)
if result:
    idx1, idx2 = result
    print(f"✓ Target sum {target} found at indices: {idx1} and {idx2}")
    print(f"  Values: {sequence[idx1]} + {sequence[idx2]} = {target}")
else:
    print(f"✗ No pair found that sums to {target}")

# Additional test cases
print("\n--- Additional Tests ---")
print(find_target_sum_index([2, 7, 11, 15], 9))  # (0, 1) -> 2+7=9
print(find_target_sum_index([3, 2, 4], 6))  # (1, 2) -> 2+4=6
print(find_target_sum_index([5,4,2,6,1], 6))  # None
