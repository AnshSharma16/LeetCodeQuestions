# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        temp=head
        length=0
        while temp:
            temp=temp.next
            length+=1


        if length==n:
            return head.next
            
        temp=head
        remove=length-n
        count=0
        while temp:
            count+=1
            if count==remove:
                temp.next=temp.next.next 
                break
            temp=temp.next
        return head
      
