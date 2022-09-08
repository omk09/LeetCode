"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = [] 
        self.preOrderTraversal(ans, root)
        return ans
        
        
        
    def preOrderTraversal(self, ans, root):
        
        if root is None:
            return 
    
        ans.append(root.val)
        for child in root.children:
            self.preOrderTraversal(ans, child)
            
        return