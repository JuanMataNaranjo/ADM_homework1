import textwrap
import calendar
import os
import sys
from datetime import datetime
import email.utils
import re
from html.parser import HTMLParser
import xml.etree.ElementTree as etree
import numpy as np
from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict
from collections import Counter
from collections import deque
import operator

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

# g. Python If-Else

if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2) != 0:
        print('Weird')
    elif (n >= 2) & (n <= 5):
        print('Not Weird')
    elif (n >= 6) & (n <= 20):
        print('Weird')
    else:
        print('Not Weird')

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

if __name__ == '__main__':
    list_ = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_.append([name, score])
    dict_ = dict(list_)
    values = list(dict_.values())
    values_unique = list(set(values))
    values_unique.sort()
    second_lowest_grade = []
    for i in range(len(list_)):
        if list_[i][1] == values_unique[1]:
            second_lowest_grade.append(list_[i][0])
        else:
            continue
    second_lowest_grade.sort()
    print('\n'.join(second_lowest_grade))

# d. Find the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    student = float(sum(student_marks[query_name]) / len(student_marks[query_name]))
    print("{:.2f}".format(student))

# e. Lists

N = int(input())
list_ = []
for i in range(N):
    s = input().split()
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
    mutated_string = string[:position] + character + string[position + 1:]
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
    print('H' * (i * 2 + 1)).rjust(width + i, ' ')
# numer of lines = width + 1
for _ in range(width + 1):
    print('H' * width + ' ' * width * 3 + 'H' * width).center(width * 5 + (width - 1), ' ')
# number of lines = (width + 1)/2
for _ in range((width + 1) / 2):
    print('H' * 5 * width).center(width * 5 + (width - 1), ' ')
# number of lines = width + 1
for _ in range(width + 1):
    print('H' * width + ' ' * width * 3 + 'H' * width).center(width * 5 + (width - 1), ' ')
# number of lines = width
for i in range(width - 1, -1, -1):
    print('H' * (i * 2 + 1)).rjust(width * 5 + i, ' ')


# h. Text Wrap


def wrap(string, max_width):
    paragraph = textwrap.wrap(string, max_width)
    return "\n".join(paragraph)


# i. Designer Door Mat

N_M = list(map(int, input().split()))
N = N_M[0]
M = N * 3

