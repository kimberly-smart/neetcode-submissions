# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def maxlen(root):
            if not root:
                return 0
            
            rootleft = maxlen(root.left)
            rootright = maxlen(root.right)
            self.res = max(self.res, rootleft+rootright)
            return 1+ max(rootleft, rootright)
        maxlen(root)
        return self.res