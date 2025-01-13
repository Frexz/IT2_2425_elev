class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Kan ikke fjerne fra en tom stack.")
    
    def peek(self):
        if not self.is_empty(): 
            return self.items[0]
        else:
            print("Kan ikke kikke på første element i en tom stack.")
    
    def is_empty(self):
        if self.items:
            return False
        else:
            return True

    def size(self):
        return len(self.items)

    def __str__(self):
        return "[" + ", ".join(self.items) + "]"

stack = Stack()

# Test 1 - push
print("Test 1".center(40, "-"))
stack.push("Alice")
print(stack)
stack.push("Bob")
print(stack)


# Test 2 - pop
print("Test 2".center(40, "-"))
print(f"Fjernet: {stack.pop()}")
print(stack)
print(f"Fjernet: {stack.pop()}")
print(stack)
stack.pop() # Fjerner fra tom stack

# Test 3 - peek
print("Test 3".center(40, "-"))
stack.push("Alice")
stack.push("Bob")
print(f"Første element er {stack.peek()}")
print(stack)
stack.pop()
stack.pop()
stack.peek() # Kikker på en tom stack

# Test 4 - is_empty
print("Test 4".center(40, "-"))
print(stack.is_empty())
stack.push("Alice")
print(stack.is_empty())

# Test 4 - size
print("Test 5".center(40, "-"))
print(stack.size())
stack.pop()
print(stack.size())
