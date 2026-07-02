# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            rootleft = dfs(root.left)
            rootright = dfs(root.right)
            rootleft = max(rootleft, 0)
            rootright = max(rootright, 0)
            self.res = max(self.res, rootleft + rootright)

            return 1 + max(rootleft, rootright)
        
        dfs(root)
        return self.res