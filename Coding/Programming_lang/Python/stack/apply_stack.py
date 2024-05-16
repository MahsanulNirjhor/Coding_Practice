from stack import Stack 
# Create a new stack
stack = Stack()

# Push items onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Check the size of the stack
print(stack.size())  # Output: 3

# Peek at the top item
print(stack.peek())  # Output: 3

# Pop items from the stack
print(stack.pop())   # Output: 3
print(stack.size())  # Output: 2

# Check if the stack is empty
print(stack.is_empty())  # Output: False

# Print the stack
print(stack)
