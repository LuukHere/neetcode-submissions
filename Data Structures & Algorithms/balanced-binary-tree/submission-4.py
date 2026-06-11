# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root): #inner depth first search
            if not root: return [True, 0] #0 is still balanced
            left = dfs(root.left) #left height
            right = dfs(root.right) #right height

            balance = (
                left[0] and #checks left side boolean
                right[0] and #checks right side boolean
                abs(left[1] - right[1]) <= 1 #checks to see if the difference in height is <= 1
                )

            return [balance, 1 + max(left[1], right[1])] #sees if inner nodes are balanced at each level and adds them up with dfs
        
        return dfs(root)[0]
        
