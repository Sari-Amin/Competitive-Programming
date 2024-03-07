# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None

        temp = head

        while temp:
            rev = temp
            temp = temp.next

            rev.next = reverse
            reverse = rev
            
        return reverse