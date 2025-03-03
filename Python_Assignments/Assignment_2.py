# 1. Write a function pascals_triangle(rows) that prints the first rows of
# Pascal’s Triangle using nested for loops.

def pascals_triangle(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1), end='')
        
        value = 1
        for j in range(i + 1):
            print(value, end=' ')
            value = value * (i - j) // (j + 1)
        
        print()

pascals_triangle(5)

# 2. Explain how the `continue` statement works in a loop.
# The continue statement in a loop in Python is used to skip the rest of the code inside the loop
# for the current iteration and proceed to the next iteration.
# When the continue statement is encountered, the loop does not terminate but immediately starts the next iteration.

# Coding Challenge: Write a Python program that iterates through a list of numbers
# and prints only those numbers that are divisible by 3, using the `continue` statement.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for number in numbers:
    if number % 3 != 0:
        continue
    print(number)

# 3. Use list comprehension to generate all Pythagorean triplets (a, b, c)
# where a² + b² = c² and a, b, c ≤ 50.

pythagorean_triplets = [
    (a, b, c)
    for a in range(1, 51)
    for b in range(a, 51)
    for c in range(b, 51)
    if a**2 + b**2 == c**2
]

for triplet in pythagorean_triplets:
    print(triplet)

# 4. Write a function max_consecutive_sum(nums, k) that finds the
# maximum sum of k consecutive elements in a list.

def max_consecutive_sum(nums, k):
    if len(nums) < k:
        return "List is shorter than k"
    
    max_sum = current_sum = sum(nums[:k])
    
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(max_consecutive_sum(nums, k))

# 5. Write a function that takes a list as an argument and modifies it by
# appending a new item. Demonstrate how changes to the list inside the
# function affect the list outside the function.

def append_to_list(my_list, item):
    my_list.append(item)
    print("Inside the function:", my_list)

original_list = [1, 2, 3]
append_to_list(original_list, 4)
print("Outside the function:", original_list)

# 6. Take a number as input and print the Fibonacci sequence up to that
# many terms using user-defined functions.

def fibonacci_sequence(n):
    a, b = 0, 1
    sequence = []
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci_sequence(num_terms)
print(f"The first {num_terms} terms of the Fibonacci sequence are: {fib_sequence}")
