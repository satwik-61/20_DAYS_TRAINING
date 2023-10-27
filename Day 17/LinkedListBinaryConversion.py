# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr=head
        s=''
        while curr:
           s+=str(curr.val)
           curr=curr.next
        return int(s,2)
                
            

        
        