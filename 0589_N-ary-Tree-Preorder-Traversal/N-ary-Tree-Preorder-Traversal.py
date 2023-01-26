"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        preorder = []
        stack = [root]

        while stack:
            popped = stack.pop()
            preorder.append(popped.val)
            stack.extend(popped.children[::-1])
        
        return preorder
