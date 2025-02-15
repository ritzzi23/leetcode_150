from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return None
        
    
    def createTree(self, values: List[int]) -> Optional[TreeNode]:
        """Create a binary tree from a list of values (level-order traversal)."""
        if not values:
            return None
            
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Add left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Add right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
            
        return root
    
    def treeToList(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        """Convert a binary tree to a list (level-order traversal)."""
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
                
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
            
        return result

# Example usage
if __name__ == "__main__":
    root = [1,2,3,4,5,6,7]
    solution = Solution()
    
    # Create the tree from list
    root = solution.createTree(root)
    
    # Invert the tree
    inverted = solution.levelOrder(root)
    
    # Convert back to list for visualization
    result = solution.treeToList(inverted)
    print(f"Original tree: {root}")
    print(f"Inverted tree: {result}")