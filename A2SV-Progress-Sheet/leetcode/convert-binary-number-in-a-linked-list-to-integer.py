# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lenght = 0
        temp = head
        while temp:
            lenght += 1
            temp = temp.next
        temp = head
        ans = 0
        while temp:
            ans += temp.val * 2 ** (lenght - 1)
            lenght -= 1
            temp = temp.next
        return ans
