# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        n = 1
        temp = head
        while temp:
            n += 1 
            temp = temp.next

        temp = head
        ans = ListNode(-1)
        ans_temp = ans
        while n - 1:
            temp = head
            min_ = head
            prev = temp
            min_prev = temp
            while temp:
                if temp.val < min_.val:
                    min_prev = prev
                    min_ = temp
                prev = temp
                temp = temp.next
  
            ans_temp.next = min_
            ans_temp = ans_temp.next
            if head.val == min_.val:
                head = head.next
            elif min_prev and min_prev.next:
                min_prev.next = min_prev.next.next

            n -= 1
        ans_temp.next = None
        return ans.next
