# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # If subRoot is NULL then it exists in child
        if not root: return False # If root is NULL there is no way for subtree to be in it

        if self.sameTree(root, subRoot): # If they are the same tree
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) # Recursively runs through nodes to check if it equals subRoot

    def sameTree(self, s, t):
        if not s and not t: return True # NULL == NULL
        if s and t and s.val == t.val: # IF s and t are NOT NULL AND values are the same
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)) # recursively runs through both trees to see if they're equal
        return False
