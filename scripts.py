
import textwrap


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

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    student = float(sum(student_marks[query_name])/len(student_marks[query_name]))
    print("{:.2f}".format(student))

# e. Lists

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

# a. sWAP cASE


def swap_case(s):
    swapped = s.swapcase()
    return swapped

# b. String Split and Join


def split_and_join(line):
    # write your code here
    x = line.split(" ")
    y = "-".join(x)
    return y

# c. What's your Name?


def print_full_name(a, b):
    print("Hello " + str(a) + " " + str(b) + "! You just delved into python.")


# d. Mutations


def mutate_string(string, position, character):
    mutated_string = string[:position] + character + string[position+1:]
    return mutated_string

# e. Find a string


def count_substring(string, sub_string):
    length_sub_string = len(sub_string)
    count = 0
    for i in range(0, len(string) - length_sub_string + 1):
        if string[i:i + length_sub_string] == sub_string:
            count += 1

    return count

# f. String Validators

s = 'qA2'
alphanumeric_characters = False
alphabetical_characters = False
digits = False
lowercase_characters = False
uppercase_characters = False
for i in s:
    if i.isalnum():
        alphanumeric_characters = True
    if i.isalpha():
        alphabetical_characters = True
    if i.isdigit():
        digits = True
    if i.islower():
        lowercase_characters = True
    if i.isupper():
        uppercase_characters = True

print(alphanumeric_characters)
print(alphabetical_characters)
print(digits)
print(lowercase_characters)
print(uppercase_characters)

# g. Text Alignment

width = 5

# number of lines = width
for i in range(width):
    print('H'*(i*2+1)).rjust(width+i, ' ')
# numer of lines = width + 1
for _ in range(width+1):
    print('H'*width + ' '*width*3 + 'H'*width).center(width*5+(width-1),' ')
# number of lines = (width + 1)/2
for _ in range((width + 1)/2):
    print('H'*5*width).center(width*5+(width-1),' ')
# number of lines = width + 1
for _ in range(width+1):
    print('H'*width + ' '*width*3 + 'H'*width).center(width*5+(width-1),' ')
# number of lines = width
for i in range(width-1, -1, -1):
    print('H'*(i*2+1)).rjust(width*5+i, ' ')

# h. Text Wrap


def wrap(string, max_width):
    paragraph = textwrap.wrap(string, max_width)
    return "\n".join(paragraph)

# i. Designer Door Mat
# TODO: (Designer Door Mat) This code does not pass some of the solutions (despite having the same answer seemingly...)

s = 7
N = int(s[0])
M = N*3

for i in range((N/2)):
    print('.|.'*(i*2+1)).center(M, '-')
print('WELCOME').center(M, '-')
for i in range((N/2)-1, -1, -1):
    print('.|.'*(i*2+1)).center(M, '-')

# j. String Formatting
# I have looked up the part of "width = len("{0:b}".format(number)) + 1" since I did not understand the exercise
# explanation


def print_formatted(number):
    width = len("{0:b}".format(number)) + 1
    for i in range(number):
        print('{0:d}'.format(i+1).rjust(width-1) + '{0:o}'.format(i+1).rjust(width) + '{0:X}'.format(i+1).rjust(width)
              + '{0:b}'.format(i+1).rjust(width))

# k. Alphabet Rangoli


def print_rangoli(size):
    # your code goes here
    alphabet = [chr(ord('`')+i+1) for i in range(26)]
    alphabet_reverse = alphabet[::-1]
    width = size + (3*(size-1))
    for i in range(size-1):
        print('-'.join(alphabet_reverse[-size:-(size-1-i)] + alphabet[size-i:size])).center(width, '-')
    print('-'.join(alphabet_reverse[-size:] + alphabet[1:size]))
    for i in range(size-2, -1, -1):
        print('-'.join(alphabet_reverse[-size:-(size-1-i)] + alphabet[size-i:size])).center(width, '-')

# l. Capitalize!


def solve(s):
    single_characters = s.split(' ')
    capitalized_characters = [single_characters[i].capitalize() for i in range(len(single_characters))]
    return ' '.join(capitalized_characters)

# m. The Minion Game
# TODO: (The Minion Game) Issue with this piece of code is that it seems to take too much time to run. Look for a
#  better approach...