for i in range(int((N - 1) / 2)):
    print(str('.|.' * (i * 2 + 1)).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(int(N / 2) - 1, -1, -1):
    print(str('.|.' * (i * 2 + 1)).center(M, '-'))


# j. String Formatting
# I have looked up the part of "width = len("{0:b}".format(number)) + 1" since I did not understand the exercise
# explanation


def print_formatted(number):
    width = len("{0:b}".format(number)) + 1
    for i in range(number):
        print('{0:d}'.format(i + 1).rjust(width - 1) + '{0:o}'.format(i + 1).rjust(width) + '{0:X}'.format(i + 1).rjust(
            width)
              + '{0:b}'.format(i + 1).rjust(width))


# k. Alphabet Rangoli


def print_rangoli(size):
    # your code goes here
    alphabet = [chr(ord('`') + i + 1) for i in range(26)]
    alphabet_reverse = alphabet[::-1]
    width = size + (3 * (size - 1))
    for i in range(size - 1):
        print('-'.join(alphabet_reverse[-size:-(size - 1 - i)] + alphabet[size - i:size])).center(width, '-')
    print('-'.join(alphabet_reverse[-size:] + alphabet[1:size]))
    for i in range(size - 2, -1, -1):
        print('-'.join(alphabet_reverse[-size:-(size - 1 - i)] + alphabet[size - i:size])).center(width, '-')


# l. Capitalize!


def solve(s):
    single_characters = s.split(' ')
    capitalized_characters = [single_characters[i].capitalize() for i in range(len(single_characters))]
    return ' '.join(capitalized_characters)


# m. The Minion Game


# First approach (seems to be too slow)
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


# Second approach (much faster since it only iterates over the word once)
def minion_game(string, vowel_player='Kevin', consonant_player='Stuart'):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    score_vowel = 0
    score_consonant = 0
    for i in range(len(string)):
        if string[i] in vowels:
            score_vowel = score_vowel + len(string) - i
        else:
            score_consonant = score_consonant + len(string) - i

    if score_vowel == score_consonant:
        print('Draw')
    else:
        if score_vowel > score_consonant:
            print(vowel_player + ' ' + str(score_vowel))
        else:
            print(consonant_player + ' ' + str(score_consonant))


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
    return sum(set(array)) / len(set(array))


# b. No Idea!

_ = list(map(int, input().split()))
array = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_array_intersection = set(A).intersection(array)
B_array_intersection = set(B).intersection(array)

positive_happiness = sum([i in A_array_intersection for i in array])
negative_happiness = sum([i in B_array_intersection for i in array])

print(positive_happiness - negative_happiness)

# c. Symmetric Difference

M_ = input()
M_temp = input()
M = set(M_temp.split())
N_ = input()
N_temp = input()
N = set(N_temp.split())

M_N_differences = list(M.difference(N)) + list(N.difference(M))
final_list = list(map(int, M_N_differences))
final_list.sort()
sorted_list = list(map(str, final_list))

print('\n'.join(sorted_list))

# d. Set .add()

num_stamps = input()
country_stamps = set()
for _ in range(int(num_stamps)):
    country = input()
    country_stamps.add(country)

print(len(country_stamps))

# e. Set .discard(), .remove() & .pop()

num = input()
s = set(list(map(int, input().split())))
command_lines = input()
for _ in range(int(command_lines)):
    inputs = input().split()
    if inputs[0] == 'pop':
        s.pop()
    else:
        eval('s.' + str(inputs[0]) + '(' + str(inputs[1]) + ')')

print(sum(list(s)))

# f. Set .union() Operation

num_students_english = input()
roll_num_english = set(list(map(int, input().split())))
num_students_french = input()
roll_num_french = set(list(map(int, input().split())))

print(len(roll_num_english.union(roll_num_french)))

# g. Set .intersection() Operation

num_students_english = input()
roll_num_english = set(list(map(int, input().split())))
num_students_french = input()
roll_num_french = set(list(map(int, input().split())))

print(len(roll_num_english.intersection(roll_num_french)))

# h. Set .difference() Operation

num_students_english = input()
roll_num_english = set(list(map(int, input().split())))
num_students_french = input()
roll_num_french = set(list(map(int, input().split())))

print(len(roll_num_english.difference(roll_num_french)))

# i. Set .symmetric_difference() Operation

num_students_english = input()
roll_num_english = set(list(map(int, input().split())))
num_students_french = input()
roll_num_french = set(list(map(int, input().split())))

print(len(roll_num_english.symmetric_difference(roll_num_french)))

# j. Set Mutations

_ = input()
A = set(list(map(int, input().split())))
command_lines = input()
for _ in range(int(command_lines)):
    inputs = input().split()
    N = set(list(map(int, input().split())))
    if inputs[0] == 'intersection_update':
        A.intersection_update(N)
    elif inputs[0] == 'update':
        A.update(N)
    elif inputs[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(N)
    elif inputs[0] == 'difference_update':
        A.difference_update(N)
print(sum(A))

# k. The Captain's Room

_ = input()
room_number_list = list(map(int, input().split()))

room_number_list.sort()

if len(room_number_list) % 2 == 0:
    set_1 = [room_number_list[i] for i in range(0, len(room_number_list), 2)]
    set_2 = [room_number_list[i] for i in range(1, len(room_number_list), 2)]
else:
    set_1 = [room_number_list[i] for i in range(0, len(room_number_list) + 1, 2)]
    set_2 = [room_number_list[i] for i in range(1, len(room_number_list), 2)]

captain_room = set(set_1).symmetric_difference(set_2)

print(list(captain_room)[0])

# l. Check Subset

test_cases = int(input())
for _ in range(test_cases):
    answer = True
    len_A = int(input())
    A = list(map(int, input().split()))
    len_B = int(input())
    B = list(map(int, input().split()))
    intersection = set(A).intersection(B)
    if list(intersection) != A:
        answer = False
    print(answer)

# m. Check Strict Superset

A = list(map(int, input().split()))
num_test_sets = int(input())
result = True
for _ in range(num_test_sets):
    test_sets = list(map(int, input().split()))
    difference = set(test_sets).difference(A)
    if len(difference) >= 1:
        result = False
        break
    elif len(A) == len(test_sets):
        result = False
        break
    else:
        continue
print(result)

# 5. COLLECTIONS

# a. collections.Counter()

num_shoes = int(input())
shoe_size = list(map(int, input().split()))
num_customers = int(input())
income = 0
for i in range(num_customers):
    request = list(map(int, input().split()))
    if request[0] in shoe_size:
        income += request[1]
        shoe_size.remove(request[0])
print(income)

# b. DefaultDict Tutorial

n_m = list(map(int, input().split()))
a = [input() for x in range(n_m[0])]
b = [input() for x in range(n_m[1])]

d = defaultdict(list)
for b_words in b:
    i = 0
    if b_words in a:
        for a_words in a:
            i += 1
            if a_words == b_words:
                d[b_words].append(i)
    else:
        d[b_words].append(-1)
    print(' '.join([str(d[b_words][i]) for i in range(len(list(set(d[b_words]))))]))

# c. Collections.namedtuple()

num_students = int(input())
columns = input()
Student_stats = namedtuple('Student_stats', columns)
list_ = []
for _ in range(num_students):
    list_.append(int(Student_stats(*list(input().split())).MARKS))

print("{:.2f}".format(sum(list_) / num_students))

# d. Collections.OrderedDict()

num_items = int(input())

ordered_dictionary = OrderedDict()
list_complete = []
list_items = []
for _ in range(num_items):
    temp = input().split()
    item = ' '.join(temp[:-1])
    price = temp[-1]
    list_complete.append([item, price])
    list_items.append(item)

list_counter = Counter(list_items)
for i in range(num_items):
    ordered_dictionary[list_items[i]] = int(list_complete[i][1]) * list_counter[list_items[i]]

for i in range(len(ordered_dictionary)):
    print(list(ordered_dictionary.keys())[i] + ' ' + str(list(ordered_dictionary.values())[i]))

# e. Word Order

num_words = int(input())
list_words = [input() for _ in range(num_words)]

words_counter = Counter(list_words)
ordered_dict_words = OrderedDict()
for word in list_words:
    ordered_dict_words[word] = words_counter[word]

print(len(ordered_dict_words))
print(*ordered_dict_words.values())

# f. Collection.deque()

num_lines = int(input())

d = deque()
for i in range(num_lines):
    command = list(input().split())
    if len(command) == 1:
        eval('d.' + command[0] + '()')
    else:
        eval('d.' + command[0] + '(' + command[1] + ')')
print(*list(d))

# g. Company Logo

if __name__ == '__main__':
    s = input()
    letter_count = list(Counter(s).items())
    ordered_list = sorted(sorted(letter_count, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)[0:3]

    for i in range(3):
        print(ordered_list[i][0], ordered_list[i][1])

# h. Pilling Up!

test_cases = int(input())

for _ in range(test_cases):
    num_cubes = int(input())
    size_cubes = deque(list(map(int, input().split())))
    base_pill = size_cubes.popleft() if size_cubes[0] >= size_cubes[-1] else size_cubes.pop()
    while size_cubes:
        if (len(size_cubes) == 1) & (size_cubes[0] <= base_pill):
            print('Yes')
        if (size_cubes[0] >= size_cubes[-1]) & (max(size_cubes[0], size_cubes[-1]) <= base_pill):
            base_pill = size_cubes.popleft()
        elif (size_cubes[-1] > size_cubes[0]) & (max(size_cubes[0], size_cubes[-1]) <= base_pill):
            base_pill = size_cubes.pop()
        else:
            print('No')
            break

# 6. DATE AND TIME

# a. Calendar Module

date = list(map(int, input().split()))

week_list = ['MONDAY',
             'TUESDAY',
             'WEDNESDAY',
             'THURSDAY',
             'FRIDAY',
             'SATURDAY',
             'SUNDAY']

week_day = calendar.weekday(date[2], date[0], date[1])
print(week_list[week_day])


# b. Time Delta


def time_delta(t1, t2):
    date_1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date_2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    delta = int(abs(date_1 - date_2).total_seconds())
    return str(delta)


# 7. ERRORS AND EXCEPTIONS

# a. Exceptions

num_loops = int(input())
for _ in range(num_loops):
    division_numbers = list(input().split())
    try:
        print(int(int(division_numbers[0]) / int(division_numbers[1])))
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print('Error Code:', e)

# b. Incorrect Regex
# I have looked for the re.compile function (found it in a code pretty similar to actual solution...)

num_loops = int(input())
for _ in range(num_loops):
    regex = input()
    try:
        re.compile(regex)
        print(True)
    except:
        print(False)

# 8. BUILT-INS

# a. Zipped!

num_students_subjects = list(map(int, input().split()))
results_matrix = []
for _ in range(num_students_subjects[1]):
    results_matrix.append(list(map(float, input().split())))

averages = [sum(list(zip(*results_matrix))[x]) / num_students_subjects[1] for x in range(num_students_subjects[0])]
for i in range(num_students_subjects[0]):
    print(averages[i])

# b. Input()

input_ = list(map(int, input().split()))
x = input_[0]
k = input_[1]
polynomial = input()
print(eval(polynomial + '==' + str(k)))

# c. Python Evaluation

input_string = input()
eval(input_string)

# d. Athlete Sort

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda x: x[k])
    for i in range(n):
        print(*arr[i])


# e. Any or All


def check_palindromic_integer(integer):
    # Check whether the integer is a palindromic integer
    len_integer = len(str(integer))
    if len_integer == 1:
        return True
    elif str(integer)[0:len_integer // 2 - 1] == str(integer)[-len_integer // 2:][::-1]:
        return True
    else:
        return False


_ = input()

number_list = list(map(int, input().split()))
condition_1 = [number_list[i] > 0 for i in range(len(number_list))]
condition_2 = [check_palindromic_integer(number_list[i]) for i in range(len(number_list))]
if all(condition_1) & any(condition_2):
    print(True)
else:
    print(False)

# f. ginortS

string = input()
lower_case = []
upper_case = []
odd_digit = []
pair_digit = []
splitted_string = [string[i] for i in range(len(string))]
for i in range(len(string)):
    if splitted_string[i].isdigit():
        if int(splitted_string[i]) % 2 == 1:
            odd_digit.append(splitted_string[i])
        else:
            pair_digit.append(splitted_string[i])
    else:
        if splitted_string[i].islower():
            lower_case.append(splitted_string[i])
        else:
            upper_case.append(splitted_string[i])
lower_case.sort()
upper_case.sort()
odd_digit.sort()
pair_digit.sort()
final_list = lower_case + upper_case + odd_digit + pair_digit
print(''.join(final_list))

# 9. PYTHON FUNCTIONALS

# a. Map and Lambda Function

cube = lambda x: x ** 3


def fibonacci(n):
    if n == 1:
        return [0]
    if n == 0:
        return []
    list_ = [None] * n
    list_[0:2] = [0, 1]
    for i in range(2, n):
        list_[i] = list_[i - 1] + list_[i - 2]
    return list_


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# 10. REGEX AND PARSING
# I have used internet for several of these exercises

# a. Detect Floating Point Number

test_cases = int(input())
regex_pattern = r'^[\+|\-|\.]?[0-9]*\.[0-9]{1,}$'
for _ in range(test_cases):
    string = input()
    print(bool(re.search(regex_pattern, string)))

# b. Re.split()

regex_pattern = r"\W+"

print("\n".join(re.split(regex_pattern, input())))

# c. Group(), Groups() & Groupdict()

string = str(input())
try:
    m = re.search(r'([a-zA-Z0-9])\1+', string).group(1)
    print(m)
except:
    print(-1)

# d. Re.findall() & Re.finditer()

string = str(input())
x = re.findall(
    r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',
    string)
if x:
    print('\n'.join(x))
else:
    print(-1)

# e. Re.start() & Re.end()

string = input()
k = input()

regex_pattern = '(?=(' + k + '))'
total_matches = re.findall(regex_pattern, string)
first_match = -1
if total_matches:
    for _ in total_matches:
        m = re.search(k, string[first_match + 1:])
        print('(' + str(m.start() + first_match + 1) + ', ' + str(m.end() - 1 + first_match + 1) + ')')
        first_match = m.start() + first_match + 1
else:
    print('(-1, -1)')

# f. Regex Substitution

code_lines = int(input())
updated_code = []
for _ in range(code_lines):
    code_line = input()
    print(re.sub(r'(?<=\s)(&&|\|\|)(?=\s)', lambda x: 'and' if (x.group() == '&&') else 'or', code_line))

# g. Validating Roman Numerals

regex_pattern = r'(?<=^)^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$(?=$)'
print(str(bool(re.match(regex_pattern, input()))))

# h. Validating phone numbers

num_phone_numbers = int(input())
regex_pattern = r'^[7-9]\d{9}'
for _ in range(num_phone_numbers):
    if bool(re.match(regex_pattern, input())):
        print('YES')
    else:
        print('NO')

# i. Validating and Parsing Email Addresses

num_email = int(input())
regex_pattern = r'^[a-zA-Z0-9](\w|-|\.|_)+@[a-zA-Z]+\.[a-z]{1,3}$'
for _ in range(num_email):
    email_temp = input()
    email_split = email.utils.parseaddr(email_temp)
    if bool(re.match(regex_pattern, email_split[1])):
        print(email_temp)

# j. Hex Color Code

lines_code = int(input())
inside_css_brackets = False
matches = []
for _ in range(lines_code):
    code = input()
    if bool(re.search(r'\{+|\}+', code)):
        inside_css_brackets = not inside_css_brackets
        continue
    if inside_css_brackets:
        matches.append(re.findall(r'(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})', code))

print('\n'.join(sum([x for x in matches if x != []], [])))


# k. HTML Parser - Part 1


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if attrs:
            print('Start :', tag)
            print('\n'.join(['-> ' + attrs[i][0] + ' > ' + str(attrs[i][1]) for i in range(len(attrs))]))
        else:
            print('Start :', tag)

    def handle_endtag(self, tag):
        print('End ', ':'.rjust(2), tag)

    def handle_startendtag(self, tag, attrs):
        if attrs:
            print('Empty :', tag)
            print('\n'.join(['-> ' + attrs[i][0] + ' > ' + str(attrs[i][1]) for i in range(len(attrs))]))
        else:
            print('Empty :', tag)


lines_code = int(input())
code = []
for _ in range(lines_code):
    code.append(input())
code = ' '.join(code)

parser = MyHTMLParser()
parser.feed(code)


# l. HTML Parser - Part 2


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if bool(re.search(r'\n', data)):
            print('>>> Multi-line Comment \n' + data)
        else:
            print('>>> Single-line Comment \n' + data)

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data \n' + data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
html

parser = MyHTMLParser()
parser.feed(html)
parser.close()


# m. Detect HTML Tags, Attributes and Attribute Values


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if attrs:
            print(tag)
            print('\n'.join(['-> ' + attrs[i][0] + ' > ' + str(attrs[i][1]) for i in range(len(attrs))]))
        else:
            print(tag)

    def handle_startendtag(self, tag, attrs):
        if attrs:
            print(tag)
            print('\n'.join(['-> ' + attrs[i][0] + ' > ' + str(attrs[i][1]) for i in range(len(attrs))]))
        else:
            print(tag)


lines_code = int(input())
code = []
for _ in range(lines_code):
    code.append(input())
code = ' '.join(code)

parser = MyHTMLParser()
parser.feed(code)

# n. Validating UID

test_cases = int(input())
for _ in range(test_cases):
    UID = input()
    condition_1 = bool(re.search(r'.*[A-Z].*[A-Z].*', UID))
    condition_2 = bool(re.search(r'.*[0-9].*[0-9].*[0-9].*', UID))
    condition_3 = bool(re.search(r'^[\w-]+$', UID))
    condition_4 = bool(re.search(r'^(?:([A-Za-z0-9])(?!.*\1))*$', UID))
    condition_5 = len(UID) == 10
    if all([condition_1, condition_2, condition_3, condition_4, condition_5]):
        print('Valid')
    else:
        print('Invalid')

# o. Validating Credit Card Numbers

num_credit_cards = int(input())

for _ in range(num_credit_cards):
    credit_card = input()
    condition_1 = bool(re.search(r'^[456]', credit_card))
    condition_2 = bool(re.search(r'([0-9]{4}-){3}[0-9]{4}$', credit_card)) | bool(re.search(r'[0-9]{16}', credit_card))
    updated_string = re.sub('-', '', credit_card)
    condition_3 = not bool(re.search(r'([0-9])\1{3,}', updated_string))
    condition_4 = len(updated_string) == 16
    if all([condition_1, condition_2, condition_3, condition_4]):
        print('Valid')
    else:
        print('Invalid')

# p. Validating Postal Codes

regex_integer_in_range = r"^[1-9][0-9]{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.

P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# q. Matrix Script

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

temp_list = list(zip(*matrix))
list_ = []
while temp_list:
    list_.extend(temp_list.pop(0))
matrix_string = ''.join(list_)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", matrix_string))


# 11. XML

# a. XML1 - Find the Score


def get_attr_number(node):
    # first level of xml
    score = len(node.attrib)
    # second level of xml
    for child in node:
        score = score + len(child.attrib)
        # third level of xml
        for grandson in child:
            score = score + len(grandson.attrib)
    return score


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# b. XML2 - Find the Maximum Depth

maxdepth = 0


def depth(elem, level):
    global maxdepth
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)


# 12. CLOSURES AND DECORATORS

# a. Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        updated_numbers = ['+91 ' + l[i][-10:-5] + ' ' + l[i][-5:] for i in range(len(l))]
        return f(updated_numbers)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


# b. Decorators 2 - Name Directory


def person_lister(f):
    def inner(people):
        updated_people = [x[0:2] + [int(x[2])] + list(x[-1]) for x in people]
        updated_people.sort(key=operator.itemgetter(2))
        return [f(i) for i in updated_people]

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# 13. NUMPY

# a. Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    reversed_array = np.flip(np.array(arr, float))
    return reversed_array


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# b. Shape and Reshape

initial_list = list(map(int, input().split()))
print(np.reshape(np.array(initial_list), (3, 3)))

# c. Transpose and Flatten

N_M = list(map(int, input().split()))
arr = []
for _ in range(N_M[0]):
    arr.append(list(map(int, input().split())))

print(np.transpose(np.array(arr)))
print(np.array(arr).flatten())

# d. Concatenate

N_M_P = list(map(int, input().split()))

N_P = []
M_P = []
for _ in range(N_M_P[0]):
    N_P.append(list(map(int, input().split())))
for _ in range(N_M_P[1]):
    M_P.append(list(map(int, input().split())))

print(np.concatenate((N_P, M_P), axis=0))

# e. Zeros and Ones

dimensions = list(map(int, input().split()))

print(np.zeros(shape=(*dimensions,), dtype=np.int))
print(np.ones(shape=(*dimensions,), dtype=np.int))

# f. Eye and Identity
# Looked for help since I was not understanding why the submission was not providing correct answer...

print(str(np.eye(*map(int, input().split()))).replace('1', ' 1').replace('0', ' 0'))

# g. Array Mathematics

N_M = list(map(int, input().split()))
A = []
B = []
for _ in range(N_M[0]):
    A.append(np.array(list(map(int, input().split()))))
for _ in range(N_M[0]):
    B.append(np.array(list(map(int, input().split()))))
A = np.array(A)
B = np.array(B)

print(A + B)
print(A - B)
print(A * B)
print((A / B).astype(int))
print(A % B)
print(A ** B)

# h. Floor, Ceil and Rint

arr = np.array(list(map(float, input().split())))

np.set_printoptions(sign=' ')

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

# i. Sum and Prod

N_M = list(map(int, input().split()))
arr = []
for _ in range(N_M[0]):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
sum_ = np.sum(arr, axis=0)
print(np.prod(sum_))

# j. Min and Max

N_M = list(map(int, input().split()))
arr = []
for _ in range(N_M[0]):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
min_ = np.min(arr, axis=1)
print(np.max(min_))

# k. Mean, Var and Std

np.set_printoptions(legacy='1.13')

N_M = list(map(int, input().split()))
arr = []
for _ in range(N_M[0]):
    arr.append(list(map(int, input().split())))

np.set_printoptions(sign=' ')

arr = np.array(arr)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))

