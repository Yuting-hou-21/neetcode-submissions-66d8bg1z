# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        Pqueue = deque([p])
        Qqueue = deque([q])

        while Pqueue and Qqueue:
            Player, Qlayer = len(Pqueue), len(Pqueue)
            if Player != Qlayer:
                return False
            for i in range(Player):
                Pnode, Qnode = Pqueue.popleft(), Qqueue.popleft()
                Pval = Pnode.val if Pnode else -1
                Qval = Qnode.val if Qnode else -1
                if Pval != Qval:
                    return False
                if Pnode:
                    Pqueue.append(Pnode.left)
                    Pqueue.append(Pnode.right)
                    
                if Qnode:
                    Qqueue.append(Qnode.left)
                    Qqueue.append(Qnode.right)
                    

        if len(Pqueue) + len(Qqueue) > 0:
            return False

        return True
                
            