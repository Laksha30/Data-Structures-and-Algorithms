'''
1. Init -> Initialize 2 queues
2. Push -> Push x into the queue 1
3. Pop -> 
    Pop(0) from queue 1 and push to queue 2
    Ans -> Pop value from queue 2 
    Pop(0) from queue 2 and push to queue 1
4. Top -> 
    Pop(0) from queue 1 and push to queue 2
    Ans -> Pop value from queue 2 
    Push the value of Ans in stack 1 
    Pop from queue 2 and push to queue 1
5. empty -> If queue 1 is empty, return True; else return False
'''

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x: int) -> None:
        self.queue1.append(x)
        

    def pop(self) -> int:
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        ans = self.queue1.pop(0)
        
        while self.queue2:
            self.push(self.queue2.pop(0))
        return ans
        

    def top(self) -> int:
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        ans = self.queue1.pop(0)
        
        while self.queue2:
            self.push(self.queue2.pop(0))
        self.push(ans)
        return ans
        

    def empty(self) -> bool:
        while self.queue1:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()