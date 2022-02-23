class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root
        
        left_subtree = self.lowestCommonAncestor(root.left, p, q)
        right_subtree = self.lowestCommonAncestor(root.right, p, q)
        
        # If left subtree contains one of descendant (p or q) and right subtree contains the remaining descendant (q or p) then the root is their LCA.
        if left_subtree and right_subtree:
            return root
        elif left_subtree and (not right_subtree):
            return left_subtree
        else:
            return right_subtree  
