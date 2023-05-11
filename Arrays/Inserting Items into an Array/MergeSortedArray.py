'''
i -> Iterator for nums1 list
j -> Iterator for nums2 list 

Logic:
- Iterate the nums1 and nums2 lists using the i and j variable with m and n as length of the respective lists
- If nums1[i] < nums2[j]
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        while (i<m+n and j<n):
            if nums1[i]<nums2[j]:
                if (nums1[i]==0 and i>nums1.index(max(nums1))) or (nums1[i]==0 and m==0):
                    for rest in range(i,m+n):
                        nums1[rest] = nums2[j]
                        j=j+1
                else:
                    pass   
                    
            elif nums1[i]>=nums2[j]:
                for k in range(m+n-1, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                j=j+1
            
            i=i+1
                
                
            