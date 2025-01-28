 # type: ignore
class Queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.front=0
        self.rear=0
        self.size=size
        self.availiable=size
    def enqueue(self,j):
        if self.availiable==0:
            print("Queue Overflow!")
        else:
            self.queue[self.rear]=j
            self.rear=(self.rear+1)%self.size
            self.availiable-=1
    def dequeue(self):
        if self.availiable==self.size:
            print("Queue Underflow!")
        else:
            self.queue[self.front]=None
            self.front=(self.front+1)%self.size
            self.availiable+=1
    def peek(self):
        print(self.queue[self.front])
    def getrear(self):
        print(self.queue[self.rear])
    def display(self):
        print(self.queue)


queue=Queue(3)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.dequeue()
queue.getrear()
queue.peek()
queue.display()
