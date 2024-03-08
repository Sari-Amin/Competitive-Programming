# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(-1)
        greater = ListNode(-1)
        temp2 = less
        temp1 = greater
        temp = head

        while temp:
            if temp.val >= x:
                temp1.next = temp
                temp1 = temp1.next
            else:
                temp2.next = temp
                temp2 = temp2.next
            temp = temp.next

        temp2.next = greater.next
        temp1.next = None
        return less.next

