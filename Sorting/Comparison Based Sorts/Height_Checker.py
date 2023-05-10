'''
Given: heights -> Array

Solution: Using Bubble sort
1. Initialize 'expected' array as a copy of 'heights' array
2. Iterate through the 'expected' array using a variable 'i' to count the number of steps
3. Iterate through the 'expected' array using a variable 'j' to compare adjacent elements of the 'expected' array
4. Swap the adjacent elements if the first is greater than the second 
5. Initialize the 'count' variable to 0
6. Iterate through the array using a variable 'i'
7. If the element of index 'i' of array 'expected' and 'heights', 
    then increment the value of count to 1 
8. Return the 'count' variable. 
'''


class Solution:
    def heightChecker(self, heights) -> int:
        expected = heights.copy()
        
        for i in range(len(expected)-1):
            for j in range(len(expected)-1):
                if expected[j] > expected[j+1]:
                    expected[j], expected[j+1] = expected[j+1], expected[j]
                
        count = 0
        for i in range(len(expected)):
            if heights[i] != expected[i]:
                count += 1
                
        return count
        