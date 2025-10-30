from functools import reduce
import random
def my_tripler(n):
    return n * 3
def is_divisible(n):
    return n % 3 == 0


numbers = [3, 4, 5, 6]
tripler = map(my_tripler, numbers)
sum = reduce(lambda a,b:a+b,numbers)
divisible = filter(is_divisible,numbers)
print(list(divisible))
print(sum)
print(list(tripler))

# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

print(squares)
# Dictionary comprehension
students = {"Ali": 85, "Sara": 90, "Umar": 76}
grades = {name: ("A" if marks > 80 else "B") for name, marks in students.items()}
print(grades)

"""
Create a list of 10 random numbers between 1–100.
Use list comprehension to:
Get only even numbers.
Create a dict: {number: "Even"/"Odd"}."""


random_number = [random.randrange(1,100) for n in range(10) ]
print(random_number)

even_numbers = {x: ("Even" if x%2==0 else "Odd") for x in random_number}
print(even_numbers)


"""Create a lambda that takes a name and returns "Hello, <name>".

Create another that squares a number.

Use lambdas inside sorted() to sort a list of tuples by their second value:

data = [("Ali", 90), ("Sara", 85), ("Umar", 95)]"""


def greeting(name):
    return lambda : f"Hello {name}"

names = {"bob", "marley", "James"}
for x in names:
    print(greeting(x)())

def square(num):
    return lambda : num*num
for x in numbers:
    print(square(x)())

def sorting(data, y):
    z = []
    for a in y:
        for b in data:
            if a==b[1]:
                z.append(b)
            else:
                continue
    return z



data = [("Ali", 90), ("Sara", 85), ("Umar", 95)]
y = []
for x in data:
    y.append(x[1])
y.sort()
print(sorting(data, y))

sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)



import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ Function '{func.__name__}' took {end - start:.4f} sec")
        return result
    return wrapper

@timer
def process_data():
    time.sleep(1)
    print("Data processed!")

process_data()




from functools import reduce

data = [12, 45, 33, 27, 89, 66, 23, 41, 90]

# Filter out values below 40
filtered = list(filter(lambda x: x >= 40, data))

# Transform: square each number
transformed = list(map(lambda x: x**2, filtered))

# Reduce: find sum of all squared values
total = reduce(lambda a, b: a + b, transformed)

print(f"Filtered: {filtered}")
print(f"Squared: {transformed}")
print(f"Sum of squares: {total}")
