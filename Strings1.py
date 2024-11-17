# Data Types: Strings, Escape sequences
#  Strings  come after = 
string_example_1 = "This is a string with double quotes"
print(string_example_1) # "This is a string with double quotes"
string_example_2 ='This is also a string, but it utilizes single quotes'
print(string_example_2) # 'This is also a string, but it utilizes single quotes'
string_example_3 ="""This is a multi-line
string that
spreads over 4
different lines"""
print(string_example_3) #This is a multi-line
# string that
# spreads over 4
# different lines

# Use single quotes when you need to quote someone.
string_example_4 = 'I told John, "you will really enjoy coding!"'
print(string_example_4) # I told John, "you will really enjoy coding!"

# Use double quotes when you need to use an apostrophe.
string_example_5 = "Using Python's straightforward syntax makes coding a lot easier."
print(string_example_5) # Using Python's straightforward syntax makes coding a lot easier.

# Use \ to use all single quotes and double quotes
string_example_6 = "She said \"Hello!\""
print(string_example_6) # She said "Hello!"
string_example_7 = 'What\'s your name?'
print(string_example_7) # What's your name?

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


# You can convert a string contains an integer value, If we convert a string that contains a non-integer value, we get an error. (NO WORDS)
int("23") # will print 23 and the type(string)of class will change to integer 
type(int("23"))
# or you can convert an int to a "string"
str(5) #will print '5' and the type(int) of class changes to string

# a 'string' to flaot.
float("25") # will print 25.0
# or a float to string
str(1.5) # will print '1.5' and the type(float) of class changes to "string"


# find the type 
#type(int, float, string(the value))