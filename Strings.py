# PRINT A STRING

a = "Hello"
print(a)

# STRINGS ARE ARRAYS

a = "Hello world"
print(a[0])

# LOOPING THROUGH A STRING

for i in "banana":
    print(i)

# STRING LENGTH

a = "Hello World"
print(len(a))

# CHECKING A STRING

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
if "free" not in txt:
   print("No, free is not present.")

# SLICING A STRING

a = "Hello, World!"
print(a[2:4]) # This will print characters from index 2 to 4 (not including 4)

# -----------------------------------------------

a = "Hello, World!"
print(a[:4])

# -----------------------------------------------

a = "Hello, World!"
print(a[2:])

# -----------------------------------------------

a = "Hello, World!"
print(a[-5:-2])

# MODIFYING A STRING

a = "Hello, World!"
print(a.upper()) # This will convert the string to upper case

# -----------------------------------------------

a = "Hello, World!"
print(a.lower()) # This will convert the string to lower case

# -----------------------------------------------

a = " Hello, World! "
print(a.strip()) # This will remove any whitespace from the beginning or the end

# -----------------------------------------------

a = "Hello, World!"
print(a.replace("H", "J")) # This will replace H with J

# -----------------------------------------------

a = "Hello, World!"
print(a.split(",")) # This will split the string into a list where there is a comma

# STRING CONCATENATION

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# STRING FORMAT

age = 16
txt = f"My name is Mridul, and I am {age}"
print(txt)

# ------------------------------------------------

price = 50
txt = f"The price of chips is {price:.2f} rupees" # This will format the price to 2 decimal places
print(txt) 

# -------------------------------------------------

txt = f"The price is {20 * 59} dollars"
print(txt)

# ESCAPE CHARACTER

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hi \n Mridul"
print(txt)

# -------------------------------------------------

"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""