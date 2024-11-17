# Numbers
# An INTEGER is a whole number that can be positive or negative.
add_two_numbers = 2 + 2
print(add_two_numbers)
multiply_two_numbers = 33 * 54
print(multiply_two_numbers)
multiply_three_numbers = 33 * 54 * 89
print(multiply_three_numbers)
divide = 100/5
print(divide)

# FLOATS are "real number" with a "floating point" -can be positive or negative decimals
add_two_float_numbers = 0.1 + 0.4
print(add_two_float_numbers)
multiply_two_float_numbers = 3 * 0.1
print(multiply_two_float_numbers)


# You can change the type of the expression in Python, this is called typecasting

# You can convert an int 2 to a float
float(2) # will print 2.0
# You can convert an float 1.1 to a int
int(1.6) # will print 1 * you will lose the decimals what ever the number is before the decimal that is the number you will get(no round it out)
# You can convert a string contains an integer value, If we convert a string that contains a non-integer value, we get an error.
int("23") # will print 23 and the type()of class will change to integer
#  You can convert an int to a string or a float to a string.
str(5) #will print '5' and the type(int) of class changes to string
str(1.5) # will print '1.5' and the type(float) of class changes to string


# BOOLEAN can only take up 2 values True 1, False 0
type(True) # bool (class)
type(False) #bool (class)
int(True) # 1
float(False) # 0
bool(1) # True
bool(0) # False

# In the example code below, the two boolean variables indicate whether or not a user can update payment info. 
# This is taken from the context of the variable name, which is user_update_payment_info. If the value is True, then the user can update that info. 
# If the value is False, then the user cannot update payment info. Every boolean variable has either a value of True or False.
user_update_payment_info = False
# If the value is False, then the user cannot update payment info
edit_content = True
# If the value is True, then the user can update that info.


# MATH When doing math 1 / means you will get a float, 2 // means you will get a integer


# Exercise: Types

# What is the data type of the result of: 6 / 2?
6 / 2
type(6/2)
# 3.0 Float
6 // 2
type(6 //2)
# 3 integer


# What is the type of the result of: "Hello, World!"
type("Hello, World") # string

# What is the type of the result of: "hello" == "world"
type("Hello" == "World") # bool

# Write the code to convert the following number representing employeeid "1001" to an integer
int("1001") # 1001

# Write the code to convert this number representing financial value "1234.56" to a floating point number
float("1234.56") # 1234.56

#Write the code to convert this phone number 123-456-7890 to a string
str("123-456-7890")