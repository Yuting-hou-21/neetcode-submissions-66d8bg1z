# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(curr) -> int:
            if not curr: return 0

            leftheight = dfs(curr.left)
            rightheight = dfs(curr.right)
            D = leftheight + rightheight

            self.res = max(self.res, D)
            return 1 + max(leftheight, rightheight)
        
        dfs(root)
        return self.res