'''
1. Init -> Initialize 2 stacks
2. Push -> Push x into the stack 1
3. Pop -> 
    Pop from stack 1 and push to stack 2
    Ans -> Pop value from stack 2 
    Pop from stack 2 and push to stack 1
4. Peek -> 
    Pop from stack 1 and push to stack 2
    Ans -> Pop value from stack 2 
    Push the value of Ans in stack 1 
    Pop from stack 2 and push to stack 1
5. empty -> If stack 1 is empty, return True; else return False
'''

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()

        while self.stack2:
            self.push(self.stack2.pop())
        return ans
        

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()
        self.stack1.append(ans)
        while self.stack2:
            self.push(self.stack2.pop())
        return ans
        

    def empty(self) -> bool:
        if self.stack1:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()