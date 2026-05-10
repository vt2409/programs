"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

"""

from collections import defaultdict

def find_target_index(nums, target):

    freq = defaultdict(int)

    for index, num in enumerate(nums):
        
        compilement = target - num
        if compilement in freq:
            print(f"Here's output index of target {freq[compilement]} and {index}")
            return [freq[compilement], index]
        freq[num] = index
    return -1

def find_all_target_index(nums, target):
    result = []
    freq = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in freq:
            result.append((freq[complement], index))

        freq[num] = index

    return result


print(find_all_target_index([1,2,3,4,5], 6))


    