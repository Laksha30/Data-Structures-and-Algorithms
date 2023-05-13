'''
Output: Retrieve the minimum element from the stack

Solution:
1. init -> Initialises the stack variable
2. Push -> Pushes the given 'val' to the stack
3. Pop -> Pops the val in the top of the stack
4. Top -> Returns the val in the top of the stack
5. getMin -> returns the minimum val in the stack 
'''

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()