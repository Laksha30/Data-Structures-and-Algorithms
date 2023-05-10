'''
Given: head of the linked list 

Solution: 
1. Input the elements of the linked list in a list 
2. Sort the list using Insertion sort by the following steps:
    1. Traverse the list from the index 1 to the end of the list
    2. Initialise the 'var' variable with the value of 'i'
    3. Iterate backwards from i to 0
    4. If the value of the element in index 'var' is less than its previous index
        then, swap the 'var' index with the previous element to it
3. Replace the elements of the list back to the linked list 
4. Return the head of the linked list
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        h = head
        arr = []
        while h:
            arr.append(h.val)
            h = h.next
            
        #print(arr)
        
        for i in range(1,len(arr)):
            var = i
            while var != 0 and arr[var] < arr[var-1]:
                arr[var], arr[var-1] = arr[var-1], arr[var]
                var -= 1
                
        h = head
        for i in range(len(arr)):
            h.val = arr[i]
            h = h.next
        
        return head