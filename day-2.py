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

