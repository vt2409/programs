# TIME COMPLEXITY: O(n^2) - Selection sort has nested loops
# SPACE COMPLEXITY: O(1) - In-place sorting, only constant extra space

"""
Sort the list
"""

arr = [4, 3, 2, 6]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


selection_sort(arr)
print(f"Here's sorted list {arr}")
""" Sort the dictionary by values without using built-in functions and return the sorted dictionary. """


def sort_dict_by_values(d):

    sorted_dict = {}
    values = selection_sort(list(d.values()))

    for value in values:
        for key, val in d.items():
            if val == value:
                sorted_dict[key] = value
                break

    return sorted_dict
