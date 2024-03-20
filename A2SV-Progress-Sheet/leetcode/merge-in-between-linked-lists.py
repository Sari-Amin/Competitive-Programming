# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        prev = temp 
        cnt = 0
        while temp and cnt != a:
            prev = temp
            temp = temp.next
            cnt += 1
        while temp:
            if cnt == b:
                temp = temp.next
                break
            temp = temp.next
            cnt += 1
      
        prev.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = temp
    
        return list1
        