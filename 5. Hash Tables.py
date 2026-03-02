'''Hash Table
A Hash Table is a data structure designed to be fast to work with.

The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for, adding, and deleting data can be done really quickly, even for large amounts of data.

In a Linked List, finding a person "Bob" takes time because we would have to go from one node to the next, checking each node, until the node with "Bob" is found.

And finding "Bob" in an list/array could be fast if we knew the index, but when we only know the name "Bob", we need to compare each element and that takes time.

With a Hash Table however, finding "Bob" is done really fast because there is a way to go directly to where "Bob" is stored, using something called a hash function.

Building A Hash Table from Scratch
To get the idea of what a Hash Table is, let's try to build one from scratch, to store unique first names inside it.

We will build the Hash Table in 5 steps:

Create an empty list (it can also be a dictionary or a set).
Create a hash function.
Inserting an element using a hash function.
Looking up an element using a hash function.
Handling collisions.'''

#Create a Hash Function that sums the Unicode numbers of each character and return a number between 0 and 9:

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))
print("'Alice' has hash code:", hash_function('Alice'))

#The character B has Unicode number 66, o has 111, and b has 98. Adding those together we get 275. Modulo 10 of 275 is 5, so "Bob" should be stored at index 5.


# Steps of hash function 
#Step 1: Create an Empty List
#Step 2: Create a Hash Function
#Step 3: Inserting an Element 
#Step 4: Looking up a name
#Step 5: Handling collisions
my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index] = name

add('Bob')
print(my_list)
add('Alice')
print(my_list)

#Looking up a name
# Now that we have a super basic Hash Table, let's see how we can look up a name from it.

# To find "Pete" in the Hash Table, we give the name "Pete" to our hash function. The hash function returns 8, meaning that "Pete" is stored at index 8. So we can just check if the name at index 8 is "Pete" and if it is, we know that "Pete" is in the Hash Table.

my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index] = name

def contains(name):
  index = hash_function(name)
  return my_list[index] == name

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print("'Pete' is in the Hash Table:", contains('Pete'))