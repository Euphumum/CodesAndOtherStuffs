# Strings
#     data that falls within " " marks

# Concatenation
# Put 2  or more strings together

firstName = "Fred"
lastName = "Flinstone"

fullName = firstName + " " + lastName

print(fullName)

# Repetition
# repetition operator: *

print("Hip " * 2 + "Hooray!")


def rowYourBoat():
    print("Row " * 3 + 'your boat')
    print("Gently down a stream")
    print("Merrily," * 4)
    print("Life is but a dream")


rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChair = name[0]
print(firstChair)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
#   slicing operator: :
#   slicing lets us make substrings

print(name[0:4])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name) + 1):
    print(name[0:i])

# Searching inside of strings

print("biv" in name)
print("v" not in name)

if "y" in name:
    print("The letter y is in name")
else:
    print("The letter y is not in  name")

# String Methods to investigate:
# Method        Use Example         Explanation

# center        aStr.center(w)
string = "Python is awesome"

new_string = string.center(24)

print("Centered String: ", new_string)
# Returns a string padded with fillchar. It doesn't modify the original string.

# ljust         aStr.ljust(w)
string = 'cat'
width = 5

print(string.ljust(width))
# Adds space to the end of the word

# rjust         aStr.rjust(w)
string = 'cat'
width = 5

print(string.rjust(width))
# Adds space to the beginning of the string

# upper         aStr.upper()
string = "this should be uppercase!"
print(string.upper())

string = "Th!s Sh0uLd B3 uPp3rCas3!"
print(string.upper())

# Makes everything UpperCase

# lower         aStr.lower()
string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())

string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())
# Makes everything lowercase

# index       aStr.index(item)
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
# rindex        aStr.rindex(item)
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)
# find          aStr.find(item)
txt = "Hello,welcome to my world."

x = txt.find("e, 5, 10")

print(x)
# rfind         aStr.rfind(item)
quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if result != -1:
    print("Highest index where 'be,' occurs:", result)
else:
    print("Doesn't contain substring")
# replace       aStr.replace(old, new)
song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')


print('Original string:', song)
print('Replaced string:', replaced_song)

song = 'let it be, let it be, let it be'

print(song.replace('let', 'so', 0))

# Be sure to include multiple examples of all of them in use

# Character Functions

print(ord('5'))

print(chr(97+13))

print(str(12548))

# testing functions from mapper.py

from mapper import *

print(letterToIndex('P'))
print(indexToLetter(10))

# this_is_a_secret_message_that_i_want_to_transmit
# t i _ s_a_s c e _ e s g _ h t_i_w n _ o_t a s i
#  h s_i _ _ e r t_m s a e_t a _ _ a t_t _ r n m t
# hsi_ertmaesta_att_rnmtti_sasce_esg_htiwn_otasi

from crypto import *

print(scramble2Encrypt("GOOD MORNING LADIES AND GENTLEMEN"))

print(scramble2Decrypt("ODMRIGLDE N ETEEGO ONN AISADGNLMN"))


def stripSpace(text):
    print(text.replace(" ", ""))


stripSpace("Hello world")










