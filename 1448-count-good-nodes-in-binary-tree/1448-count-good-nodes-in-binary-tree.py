# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque()
        q.append([root, -10001])
        answer =0
        while q:
            node, prior_val = q.popleft()
            if node.val >= prior_val:
                answer +=1
            
            if node.left:
                q.append([node.left, max(node.val, prior_val)])
            if node.right:
                q.append([node.right, max(node.val, prior_val)])

        return answer