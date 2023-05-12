'''
Given: Integer n 

Solution: Solving the problem using memoization where we save the recursive value in the memo

1. Initialize the 'memo' dictionary outside the method. 
2. It is noted from the sample that for '1' step we have 1 way and for '2' step we have to 2 ways 
    which could be initialized in the 'memo' itself. 
3. In the method, check if the value of n is present in the 'memo' dictionary
    if yes, return the value of 'n' in 'memo'
4. Else, call the method 'climbStairs' recursively for 'n-1' and 'n-2' values and store in the 'memo' 
    as key-value pair for key as 'n'
5. Return the value of 'memo[n]'. 
    
'''

class Solution:
    memo = {}
    memo[1] = 1
    memo[2] = 2
    
    def climbStairs(self, n: int) -> int:
        if n in Solution().memo:
            return Solution().memo[n]
        
        else:
            Solution().memo[n] = Solution().climbStairs(n-1) + Solution().climbStairs(n-2)
            return Solution().memo[n]