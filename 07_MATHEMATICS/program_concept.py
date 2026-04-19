
"""
We've two list and want to find the common items between them and store them in new list and both list are sorted.

a = [1,3,5,7,9]
b = [2,3,5,9,11]

result = [3,5,9]

"""

# TIME COMPLEXITY: O(n + m) - Set operations take linear time
# SPACE COMPLEXITY: O(min(n,m)) - Result list size at most min(list1, list2)
def common_items(list1, list2):
    """
    Find common items between two sorted lists using set intersection.
    O(n + m) time complexity.
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
    """
    result = list(set(list1) & set(list2))
    result.sort()  # Maintain sorted order
    print(f"Here's the output of common items {result}")
    return result

# TIME COMPLEXITY: O(n + m) - Single pass through both lists with two pointers
# SPACE COMPLEXITY: O(1) - Only two pointers, result list not counted
def common_items_optimized(list1, list2):
    """
    Find common items between two sorted lists using two-pointer technique.
    O(n + m) time complexity, O(1) extra space (excluding result list).
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
    """
    result = []
    pointer1 = 0
    pointer2 = 0
    
    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1] == list2[pointer2]:
            result.append(list1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif list1[pointer1] < list2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
    
    return result

print(common_items([1,3,5,7,9], [2,3,5,9,11]))
print(common_items_optimized([1,3,5,7,9], [2,3,5,9,11]))


