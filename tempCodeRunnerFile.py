
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