# need to define tries before
tries = 0

while (tries < 5):
    # try stuff
    # increment tries
    tries += 1

# using a for loop instead
for t in range(5):
    # try stuff
    # don't need to increment tries!

# multi-line string
lines = '''
Write really long
stuff with these...
'''

# regular string
line = "just a regular string"

# some input validation
x = input("Enter a number less than 5: ")

# loop while x is still an invalid answer
while (x >= 5):
    x = input("Incorrect value. Please enter a number less than 5: ")

# multiple conditions
if (name == "tom") or (name == "sarah"):
    # do something

# same as
if name == "tom" or name == "sarah":
    # also do something

# NOT the same as
if name == "tom" or "sarah":
    # this will seem like it's working
    # for tom and sarah, but this will 
    # be True for all other names too!

# for loops
numbers = [1, 2, 3, 2, 1]

for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(numbers[i])

anExample = "Ada!"
print(len(anExample))
print("da" in anExample)
print(anExample[2])
print(anExample[2] + anExample[1])

for letter in anExample:
    print(letter)

# 2D lists
twoD = [[1, 2, 3],[7,8,9]]

print(twoD[0])
print(twoD[0][0])

for item in twoD[0]:
    print(item)

# averages solution
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

total = 0

for age in ages:
    total += age

average = total / len(ages)

print(average)


# guess that secret word pseudo-code
1. pick a secret word # store as a string variable
2. print blanks for each letter in the secret word
3. partner guesses a letter
4. compare guessed letter to secret word
    i. see if letter is in secret word
5.1 if letter is in secret word
    i. fill in/display letter(s) of the secret word
5.2 if letter is not in secret word
    i. display blanks again
    ii. take away/ subract a try
6. repeat starting at #3
7. stop when we run out of tries or the whole secret
    word is guessed

# HINTS
# using blanks
secret = "somesecretword"
blanks = "_" * len(secret)
blank_list = ["_"] * len(secret)

# index function
secret.index('s') # output 0

# using a for loop
guess = 't'
for letter in secret:
    if letter == guess:
        # do something

for i in range(len(secret)):

if guess in secret:

# validating input options
    Option A:
    if answer == "hi":
      say_greeting()
    elif answer == "hello":
      say_greeting()
    elif answer == "hey":
      say_greeting()

    Option B:
    if answer == "hi" or answer == "hello" or answer == "hey" or answer == "hey there" or answer == "sup":
      say_greeting()

# Function exercises
def is_even(num):
    if num % 2 == 0:
        # print("even")
        return True
    return False

def calc_total(alist):
    total = 0
    for x in alist:
        total += x
    return total

# some_total = calc_total(l)

# example usage:
response = input()
valid_answers = [...]

is_a_valid_answer = is_valid_input(response, valid_answers)

# functions worksheet
def is_valid_input(user_input, valid_answers):
    if (user_input in valid_answers):
        return True
    return False

...

valid = is_valid_input(response, possible_answers)

# functions worksheet answers
# pseudo-code:
1. define a function
2. make a loop
    i) look for the letter (ch) in the word
    ii) return where the letter is
    iii) if we do not find the letter return -1

# python code:
def find_char(ch, word):
    if ch in word:
        # return index of character ch
        return word.index(ch)
    return -1

def find_char(ch, word):
##    for i in word:
##        if i == ch:
##            re
    for i in range(len(word)):
        if word[i] == ch:
            return i
    return -1


# importing entire module
import turtle
# need to use module name to access functions
turtle.forward(15)


# importing all of the functions from the module
# --> like copying and pasting all of those
#       functions into your own file
from turtle import *
# don't need to use module name --> more unclear!
forward(15)

# Pillow notes:
IOError --> IO = Input/Output = I/O

# factory functions
Image.open()
- opens image file
- parameters: filename, optional mode
    - mode="r" # r = reading

Image.new()
- create a new Image (object)
- will not create an entire new file; only local to your file
- parameters: size, color, mode

# Image Class
Attributes:
- gives you the info about the data that makes up the object
- size = number of pixels
- width, height
- mode
- filename

Methods:
- band (channels) --> R, G, B
- Image.getpixel(xy)
- Image.putdata(data)

# AllTheFilters part1
from PIL import Image

def load_img(filename):
    im = Image.open(filename) # returns Image object!
    return im
    #return Image.open(filename)

def show_img(imageobject):
    # Image.show()
    imageobject.show()

def save_img(imageobject, filename):
    imageobject.save(filename) # imageobject.save(filename, 'jpeg')
    show_img(imageobject)

#importing our filters module
import filters
import Filters

# obamicon hint: creating a new Image
def obamicon(imageobject):
    # 1. get this image's width and height attributes
    w = imageobject.width
    h = imageobject.height

    #2. create a new image of the same size
    filtered_image = Image.new("RGB", (w,h))

    # filter the pixels!
    new_pixels = []

    # loop through imageobject pixels...
    # use getdata() or getpixel()...

    # plug new pixel values into the new image
    filtered_image.putdata(new_pixels)
    # when we're done, return the new image
    return filtered_image

# in filtergram.py
import filters

def main():
    file = "cube.jpg"

    myimage = filters.load_img(file)
    filters.show_img(myimage)

    filtered = filters.obamicon(myimage)
    filters.save_img(filtered)


if __name__ == "__main__":
    main()


# survey project starter with functions
def survey():
    answers = {}

    '''
    Below, write code that will pose the survey questions
    from the sutdent prompt to a user. Your program should
    save user input as a dictionary.
    '''

    # return the answers you collected!
    return answers

def main():
    myanswers = survey()
    print(myanswers)

if __name__ == "__main__":
    main()


    