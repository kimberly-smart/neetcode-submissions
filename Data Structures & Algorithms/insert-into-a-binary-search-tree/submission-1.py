# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        r = root
        while True:
            if val<r.val:
                if not r.left:
                    r.left = TreeNode(val)
                    return root
                r = r.left
            else:
                if not r.right:
                    r.right = TreeNode(val)
                    return root
                r = r.right
        return root