def interative_function(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def recursive_function(n):
    if n == 0:
        return 1
    else:
        return n * recursive_function(n-1)

numbers = [0, 5, 10, 25, 50, 100]

print("Factorial results using an interactive function")
for num in numbers:
    result = interative_function(num)
    print(f"{num}!={result}")

print("Factorial results using an recursive function")
for num in numbers:
    result = recursive_function(num)
    print(f"{num}!={result}")
