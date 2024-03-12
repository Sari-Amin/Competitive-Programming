# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,head) 
        lsum = 0
        dic = {lsum:dummy}
        while head:
            lsum += head.val
            if lsum in dic:
                toBeRemoved = dic[lsum].next
                sum_ = lsum
                while toBeRemoved != head:
                    sum_ += toBeRemoved.val
                    del dic[sum_]
                    toBeRemoved = toBeRemoved.next

                dic[lsum].next = head.next
            else:
                dic[lsum] = head

            head = head.next
      
        return dummy.next
        