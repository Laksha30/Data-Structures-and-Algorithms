'''
Given: List s

Solution: 
1. Use default argument for index 'i' in the method
2. Swap the element at the index 'i' with 'n-i-1' and vice-versa where 'n' is the length of 's'
3. Recursively call the function 'reverseString' with 's' and 'i+1' 
4. Follow step 3 until the base condition satisfies 'i' equals to n/2 and return. 
'''

class Solution:
    def reverseString(self, s, i=0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if i == len(s)//2:
            return 
        
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        Solution().reverseString(s, i+1)
        


        