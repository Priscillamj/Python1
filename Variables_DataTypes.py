# print()will print whats in the () words,numbers and equations
print("Hello World")
print("2+2") # will print 2+2
print(22)    # will print 22
print(-1.35) # will print -1.35
print(2+2)   # will print 4
print(2*3*4) # will print 24
print(4/3)   # will print 1.333333333333

# VARIABLE(name you give it) = Class (string, integer, float,boolean, list, tuple,)
# # Variables Contain letters, numbers, and underscores _, Cannot start with a number, Cannot contain spaces, Cannot be a Python reserved word (they will show up as blue in the editor)
# The variable `message` is assigned a text string value
message = "Hello World"
print(message)
# The variable `my_number` is assigned a numeric value
my_number = 29
print(my_number)
# The variable `my_message` is assigned to the value of another variable
my_message = message
print(my_message)
# this variable has one word, and its purpose is clear
message = "Hello"
# this variable has multiple words, each separated with an underscore
age_to_drive = 16
# this variable has multiple words, written in CamelCase
AgeToDrive = 16
# The below is a valid variable name using an underscore _ for the separation of the words
person_age = 20
# The below variable name will fail because it is using a space. The interpreter will think it is 2 variable names.
#      person age = 20
# Numbers are allowed in variable names
engine_piston_1_working = True
# numbers are NOT allowed at the beginning of a variable name. The below will fail
#      2nd_engine_piston_working = False
# Variable names cannot be reserved words - below, do you see that 'class' is orange?
#      class = 5
# If your variable name is in blue, that means it's a reserved word - so don't use it as a variable name!
# The variable `person_age` is not the same as....
person_age = 20
# ...the variable `Person_Age`, due to the differences in case
Person_Age = 40

my_message = "Hello World"
print(my_message)
animal_type = "cat"
print(animal_type)
human_age = 34
print(human_age)
weather = "bright and sunny"
print(weather)

# DATA TYPE: "Strings", Escape sequences"\"", Integers whole and negative numbers, Floats decimals and negative decimals , Booleans TRUE 1, FALSE 0
#  Strings  come after = and must be "" or ''
string_example_1 = "This is a string with double quotes"
string_example_2 ='This is also a string, but it utilizes single quotes'
string_example_3 ="""This is a multi-line
string that
spreads over 4
different lines"""
# Use single quotes when you need to quote someone.
string_example_4 = 'I told John, "you will really enjoy coding!"'
# Use double quotes when you need to use an apostrophe.
string_example_5 = "Using Python's straightforward syntax makes coding a lot easier."
# Use \ to use all single quotes and double quotes
string_example_6 = "She said \"Hello!\""
print(string_example_6)
string_example_7 = 'What\'s your name?'
print(string_example_7)

# Escape Sequences  \t,  \n,  \',  \"\""
escape_seq1 = "\tI should be shifted to the right"
print(escape_seq1)
#        I should be shifted to the right

escape_seq2 = "I am on one line\nbut I'm on the next line"
print(escape_seq2)
#I am on one line
#but I'm on the next line

escape_seq3 = "She said \"Hello!\""
print(escape_seq3) # She said "Hello!”

escape_seq4 = 'What\'s your name?'
print (escape_seq4) #What's your name?

# Numbers
# An integer is a whole number that can be positive or negative.
add_two_numbers = 2 + 2
print(add_two_numbers)
multiply_two_numbers = 33 * 54
print(multiply_two_numbers)
multiply_three_numbers = 33 * 54 * 89
print(multiply_three_numbers)
divide = 100/5
print(divide)

# A float is a real number with a "floating point" - a decimal
add_two_float_numbers = 0.1 + 0.4
print(add_two_float_numbers)
multiply_two_float_numbers = 3 * 0.1
print(multiply_two_float_numbers)

# Boolean 
user_update_payment_info = False
# If the value is False, then the user cannot update payment info
edit_content = True
# If the value is True, then the user can update that info.

# VARIABLE HANDS ON

# 1 create three variables 
MyName = "What is your name?"
my_age = "How old are you?"
My_Age = "How many months is that?"

# 2 create three more variables 
MyName1 = ('My name is "Billy".')
my_age_30 = ("30")
months = ("360")

# 3 Use the print function to print each of the variables
print(MyName)
print(MyName1)
print(my_age)
print(my_age_30)
print(My_Age)
print(months)

# 4 comment out comment out the appropriate variables and print functions so the output now looks like below: 
# What is your name?, My name is "Billy"., How old are you?, 30
print(MyName)
print(MyName1)
print(my_age)
print(my_age_30)

# print(My_Age)
# print(months)

# 5 Finally, create three new variables: my_string, my_integer, and my_float
my_string = "Have A great day!!!"
my_integer = 25 + 10 
my_float = 2.5 * 1.0
print(my_string)
print(my_integer)
print(my_float)