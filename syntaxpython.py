# Python syntax
# Numbers
# Finding Odd/Even
a = 2 % 1
# Returns 0 = Even
a = 7 % 4
# Returns 3 = Odd

# Power
a = 2 ** 2
pow(2,2,2)
# Hexadecimal
hex(2)
# Binary
bin(2)
# Rounding
round(1.234, 2)

# Precision
a = 100/1234567
a = f'Result = {a:1.3f}'
# 1 = width(10 = tab), 3f = pres

# String
# Slice
word = 'abcdefgh'
a = word[2:]
# cdefgh     0
a = word[-2]
# g
a = word[2:-2]
# cdefg
a = word [::2]
# aceg, skips every 2 letters
a = word[2:7:2]
# ceg, starting from index 2 -> 7, skips every 2 letters
a = word[::-1]
# hgfedcba, string reverse
word.upper()
word.lower()
word.split()

# Check alphanumeric
word.isalpha()
word.isalnum()


# Format / Inserting words
a = 'The {} {} {}'.format('brown', 'fox', 'quick')
a = 'The {2} {0} {1}'.format('brown', 'fox', 'quick')
a = 'The {q} {b} {f}'.format(b='brown', f='fox', q='quick')

b = 'brown'
f = 'fox'
q = 'quick'
a = f'The {q} {b} {f}'



# Lists
# Sorting Lists
list = ['a', 'b', 'c', 'd']
list2 = ['e', 'f', 'g', 'h']

newList = list + list2

list.sort()
list.reverse()
# Append values
list.append('q')



# Dictionaries
# Cannot be sorted
dict = {'a': 1, 'b': [1, 2, 3], 'c': {'dict2': 7}}

dict.keys()
dict.values()
dict.items()
# Returns Tuples



# Tuples
# Lists, Immutable

# Sets
# Unordered Lists with unique values
list = [1, 2, 2, 3, 4]
newset = set(list)

# res = {1, 2, 3, 4}
newset2 = newset.copy()
newset.add(7)
newset.difference(newset2)
# [7]
newset.difference_update(newset2)
# returns list after removing same elements, [7]

# Read/Write Files
%%writefile file.txt
abcdefgh

with open(file.txt, mode='r') as file:
    file.read()
    file.write('a')
# permissions = r,w,a,r+,w+

# Forloop Operators
list = [a, b, c, d]
list2 = [1, 2, 3, 4]
newList = []

for index,value in enumerate(list):
    print(index)
    print(value)
# returns index + value, can be used on strings
list = (num*2 for num in list2)
# forloop in a single line

newList(zip(list, list2))
# returns [(a,1), (b,2), (c,3), (d,4)], tuples



# Functions / lambda
list = [1, 2, 3, 4]

def mapList(num):
    return num**2

list(map(mapList,list))

def filterList(num):
    return num%2 == 0

list(filter(filterList,list))

(lambda num: num**2, list)
list(map(lambda num: num**2, list))



# Python Decr
def printname():
    print('print name')

def printnumbers(dec_func):
    def newfunc():
        print('1')
        dec_func()
        print('2')
    return newfunc

printnumbers(printname)

@printnumbers
def printname():
    print('print name')


# Generator Functions
def generatorFunction():
    for x in range(3):
        yield x

for x in generatorFunction():
    print(x)
    # 0,1,2

a = generatorFunction()

print(next(a))
# 0
print(next(a))
# 1
print(next(a))
# 2

b = 'dog'

for letter in b:
    print(letter)

next(b)
# error

iterB = iter(b)
next(iterB)


