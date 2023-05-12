'''
Given: An integer 'n' 

Concept: 
Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
5th element of Fibonacci sequence is 
Fib(5) = Fib(4) + Fib(3) = (Fib(3) + Fib(2)) + (Fib(2) + Fib(1)) 
       = ((Fib(2) + Fib(1)) + Fib(2)) + (Fib(2) + Fib(1))
       = 1 + 1 + 1 + 1 + 1
       = 5 

Solution: 
1. If n is 0, return 0
2. If n is 1 or 2, return 1
3. Return the sum of recursive calling of the function Fib with 'n-1' and 'n-2' values. 
'''

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n <= 2:
            return 1 
        
        return Solution().fib(n-1) + Solution().fib(n-2)
    
