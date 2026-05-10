""" Here's a simple program to convert decimal numbers to binarys."""

def decimal_to_binary(n) -> str:
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

print(decimal_to_binary(10))  # Output: 1010
print(decimal_to_binary(5))   # Output: 101

