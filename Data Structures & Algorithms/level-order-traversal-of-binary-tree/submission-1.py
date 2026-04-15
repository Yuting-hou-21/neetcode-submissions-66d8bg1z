# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []

        while queue:
            layer = len(queue)
            level = []
            for i in range(layer):
                node = queue.popleft()
                if node:
                    val = node.val
                    level.append(val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(level) > 0:
                res.append(level)

        return res
