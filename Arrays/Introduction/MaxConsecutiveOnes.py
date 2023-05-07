'''
count -> Counts the consecutive ones
maxi -> Stores the maximum of the count 

Logic: 
- The nums list is iterated till the end
    - If the value of the iterator is 1, 
        - then count is incremented by 1
    - If value of the iterator is 0,
        - The already existing value in the maxi variable is compared with the count variable and 
          the maximum of of the both is stored in maxi variable 
        - The count variable is reset to 0
- The maxi variable is updated again with the count 
  (Case when the last value of the given list is 1 
  since the program doesn't get to update the maximum for the last consecutive ones if it exists)
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, maxi = 0, 0
        for i in nums:
            if i == 1:
                count += 1  
            else:
                maxi = max(count, maxi)
                count = 0
        maxi = max(count, maxi)
        return maxi