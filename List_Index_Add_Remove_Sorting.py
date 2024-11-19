# LIST or ARRAY[] [ , , , ] is a data structure that holds a collection of objects (like an array)

# Creating a LIST/ARRAY  you can use string, numbers and mix 
planets = ['Earth', 'Mars', 'Saturn', 'Venus']
print(planets) # All string

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers) # All numbers

decimals = [1.1, 1.2, 1.3, 1.4, 1.5]
print(decimals) # All decimals

ListTuples = ['Michael Jackson', 10.1, 1982, [1,2], ('A',1)]
print(ListTuples) # ['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1)]
                  #     String        , float, int, [another list], (tuple)]
# TYPE(Class) LIST
another_variable = "Hello world"
my_list = ["String", 3, 7.5, another_variable]
print(my_list) # ['String', 3, 7.5, 'Hello world']
type(my_list) # List


# The result of calling split on the above string variable resulted in the creation of a list.
my_message = "Split these words for me"
split_at_spaces = my_message.split()
print(my_message.split())
['Split', 'these', 'words', 'for', 'me'] # ['Split', 'these', 'words', 'for', 'me']
# As you can see above, all of the words are between square brackets ([ and ]) and are separated with commas. This is the structure of a list in Python.


# A list/array can contain a string value, two number values,  variable names.
another_variable = "Hello world"
my_list = ["String", 3, 7.5, another_variable]
print(my_list) # ['String', 3, 7.5, 'Hello world']


# NESTING LIST/ARRAY  create a list that contains other lists ['1st List',['2nd List','', '' ], ['3rd List','']] 3 brackets for 3 list.
our_world = ['Earth', ['United States', 'Canada', 'Mexico'], [1, 2, 3]]
print(our_world) # ['Earth', ['United States', 'Canada', 'Mexico'], [1, 2, 3]]

ListTuples = ['Michael Jackson', 10.1, 1982, [1,2], ('A',1)]
print(ListTuples) # ['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1)]
                  #     String        , float, int, [another list], (tuple)]


# EMPTY LIST/ARRAY
my_empty_list = []

# LIST INDEXING  len() function is used to get a count of the items in a collection
colors_list = ['red', 'green', 'blue', 'yellow']
num_colors = len(colors_list)
print(num_colors) # 4, 4 items in the list

# ACCESSING ITEMS SLICING / INDEXING To access values in a list, you append the index enclosed within square brackets [] to the end of the variable
   #[red, yellow, blue, green, purple]
####  0      1      2     3      4   PYTHON WILL START WITH 0
# print the third item of the list
colors_list = ['red', 'yellow', 'blue', 'green', 'purple']
print(colors_list[2])  #blue

ListTuples = ["Michael Jackson", 10.1, 1982, [1,2], ('A',1)]
 #                0                1     2     3        4  
ListTuples[0][10] #           [0'michael'][letter/one word]
ListTuples[1] # 10.1
ListTuples[3][1] # 2
ListTuples[4][0] # 'A'

# MODIFYING LISTS
  # the starting list
contacts = ['Sally', 'Bob', 'Mary', 'Steven']
  # Bob prefers to go by "Robert"
  # Bob is at index 1 in the list
contacts[1] = "Robert"
print(contacts)

colors_list = ['white', 'white', 'white', 'white']
print(colors_list)

colors_list[0] = 'red'
colors_list[1] = 'green'
colors_list[2] = 'blue'
colors_list[3] = 'yellow'
print(colors_list)

colors_list[-1] = 'purple'
print(colors_list)
['white', 'white', 'white', 'white']
['red', 'green', 'blue', 'yellow']
['red', 'green', 'blue', 'purple']  

# ADDING AN ITEM TO THE END OF THE LIST  .append()
my_string = "Hello there Bob"
# splits string into list using space as the delimiter/separator
my_string_items = my_string.split()
print(my_string_items)
['Hello', 'there', 'Bob']
# but we forgot Sally!
# add 'and' and 'Sally' to the list
my_string_items.append("and")
my_string_items.append("Sally")
print(my_string_items)
['Hello', 'there', 'Bob', 'and', 'Sally']

numbers = [1, 2, 3, 4, 5]
# add 6 to the end
numbers.append(6)
# add 'seven' to the end
numbers.append('seven')
print(numbers)
[1, 2, 3, 4, 5, 6, 'seven']

# INSERTING AN ITEM INTO THE LIST  .insert(the place value(0,1,2,3rd place), what you want to insert)
my_list = [1, 2, 4]
# Oops! Forgot 3!
my_list.insert(2, 3)
print(my_list)  #[1, 2, 3, 4]

my_list = [1, 2, 3, 5]
# add 'zero' to the beginning of the list
my_list.insert(0, 'zero')
# insert `four' at index 4
my_list.insert(4, 'four')
print(my_list) 
['zero', 1, 2, 3, 'four', 5]

colors = ['red', 'white', 'blue']
colors.insert(1, "green")
colors.insert(3, "yellow")
print(colors)

# REMOVING AN ITEM FROM THE LIST  .remove()  del[]   index means place value
    # When You Know the Index - del     
numbers = [1, 2, 3, 4]
# delete item at index 2  (remember 3 is in the second place)
del numbers[2]
print(numbers) [1, 2, 4]
# the position of value 4 has changed
# its index went from 3 to 2, due to the deletion

# delete the first item (1 is in the 0 place)
del numbers[0]
print(numbers)  [2, 4]

# delete the last item (-1 means last place)
del numbers[-1]
print(numbers)   [2]

  # When You Don't Know the Index - .remove()
colors = ['red', 'blue', 'yellow', 'green']
colors.remove('yellow')
print(colors) ['red', 'blue', 'green'] 

colors = ['red', 'blue', 'red', 'green']
colors.remove('red')
print(colors)  ['blue', 'red', 'green']

  # CREATING A LIST FROM A RANGE OF NUMBERS  range() 
   # Storing Range as a List
numbers = list(range(1, 11))
print(numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   #Storing Range as a Variable
the_range = range(1, 11)
numbers = list(the_range)

  # Range with No Start Value  (will start at 0)
no_start_range = range(5)
numbers = list(no_start_range)
print(numbers)
[0, 1, 2, 3, 4]

   # Specify the Increment in the Range
inc_by_2_range = range(2, 11, 2) # 2-11 everother even# skip 1
numbers = list(inc_by_2_range)
print(numbers)
[2, 4, 6, 8, 10] 

inc_by_10_range = range(0, 101, 10)  # 0- 101  count by 10s
numbers = list(inc_by_10_range)
print(numbers)
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# SORTING A LIST .sort()
   #sort numerically
numbers = [2, 6, 3, 9, 1, 10]
numbers.sort()
print(numbers)  
[1, 2, 3, 6, 9, 10]
   # sort alphabetically
strings = ['dog', 'cat', 'bird']
strings.sort()
print(strings)
['bird', 'cat', 'dog']

   # Sort in Descending Order   .sort(reverse=True)
numbers = [2, 6, 3, 9, 1, 10]
numbers.sort(reverse=True)
print(numbers)
[10, 9, 6, 3, 2, 1]

   # Non-Permanent Sorting     print(sorted(variable name))
numbers = [2, 6, 3, 9, 1, 10]
print(numbers) #[2, 6, 3, 9, 1, 10]
print(sorted(numbers)) #[1, 2, 3, 6, 9, 10]
print(numbers) #[2, 6, 3, 9, 1, 10]

A = [1]
A.append([2,3,4,5])
print(A) # [1, [2, 3, 4, 5]]

