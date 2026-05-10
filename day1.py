name = "mohd"
age = 22
is_developer = True

print(f"my name is {name}")
print(f"i am a developer: {is_developer}")

# Math is what you would expect
print(1 + 1)  # => 2
print(8 - 1)   # => 7
print(10 * 2)  # => 20
print(35 / 5)  # => 7.0

# Floor division rounds towards negative infinity
print(5 // 3)       # => 1
print(-5 // 3)      # => -2
print(5.0 // 3.0)   # => 1.0  # works on floats too
print(-5.0 // 3.0)  # => -2.0


# The result of division is always a float
# print(10.0 / 3)  # => 3.3333333333333335

#  modulo operator gives the remainder of the division
print(7%3) # => 1
# i % j hane same sigh an j ,, unlike floats too
print(-7%3) # => 2

# exponentiation operator
print(2**3) # => 8
print(3**2) # => 9

 # enforce precedence with parentheses
print(1 + 3 *2 ) # => 7
print((1+3)*2) # => 8

# Bollen values are primitives (note: the capitalization matters)
print(True)  # => True
print(False) # => False

# none, 0, and empty string/list/dicts/tuples/sets all evaluate to false.
# All other values evaluate to true.
print(bool(0)) # => false
print(bool("")) # => false
print(bool([])) # =>  false
print(bool({}))  # => flase
print(bool(())) # => false
print(bool(set()))  # => false
print(bool(4)) # => true
print(bool("hello")) # => true
print(bool(-12)) # => true

# using boolen logic oprators on ints casts them to boolenans for evaluation, but there non-cast value is returned. don't mix up with bool(ints) and bitwise and/or (&,|)
print(bool(0 and 1)) # => false
print(bool(0)) # => false
print(bool(2)) # => true
print(0 and -2) # => 0
print(bool(-5)) # => true
print(bool(2)) # => true
print(0 or 8) # => -5


# equal is
print(1==2) # => false
print(1 == 1)# => true

print(1 != 1) # => false
print(2 != 1) # => true

# more comparision/
print(1<10)# => true
print(1 > 10)# => false
print(2<=2)# => true
print(2>= 2) # => true

# seeing wether a value is in a range
print( 1<2 and 2<3)# =>true 
print(2<3 and 3<2)# =>false

# chaining makes this look nicer
print(1<2<3)# => true
print(2<3<2)# =>false

# (is vs. ==) is check if two variables refer to the same object, but == checks if the objects pointed to have the same values.
a = [1,2,3,4]
b = a
print(b is a)# => true 
print(b == a)# => true
b = [1,2,3,4]
print(b is a)# => false
print(b == a)# => true


# String are create d with " or '
print("this is string") # => this is string
print('this is also a string') # => this is also a string


# String can be added
print("Hello "+ "world")#=>Hello world
# string literals (but not cariables) can be concatenated without using '+'
print("hello " "world!")# =>hello world!


# A string can be treated like a list of characters
print("Hello world!"[0]) # => 'H'


# you can be find the length of string
print(len("hello worls0")) # => 12

# since python 3.6 you can use f-string or formatted string literals

name = "reho"
print(f"she sais her name is {name}") # => she sais her name is reho

# any valid python expression inside these braces is returned to the string.
print(f"{name} is {len(name)} characters long.") # => reho is 4 characters long.

# None is an object
print(None)  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
print("etc" is None)  # => False
print(None is None)   # => True