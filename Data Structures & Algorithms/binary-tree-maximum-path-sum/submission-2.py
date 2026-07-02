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
            
            curleft = maxSum(root.left)
            curright = maxSum(root.right)
            curleft = max(curleft, 0)
            curright = max(curright, 0)

            res[0] = max(root.val + curleft + curright, res[0])
            return root.val + max(curleft, curright)
        
        maxSum(root)
        return res[0]

            