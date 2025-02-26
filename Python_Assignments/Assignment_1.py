""" 1. How do lists and tuples differ in terms of mutability and 
performance? When would you choose one over the other? """

# Lists are mutable, meaning that you can change the values of the elements in the list.
# Tuples are immutable, meaning that you cannot change the values of the elements in the tuple. 
# Lists are slower than tuples because of the mutability.

""" 2. Explain how Python handles type conversion between different data 
types, such as between integers and floats or between strings and 
lists. """

# Python handles type conversion between different data types int(), float(), str(), list(), etc.

## Example 
# Convert a string to an integer
a = "50"
print(int(a))

# Convert an integer to a float
b = 50
print(float(b))

# Convert a string to a list
c = "Hello"
print(list(c))

""" Take a number and use the += operator to increase its value by 10. """
number = 10
number += 10
print(number)

""" 4. Write a Python program to check if a given year is a leap year or not. """
year = int(input("Enter a year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

""" 5. Write a program that asks the user to enter their marks and displays 
their grade: 
• 90-100: A 
• 80-89: B 
• 70-79: C 
• 60-69: D 
• Below 60: F  """

marks = int(input("Enter your marks"))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
elif marks >= 60 and marks < 70:
    print("D")
elif marks < 60:
    print("F")
else:
    print("Grades are not to be calculated")