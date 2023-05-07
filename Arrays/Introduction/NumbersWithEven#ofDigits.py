'''
count -> To count the number of even digit numbers

Logic: 
- Iterate through the nums list 
- Convert each number to a string
- If each of the number lengths is divisible by 2, then increment count by 1
- At the end return count 
'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if (len(str(i)))%2==0:
                count+=1
        return count