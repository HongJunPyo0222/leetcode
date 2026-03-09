# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getSize(self, head):
        count = 0
        
        while head.next:
            count +=1
            head = head.next
        
        return count
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        original = head
        targetIndex = (self.getSize(head)+1)// 2
        
        if self.getSize(head) == 0:
            return None

        print(targetIndex)
        for _ in range(targetIndex - 1):
            head = head.next

        head.next = head.next.next

        return original
        