# l. Dot and Cross

N = int(input())
A = []
B = []
for _ in range(N):
    A.append(np.array(list(map(int, input().split()))))
for _ in range(N):
    B.append(np.array(list(map(int, input().split()))))

print(np.dot(A, B))

# m. Inner and Outer

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print(np.inner(A, B))
print(np.outer(A, B))

# n. Polynomials

pol_coefficients = list(map(float, input().split()))
point = int(input())

print(np.polyval(pol_coefficients, point))

# o. Linear Algebra

np.set_printoptions(legacy='1.13')

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(float, input().split())))

determinant = np.linalg.det(arr)
print("{:.1f}".format(determinant))


# ===== Problem 2 =====

# a. Birthday Cake Candles

def birthdayCakeCandles(candles):
    maximum = candles[0]
    candles_to_blow = 0
    for i in range(len(candles)):
        if candles[i] > maximum:
            maximum = candles[i]
            candles_to_blow = 0
        if candles[i] == maximum:
            candles_to_blow += 1
    return candles_to_blow


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# b. Number Line Jumps

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if ((x1 > x2) & (v1 > v2)) | ((x2 > x1) & (v2 > v1)) | ((x1 != x2) & (v1 == v2)):
        return 'NO'
    elif ((x2 - x1) / (v1 - v2)).is_integer():
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# c. Viral Advertising


