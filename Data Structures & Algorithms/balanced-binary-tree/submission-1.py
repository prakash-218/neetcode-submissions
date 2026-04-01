# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return helper(root) 

def helper(root):
    if not root:
        return True
    # if not root or ( not root.left and not root.right):
    #     return 0
    
    # left = helper(root.left) + 1
    # right = helper(root.right) + 1

    # return 2 if abs(left - right) > 1 else 0
    left = height(root.left)
    right = height(root.right)
    return abs(left - right) <= 1 and helper(root.left) and helper(root.right)

def height(root):
    if not root:
        return 0
    
    return 1 + max(height(root.right), height(root.left))
    
    
        