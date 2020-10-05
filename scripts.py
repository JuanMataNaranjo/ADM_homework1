# 1. INTRODUCTION

# a. Say "Hello, World!" With Python

print('Hello, World!')

# b. Arithmetic Operators

a = 3
b = 5

print(a + b)
print(a - b)
print(a * b)

# c. Python: Division

a = 4
b = 3

print(a // b)
print(a / b)

# d. Loops

n = 5

for i in range(0, n):
    print(i ** 2)


# e. Write a function


def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 400) == 0:
        leap = True
    elif (year % 100) == 0:
        leap = False
    elif (year % 4) == 0:
        leap = True

    return leap


# f. Print Function

n = 3

result = str()
for i in range(1, n + 1):
    result = result + str(i)
print(result)

# 2. BASIC DATA TYPES


# 3. STRINGS


# 4. SETS


# 5. COLLECTIONS


# 6. DATE AND TIME


# 7. ERRORS AND EXCEPTIONS


# 8. BUILT-INS


# 9. REGEX AND PARSING


# 10. XML


# 11. CLOSURES AND DECORATORS


# 12. NUMPY