def viralAdvertising(n):
    arr = [None] * n
    arr[0] = 2
    for i in range(1, n):
        arr[i] = int((arr[i-1]*3)/2)
    return sum(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# d. Recursive Digit Sum


def superDigit(n, k):
    initial_digit = str(n)
    return initial_digit if (len(initial_digit) == 1) else superDigit(
        sum([int(initial_digit[i]) for i in range(len(initial_digit))]) * k, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# e. Insertion Sort - Part 1


def insertionSort1(n, arr):
    unsorted_value = arr[-1]
    for i in range(1, n + 1):
        try:
            if arr[-(i + 1)] > unsorted_value:
                arr[-i] = arr[-(i + 1)]
                print(' '.join([str(int) for int in arr]))
            else:
                arr[-i] = unsorted_value
                print(' '.join([str(int) for int in arr]))
                break
        except IndexError:
            arr[0] = unsorted_value
            print(' '.join([str(int) for int in arr]))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# f. Insertion Sort - Part 2


def insertionSort1(n, arr):
    unsorted_value = arr[-1]
    for i in range(1, n + 1):
        try:
            if arr[-(i + 1)] > unsorted_value:
                arr[-i] = arr[-(i + 1)]
            else:
                arr[-i] = unsorted_value
                break
        except IndexError:
            arr[0] = unsorted_value
    return arr


def insertionSort2(n, arr):
    for i in range(2, n + 1):
        arr[0:i] = insertionSort1(i, arr[0:i])
        print(' '.join([str(int) for int in arr]))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
