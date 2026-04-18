# ═══════════════════════════════════════════════════════════════
# 🏢 INTERVIEW QUESTION
# Problem: Python Decorators - Function wrapping and modification
# Difficulty: Medium | Frequency: ⭐⭐⭐⭐
# ═══════════════════════════════════════════════════════════════

# ╔═══════════════════════════════════════════════════════════════╗
# ║  CATEGORY: ADVANCED PYTHON CONCEPTS                               ║
# ║  PURPOSE: Demonstrate Python Decorators                           ║
# ║  PATTERNS: With/without parameters, function wrapping             ║
# ╚═══════════════════════════════════════════════════════════════╝

#with parameter

# def decorator_example(funct):
#     def wrapper(*args,**kargs):
#         print("Executing the wrapper function")
#         funct(*args,**kargs)
#         print("Exeuted the actually function")
#     return wrapper


# @decorator_example
# def sample_function(value):
#     print(f"Execute the sample function {value}")


# sample_function("vikas")

#without parameter


# def decorator_example(function_decorator):
#     def wrapper():
#         print("Hello, I am decorator function")
#         function_decorator()
#         print("Thank you for using it")
#     return wrapper
        

# @decorator_example
# def sample_function():
#     print("Heey, I am sample function")

# sample_function()


def decorator_example(function_decorator):
    def wrapper(request_body):
        print("Hello, I am decorator function")
        request_body["decorated"] = True
        function_decorator(request_body)
        print("Thank you for using it")
    return wrapper

@decorator_example
def actual_function(request_body):
    print(f"I am the actual function with request body: {request_body}")

request_body = {
    "name": "Vikas",
    "age": 30,
    "city": "New York"
}

print(actual_function(request_body))