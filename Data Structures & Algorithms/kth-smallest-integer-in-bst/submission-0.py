# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        inorder(root, order)
        return order[k-1]

def inorder(root, order):
    if not root:
        return 
    
    inorder(root.left, order)
    order.append(root.val)
    inorder(root.right, order)
    
