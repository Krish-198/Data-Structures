class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size

    def enqueue(self, j):
        if self.available == 0:
            print("Queue Overflow!")
        else:
            self.queue[self.rear] = j
            self.rear = (self.rear + 1) % self.size
            self.available -= 1

    def dequeue(self):
        if self.available == self.size:
            print("Queue Underflow!")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1

    def peek(self):
        print(self.queue[self.front])

    def getrear(self):
        print(self.queue[self.rear])

    def display(self):
        print(self.queue)

def add_queues(queue1,queue2):

    if queue1.size != queue2.size:
        raise ValueError("Queues must be of the same length")
        
    result_queue = Queue(queue1.size)
    
    for i in range(queue1.size):
        val1 = queue1.queue[i]
        val2 = queue2.queue[i]
        
        
        result_queue.enqueue(val1 + val2)
        
    return result_queue
queue_a = Queue(5)
queue_b = Queue(5)

queue_a.enqueue(1)
queue_a.enqueue(2)
queue_a.enqueue(3)
queue_a.enqueue(4)
queue_a.enqueue(5)

queue_b.enqueue(4)
queue_b.enqueue(5)
queue_b.enqueue(6)
queue_b.enqueue(7)
queue_b.enqueue(8)

summed_queue = add_queues(queue_a, queue_b)
summed_queue.display()