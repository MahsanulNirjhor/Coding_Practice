class Stack:
    """
    self allows you to access and modify the attributes (variables) 
    of the current instance of the class.
    """
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pop an item off the stack.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        """
        Returns the top item from the stack without removing it.

        Returns:
            The top item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of items in the stack.
        """
        return len(self.items)
    def __str__(self):

        """
        Returns a string representation of the stack.
        """
        return str(self.items)
