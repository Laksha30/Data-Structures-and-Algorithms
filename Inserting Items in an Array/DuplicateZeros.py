'''
flag -> A variable to flag that 0 has been added and to skip executing the duplicated zero

Logic:
- Initialize flag as 0
- Iterate through the list 
- If arr[i] is 0, 
    - Then make the flag value as 1 
    - Iterate from the last of the array to the value of i+1 using a variable j
    - Copy j-1 value to j
- If flag is 1
    - Then make flag as 0 and continue
'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        flag = 0
        for i in range(len(arr)):
            if flag==1:
                flag = 0
                continue
            else:
                if arr[i]==0:
                    flag = 1
                    for j in range(len(arr)-1, i, -1):
                        arr[j] = arr[j-1]
                
            
            
    
        
        

                
                
        