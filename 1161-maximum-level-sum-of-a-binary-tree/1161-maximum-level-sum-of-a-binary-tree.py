# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque()
        q.append([root, 0])
        existLevel = []
        sumTree = []
        while q:
            node, level = q.popleft()


            if level in existLevel:
                sumTree[level] += node.val
            else:
                existLevel.append(level)
                sumTree.insert(level, node.val)
            
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])
        
        print(sumTree)

        return sumTree.index(max(sumTree)) +1
