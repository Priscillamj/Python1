## TUPLES ##
 # TUPLES() (, , ,) create a collection of items that cannot change/Immutable, this means that the values inside of a tuple cannot be modified/Immutable
 # Tuples can contain string, numbers and decimals
 # type(mixed_tuple) # tuple
my_tuple = ('doctor', 'nurse', 'PA')
print(my_tuple) # ('doctor', 'nurse', 'PA')

 # EMPTY TUPLE
empty_tuple = ()

 # TUPLE WITH ONE ELEMENT
one_item_tuple = ('just me')
print(one_item_tuple) # just me

 # MIXED DATA TYPE TUPLES
 # you've already seen a string tuple
string_tuple = ("this", "contains", "string", "values")
print(string_tuple) # ('this', 'contains', 'string', 'values')

 # you can, of course, create tuples with numbers
number_tuple = (23, 23.5, 9, 144)
print(number_tuple) # (23, 23.5, 9, 144)

 # like lists, you can create tuples with a mix of types
mixed_tuple = ("Bob", 33, "Sally", 29, "Spike", 8)
print(mixed_tuple)


 # TUPLES INDEXING  len() function is used to get a count of the items in a collection
colors_list_tuple = ('red', 'green', 'blue', 'yellow')
num_colors_tuple = len(colors_list_tuple)
print(num_colors_tuple) # 4, 4 items in the tuple

 # ACCESSING ITEMS INDEXING To access values in a tuple, you append the index enclosed within square brackets [] to the end of the variable
 # #  (22, 33, 44, 55)
 ####   0   1   2   3  PYTHON WILL START WITH 0
 # print the second item of the tuple
numbers_tuple = (22, 33, 44, 55)
print(numbers_tuple[1])  # 33

 # To access the last item in a list, you can specify -1 as the index:
 # print the last item of the list
colors_list = ['red', 'green', 'blue', 'yellow']
print(colors_list[-1])   # yellow
 # print the last item of the tuple
numbers_tuple = (22, 33, 44, 55)
print(numbers_tuple[-1]) # 55
 # access the next-to-last item with index `-2`
second_from_end = colors_list[-2]
print(second_from_end) #blue
 # access the second from the last item with index `-3`
third_from_end = colors_list[-3]
print(third_from_end) #green
 
 # ACCESSING MULTIPLE ITEMS WITHIN A RANGE [#:#] [0:3] - returns items at positions 0, 1, and 2, [1:4] - returns items at positions 1, 2, and 3

colors_list = ['red', 'green', 'blue', 'yellow']
 # get the first three items
first_three_items = colors_list[0:3]
print(first_three_items) # ['red', 'green', 'blue']
 # get the middle two items
middle_two_items = colors_list[1:3]
print(middle_two_items)  # ['green', 'blue']

 # TUPLE: CONCATENATING / CONBINE tuples by adding them
tuple1 =("disco", 10, 1.2)
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2) # ('disco', 10, 1.2, 'hard rock', 10)

 # TUPLE : SLICING
tuple1 =("disco", 10, 1.2)
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2) # ('disco', 10, 1.2, 'hard rock', 10) 
tuple2[0:3] #       0      1   2        3        4
 #('disco', 10, 1.2) [0:3] 1 larger
tuple2[3:5]
 #('hard rock', 10) [3:5] 1 larger

 # IMMUTABLE tuples an not change value/ite 
Ratings = (10,9,6,5,10,8,9,6,2)
Rating1 = Ratings
Ratings[2] = 4
 # TypeError: 'tuple' object does not support item assignment
 
# Can only assinge a different tuple to the ratings variable
Ratings = (2,10,1)
print(Ratings)
print(Rating1)
 
 # We can Sort tuples =sorted(Varirable)
Ratings = (10,9,6,5,10,8,9,6,2)
RatingsSorted = sorted(Ratings)
print(RatingsSorted) # [2, 5, 6, 6, 8, 9, 9, 10, 10] []because its an assorted list, can't change

 # NESTING TUPLES : tuple that contains other tuples that contain different type class
NT = (1,2,('pop', 'rock'),(3,4),("disco",(1,2)))
 #    0 1        2          3           4 
 #         [2][0] [2][1] [3][0] [3][1]   [4][0][4][1]
NT[0] # 0
NT[1] # 2
NT[2] # ('pop', 'rock')
NT[2][0] # 'pop'
NT[2][1] # 'rock'
NT[3] # (3, 4)
NT[3][0] # 3
NT[3][1] # 4
NT[4] # ('disco', (1, 2))
NT[4][0] # 'disco'
NT[4][1] #  (1, 2)
NT[2][1][0] # 3[] will be letters [2pop rock] [1 rock][0 r]
NT [4][0][3] # [4 disco (1,2)] [0 disco] [3 c]
NT [4][1][1] # [4 disco (1,2)] [1 (1,2)] [1 2]

