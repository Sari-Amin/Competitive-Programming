# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evens = ListNode(-1)
        odds = ListNode(-1)
        temp1 = evens
        temp2 = odds
        temp = head
        counter = 1
        while temp:
            if counter%2:
                temp2.next = temp
                temp2 = temp2.next
            else:
                temp1.next = temp
                temp1 = temp1.next
            temp = temp.next
            counter += 1
        temp2.next = evens.next
        temp1.next = None
        return odds.next