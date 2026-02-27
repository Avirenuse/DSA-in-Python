"""Stacks
A stack is a data structure that can hold many elements, and the last element added is the first one to be removed.

Like a pile of pancakes, the pancakes are both added and removed from the top. So when removing a pancake, it will always be the last pancake you added. This way of organizing elements is called LIFO: Last In First Out.

Basic operations we can do on a stack are:

> Push: Adds a new element on the stack.
> Pop: Removes and returns the top element from the stack.
> Peek: Returns the top (last) element on the stack.
> isEmpty: Checks if the stack is empty.
> Size: Finds the number of elements in the stack.

Stacks can be implemented by using arrays or linked lists.

Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.

Stacks are often mentioned together with Queues, which is a similar data structure described on the next page."""

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))


'''# create a stack class #'''
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())

'''Reasons to implement stacks using lists/arrays:

Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
Easier to implement and understand: Using arrays to implement stacks require less code than using linked lists, and for this reason it is typically easier to understand as well.
A reason for not using arrays to implement stacks:

Fixed size: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements.
In contrast, a linked list can grow and shrink dynamically as needed, which can be more memory efficient in cases where the number of elements is not known in advance or can change frequently. However, linked lists can be more complex to implement and may require more memory per element due to storing additional pointers. In general, the choice between using an array or a linked list to implement a stack depends on the specific requirements of the application, such as memory constraints and the expected number of elements in the stack.'''