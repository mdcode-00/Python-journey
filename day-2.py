# python has a print function
print("i'm Python. Nice to meet you")
# => i'm Python. Nice to meet you

# by default the print function also print out a newline at the end.
# use the optional argument end to change the end String
print("hello world" , end="!")
print("NEXT")

#Simple way to get input data from console.
input_string_var = input("Enter some data: ") 
# #return the data as a string


# there are no declaration, only assigments.
# convention in naming variables is snake_case style
some_var = 5
print(some_var)

# accessing a previously unassignet variable is an excceseption.
# see_unknown_var # Rasioses a NameError
print("yay!" if 0 > 1 else "nay!")

# lists store with a perfilled list
li = []
# you can start with a prefilled list 
other_list= [4,5,6]

# Add stuff to the end of a list with append
li.append(1) # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(4)    # li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3]
print(li)
# remove from the end with opo
li.pop()  # => 3 and li is now [1, 2, 4]
print(li)
# let's put it back
li.append(3)  # li is now [1, 2, 4, 3] again.
print(li)

# access a list like you wouls any array
print(li[0]) # => 1
# look at the last element
print(li[-1]) # => 3

# Locking out of the bounds is an IndexError 
# print(li[4]) # Raises an IndexError

# you can also look at ranges with slice syntax.
# the start inedx is includes, the end index is not 
# (it's a closed/open range for you mathy types.)
print(li[1:3]) # Return list from index 1 to 2 => [2, 4]
print(li[2:])  # Return list starting from index 2 => [4, 3]
print(li[:3]) # Return list from beginning until index 3  => [1, 2, 4]
print(li[::2])  # Return list selecting elements with a step size of 2 => [1, 4]
print(li[::-1])  # Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# make one layer deep copy using slice 
li2 = li[:] # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.
print(li2)

# remove arbitrary element from a list with "del"
del li[2] # li is now [1, 2, 3]
print(li)

# remove first occurrence of a value
li.remove(2)# li is now [1, 3]
# li.remove(2)# Raises a ValueError as 2 is not in the list
print(li)

# Insert an element at a specific index
li.insert(1,2) # # li is now [1, 2, 3] again   (index , value)
print(li)

# get the index of the first item found macthing the argument 
print(li.index(2)) # => 1
# print(li.index(4)) # Raises a ValueError as 4 is not in the list

# you can add lists 
# note: value for li and for other _li are not modifiled.
print(li + other_list ) # => [1, 2, 3, 4, 5, 6]
print(li)

# concatenated litsts with :extend()
li.extend(other_list) # Now li is [1, 2, 3, 4, 5, 6]
print(li)

# in checks whether a value exists inside a list.
print(1 in li)   # => True

# Examine the length with "len()"
print(len(li)) # => 6


# Tuples are like listas but are  immutable
tup = (1,2,3)
print(tup[0]) # => 1
# tup[0] = 3  # Raises a TypeError

# note that a tuple of length one has to have a comma agter the last element but 
# tubles of other length, even zero, do not.
print(type((1))) # => <class 'int'>
print(type((1,))) # => <class 'tuple'>
print(type(()))  # => <class 'tuple'>

print(len(tup))  # => 3
print(tup + (4, 5,6)) # => (1, 2, 3, 4, 5, 6)
print(tup[:2])  # => (1, 2)
print(2 in tup)   # => True

# you can unpack tubles (or lists) into variables
a,b,c = (1,2,3)
print(a,b,c)# a is now 1, b is now 2 and c is now 3
# you can also do extended unpacking
a, *b, c = (1,2,3,4)  # a is now 1, b is now [2, 3] and c is now 4
print(a,b,c)
#tuples are created by default if you leave out the parentheses
d,e,f = 4,5,6
print(d,e,f) # tuple 4, 5, 6 is unpacked into variables d, e and f
# respectively such that d = 4, e=5 and f = 6
# now look how easy it is to swap two value
e, d = d, e
print(d,e) # d is now 5 and e is now 4


# dicttionaries store mapping from keys to value
empty_dict = {}
# here is s a prefilled dictionary
filled_dict = {"one": 1 , "two":2, "three":3}
print(filled_dict)


# note keys for deraction have to be imutable types. this is to ensure that
# the key can be converted toa contant hash value for quick look-ups.
# immutable types includs ints, floats, string, tuples.
#  invalid_dict = {[1,2,3]: "123"} # => Yield a TypeError: unhashable type: 'list'
#  print(invalid_dict)

valid_dirct = {(1,2,3): [1,2,3]}
print(valid_dirct)


# look up values with []
print(filled_dict["one"] )


# get all values as an iterable with "values()". once again we need to wrap it 
# in list() to get it out of the iterable. note - same as above regarding key 
# ordering.
print(list(filled_dict.keys()))
print(list(filled_dict.keys()))

# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
print(list(filled_dict.values()))  # => [3, 2, 1]  in Python <3.7
print(list(filled_dict.values()))  # => [1, 2, 3] in Python 3.7+

# check for existence of keys in a dictionary with "in"
print("one" in filled_dict)   # => True
print(1 in filled_dict)  # => False

# looking up a non-existing key is a KeyError 
# filled_dict["four"]    # KeyError

# use "get()" method to avoid the keyError 
print(filled_dict.get("one"))  # => 1
print(filled_dict.get("four")) # => None
# the get method supports a default aregument when the value is missing
print(filled_dict.get("one", 5)) # => 1
print(filled_dict.get("four", 4)) # => 4


# "setdefault()" inserts into a dictionary only if the given key isn't present
print(filled_dict.setdefault("five", 5) ) # filled_dict["five"] is set to 5
print(filled_dict.setdefault("five", 6) )  # filled_dict["five"] is still 5

# adding to a dictionary
filled_dict.update({"four":4})
print(filled_dict)
# print(filled_dict["four"] = 4) # another way to add to dict

# remove keys from a dictionery with del
del filled_dict["five"]
print(filled_dict)

# form Python 3.5 you can also use the addition unpacking unpacking option
print({"a": 1, ** {"b":2}}) # => {'a': 1, 'b': 2}
print({"a": 1, ** {"a":2}}) # => {'a': 2}

# Sets store ... well sets 
empty_set = set()
# Initializer a set wiith a buch of values 
some_set = {1,1,2,2,3,4}

# similer to keys of a dictionery, element of a set have to be immutable.
# invalid_set = {[1],1}   # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}
print(valid_set)

# add one more item to the set 
filled_set = some_set
filled_set.add(5)
print(filled_set)# filled_set is now {1, 2, 3, 4, 5}
print(some_set)
filled_set.add(5)
print(filled_set)# it remains as before {1, 2, 3, 4, 5}

# do set intersection with  & 
other_set = {3,4,5,6}
print(filled_set & other_set )

# do set union with |
print(filled_set | other_set)  # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
print({1, 2, 3, 4} - {2, 3, 5})  # => {1, 4}

# Do set symmetric difference with ^
print({1, 2, 3, 4} ^ {2, 3, 5})  # => {1, 4, 5}

# check if set on the left is a superset od set on the right
print({1, 2} >= {1, 2, 3})  # => False

# Check if set on the left is a subset of set on the right
print({1, 2} <= {1, 2, 3})  # => True

# check for existence in a set with in
print(2 in filled_set) # => true
print(10 in filled_set) # => false

# make a one layer deep copy  A set copy is shallow copy.
filled_set.add(8)
print(filled_set)
filled_set =  some_set.copy() # filled_set os {1,2,3,4,5}
filled_set.add(20)
print(filled_set)
print(some_set)
print(filled_set is some_set)

