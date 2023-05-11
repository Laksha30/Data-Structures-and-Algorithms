'''
Given: Head -> Head of a linked list 

Consider the linked list: a -> b -> c

Solution:
1. By the given sample test cases of [] and [1], we have to return the same head value 
2. Store the adjacent value to a variable 'temp' as 'head.next' so that 
    'head.next' value could be manipulated and,
    we don't lose the node while relinking
3. Now, head.next node could be relinked to the next node value (as per the consideration example)
    which would be returned the next time we call 'swapPairs' since 'c' has its next as None
4. Now, head.next is equal to 'c' (i.e., a -> c)
5. 'temp' has the value 'b'. Now, link head to temp.next hence becomes b -> a -> c
6. Return 'temp'

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge case
        if head is None or head.next is None:
            return head
        
        
        temp = head.next
        head.next = Solution().swapPairs(temp.next)
        temp.next = head 
        return temp