# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return same(p, q)

def same(p,q):
    if not p and not q:return True
    if p is None and q is None:return True
    if (p and not q) or (not p and q):
        return False
    # if (p.left and not q.left) or (not p.left and q.left) or (p.right and not q.right) or (not p.right and q.right):
    #     return False
    # print(p.left is None, p.right is None)
    if p.val != q.val:
        return False
    
    return same(p.left, q.left) and same(p.right, q.right)
