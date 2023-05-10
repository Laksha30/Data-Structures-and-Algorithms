'''
Given:  nums -> Array

Solution: Solved using Selection Sort
1. Iterate through the array nums using a variable 'i' to denote the current element
2. Assume that element of index 'i' to be the minimum of the array and store in a variable named 'min_array'
3. Iterate through the rest of the array from the element after the index 'i' using a variable 'j'
4. If the element of index 'j' is less than element of 'min_index', 
    then initialize 'min_index' to 'j' 

5. Swap the elements of the index 'i' and 'min_index'
'''


class Solution:
    def sortColors(self, nums) -> None:
        #Do not return anything, modify nums in-place instead.
        for i in range(len(nums)-1):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j]<nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        

            
        

                    