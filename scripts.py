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

# a. Find the Runner-Up Score

n = 5
arr = [2, 3, 6, 6, 5]

arr.sort()
print(list(set(arr))[-2])

# b. List Comprehensions

x = 2
y = 2
z = 2
n = 2

ls = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

print(ls)

# c. Nested Lists
# TODO: nested list


# d. Find the percentage
# TODO: find percentage (rounding is not working...)

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    print(student_marks[query_name])
    student = sum(student_marks[query_name])/len(student_marks[query_name])
    print(round(float(student), 2))

# e. Lists
# I have copied "s = raw_input().split()" from the solution (did not know how to access this input variables)

N = int(raw_input())
list_ = []
for i in range(N):
    s = raw_input().split()
    if s[0] == 'insert':
        eval('list_.' + str(s[0]) + '(' + s[1] + ',' + s[2] + ')')
    elif s[0] == 'print':
        print(list_)
    elif (s[0] == 'append') | (s[0] == 'remove'):
        eval('list_.' + str(s[0]) + '(' + s[1] + ')')
    else:
        eval('list_.' + str(s[0]) + '()')


# f. Tuples

n = 2
integer_list = [1, 2]
t = tuple(integer_list)
print(hash(t))

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