def minion_game(string, vowel_player='Kevin', consonant_player='Stuart'):
    # your code goes here
    alphabet = [chr(ord('`') + i + 1) for i in range(26)]
    ALPHABET = [alphabet[i].capitalize() for i in range(len(alphabet))]
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = [x for x in ALPHABET if x not in vowels]
    # find all possible permutations based on the string length
    permutations = []
    for i in range(len(string) + 1):
        for j in range(len(string) + 1):
            if i < j:
                permutations.append(string[i:j])
    starting_with_vowels = [x for x in permutations if x[0] in vowels]
    starting_with_consonant = [x for x in permutations if x[0] in consonants]
    score_vowel_player = len(starting_with_vowels)
    score_consonant_player = len(starting_with_consonant)

    if score_vowel_player == score_consonant_player:
        print('Draw')
    else:
        if score_vowel_player > score_consonant_player:
            print(vowel_player + ' ' + str(score_vowel_player))
        else:
            print(consonant_player + ' ' + str(score_consonant_player))

# n. Merge the Tools!


def merge_the_tools(string, k):
    # your code goes here
    string_split = textwrap.wrap(string, k)
    u = []
    for i in range(len(string_split)):
        u.append(''.join(list(set(string_split[i]))))
    print("\n".join(u))

# 4. SETS

# a. Introduction to Sets


def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))

# b. No Idea!
# SHOULD NOT BE TOO COMPLICATED!!!


# c. Symmetric Difference

M_ = raw_input()
M_temp = raw_input()
M = set(M_temp.split())
N_ = raw_input()
N_temp = raw_input()
N = set(N_temp.split())

M_N_differences = list(M.difference(N)) + list(N.difference(M))
final_list = list(map(int, M_N_differences))
final_list.sort()
sorted_list = list(map(str, final_list))

print('\n'.join(sorted_list))

# d. Set .add()

num_stamps = raw_input()
country_stamps = set()
for _ in range(int(num_stamps)):
    country = raw_input()
    country_stamps.add(country)

print(len(country_stamps))


# e. Set .discard(), .remove() & .pop()
# TODO: (Set .discard(), .remove() & .pop()) For some reason pop removes the 9, which then would be removed by the function remove, leading to an error...
num = raw_input()
s = set(list(map(int, raw_input().split())))
print(type(s))
print('start loop')
command_lines = raw_input()
for _ in range(int(command_lines)):
    inputs = raw_input().split()
    print(s)
    print(inputs)
    if inputs[0] == 'pop':
        s.pop()
    else:
        eval('s.' + str(inputs[0]) + '(' + str(inputs[1]) + ')')
sum(s)

# f. Set .union() Operation

num_students_english = raw_input()
roll_num_english = set(list(map(int, raw_input().split())))
num_students_french = raw_input()
roll_num_french = set(list(map(int, raw_input().split())))

print(len(roll_num_english.union(roll_num_french)))

# g. Set .intersection() Operation

num_students_english = raw_input()
roll_num_english = set(list(map(int, raw_input().split())))
num_students_french = raw_input()
roll_num_french = set(list(map(int, raw_input().split())))

print(len(roll_num_english.intersection(roll_num_french)))

# h. Set .difference() Operation

num_students_english = raw_input()
roll_num_english = set(list(map(int, raw_input().split())))
num_students_french = raw_input()
roll_num_french = set(list(map(int, raw_input().split())))

print(len(roll_num_english.difference(roll_num_french)))

# i. Set .symmetric_difference() Operation

num_students_english = raw_input()
roll_num_english = set(list(map(int, raw_input().split())))
num_students_french = raw_input()
roll_num_french = set(list(map(int, raw_input().split())))

print(len(roll_num_english.symmetric_difference(roll_num_french)))

# j. Set Mutations



# k. The Captain's Room


# l. Check Subset


# m. Check Strict Superset




# 5. COLLECTIONS


# 6. DATE AND TIME


# 7. ERRORS AND EXCEPTIONS


# 8. BUILT-INS


# 9. REGEX AND PARSING


# 10. XML


# 11. CLOSURES AND DECORATORS


# 12. NUMPY
