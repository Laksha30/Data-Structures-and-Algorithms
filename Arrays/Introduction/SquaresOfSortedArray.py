'''
- Iterate through the nums list
- Replace each element with its square
- Sort the list using any convenient method
- Return the nums list
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = pow(nums[i], 2)
        nums.sort()
        return nums
            