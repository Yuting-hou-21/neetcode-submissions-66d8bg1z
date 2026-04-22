# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, biggest):
            if not node:
                return None
            if node.val >= biggest:
                self.res += 1
                biggest = node.val

            dfs(node.left, biggest)
            dfs(node.right, biggest)

        dfs(root, root.val)
        return self.res