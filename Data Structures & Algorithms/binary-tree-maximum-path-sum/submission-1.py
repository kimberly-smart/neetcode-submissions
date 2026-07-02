# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def maxval(curr):
            if not curr:
                return 0
            
            currleft = maxval(curr.left)
            currright = maxval(curr.right)
            currleft = max(0, currleft)
            currright = max(0, currright)

            res[0] = max(res[0], curr.val + currleft + currright)

            return curr.val + max(currleft, currright)
        
        maxval(root)
        return res[0]