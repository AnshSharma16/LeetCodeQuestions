# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        cur =head
        count=0
        while cur:
            if cur.val in nums:
                count+=1
                while cur and cur.val in nums:
                    cur=cur.next
            else:
                cur=cur.next
        return count