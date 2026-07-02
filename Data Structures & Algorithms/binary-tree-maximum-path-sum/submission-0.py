# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def maxSum(root):
            if not root:
                return 0
            
            rootleft = maxSum(root.left)
            rootright = maxSum(root.right)
            rootleft = max(rootleft, 0)
            rootright = max(rootright, 0)

            res[0] = max(res[0], root.val+rootleft+rootright)
            return root.val+max(rootleft, rootright)
        
        maxSum(root)
        return res[0]