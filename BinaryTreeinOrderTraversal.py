# https://leetcode.com/problems/binary-tree-inorder-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        ans = []
        self.recursiveInOrderTraversal(root, ans)
        return ans

    def recursiveInOrderTraversal (self, root, ans): 
        if root is None:
            return     
        self.recursiveInOrderTraversal(root.left, ans)
        ans.append(root.val)
        self.recursiveInOrderTraversal(root.right, ans)
        
        
        
        
    
        