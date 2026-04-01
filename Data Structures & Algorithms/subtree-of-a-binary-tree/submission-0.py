# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        # node = find(root, subRoot.val)
        # if not node:
        #     print("cannot find")
        #     return False
        
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def same(p, q):
    if not p and not q:
        return True
    
    if (p and not q) or (not p and q):
        return False
    
    if p.val != q.val:
        return False
    
    return same(p.left, q.left) and same(p.right, q.right)

def find(root, x):
    if not root:
        return None
    
    if root.val == x:
        return root
    
    if x < root.val:
        return find(root.left, x)
    else:
        return find(root.right, x)
    