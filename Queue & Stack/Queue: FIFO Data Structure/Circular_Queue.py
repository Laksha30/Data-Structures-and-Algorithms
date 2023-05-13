'''
1. Init 
    - Initializes the Queue with size k and its values as None
    - Size of queue is k
    - head and tail in the same place as -1

2. Enqueue
    - If queue is full, return False
    - If queue is empty, move head pointer to 0
    - For the tail pointer,
        Move the tail pointer + 1 (use mod size to make sure that we don't exceen size of queue)
    - Assign the value to the incremented tail index in the queue
    - Once the value is assigned, return True

3. deQueue
    - If queue is empty, return False
    - If head and tail are in the same position (only one element in the queue), 
        set head and tail to -1
        return True
    - Normal case, increment the head pointer by 1 and mod size 
        return True

4. Front
    - If queue is empty, return False
    - Else, return queue[head]

5. Rear
    - If queue is empty, return -1
    - Else return queue[tail]

6. isEmpty
    - If head == -1, return True
    - Else return False

7. isFull
    - If tail is behind head, i.e., (tail + 1) % size == head, return True
    - Else return False
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.size = k
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        
        self.head = (self.head + 1) % self.size
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]
        

    def isEmpty(self) -> bool:
        return self.head == -1
        

    def isFull(self) -> bool:
        return ((self.tail+1) % self.size) == self.head
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()