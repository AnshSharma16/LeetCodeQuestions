# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
          def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            carry = 0
            result = ListNode(0)
            temp = result
            
            while l1 is not None or l2 is not None:
                if l1 is not None:
                    carry += l1.val
                    l1 = l1.next
                if l2 is not None:
                    carry += l2.val
                    l2 = l2.next
                temp.next = ListNode(carry % 10)
                temp = temp.next
                carry = carry // 10
            
            if carry == 1:
                temp.next = ListNode(carry)
            
            return result.next
