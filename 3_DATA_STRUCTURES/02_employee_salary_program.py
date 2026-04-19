# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Filter and Sort Data - Employee salary filtering and sorting
# Difficulty: Easy | Frequency: ⭐⭐⭐
# ═══════════════════════════════════════════════════════════════
#
# TIME COMPLEXITY: O(n log n) - Filtering O(n) + Sorting O(n log n)
# SPACE COMPLEXITY: O(n) - Result list storing filtered employees
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: DATA STRUCTURES & COLLECTIONS                          ║
# ║  PURPOSE: Filter and sort employee data                           ║
# ║  OPERATIONS: Filter by salary threshold, sort by salary           ║
# ╚═══════════════════════════════════════════════════════════════╝

employees = [
    {"name": "Alice", "department": "Engineering", "salary": 95000},
    {"name": "Bob", "department": "Marketing", "salary": 55000},
    {"name": "Charlie", "department": "Engineering", "salary": 120000},
    {"name": "Diana", "department": "HR", "salary": 48000},
    {"name": "Eve", "department": "Marketing", "salary": 72000},
]


def get_employee(employees,threshold):
    result = []
    for data in employees:
        if data['salary']>=threshold:
            result.append(data)

    sorted_result = sorted(result, key = lambda x : x['salary'], reverse=True)
    return sorted_result

print(get_employee(employees,90000))