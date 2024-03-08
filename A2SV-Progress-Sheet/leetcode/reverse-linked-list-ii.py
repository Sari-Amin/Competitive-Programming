# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right:
            return head
        temp = head
        cnt = 1
        reverse = None
        prev = head
        left_prev = prev
        right_temp = None
        while temp:

            if cnt == left:
                if left == 1:
                    left_prev = None
                else:
                    left_prev = prev
            if cnt == right:

                right_temp = temp
                right_temp = right_temp.next
            if cnt <= right and cnt >= left:
                temp1 = temp
                temp = temp.next
                temp1.next = reverse
                reverse = temp1
                cnt += 1
                continue
            prev = temp
            temp = temp.next
            cnt += 1
        
        if left_prev:
            left_prev.next = reverse
        else:
            head = reverse

        temp = reverse
    
        while temp.next:
 
            temp = temp.next

        temp.next = right_temp

        return head