def sum_of_list(l1, l2):
    result = []
    carry = 0

    for i in range(max(len(l1), len(l2))):
        val1 = l1[i] if i < len(l1) else 0
        val2 = l2[i] if i < len(l2) else 0

        total = val1 + val2 + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    return result

"""

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""
# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(sum_of_list(l1,l2))