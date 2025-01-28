class Stack:
    def __init__(self,n):
        self.stack = []
        self.n=n
    def push(self,p):
        j=len(self.stack)
        if j<self.n:
            self.stack.append(p)
        else:
            print("Stack is full!")
    def pop(self):
        if len(self.stack)==0:
            print("THE STACK IS EMPTY!")
        else:
            self.stack.pop(-1)
    def top(self):
        if len(self.stack)==0:
            print("THE STACK IS EMPTY!")
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def display(self):
        print(self.stack)
#HW
stack=Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.display()
print(stack.top)