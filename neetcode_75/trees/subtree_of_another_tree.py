from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Time: O(m * n)
#Space: O(m + n)

class Solution:   
    def isSameTree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
            
        return (self.isSameTree(root.left,subRoot.left) and
                     self.isSameTree(root.right,subRoot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or
         self.isSubtree(root.right,subRoot))


        

    
    def createTree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """Create a binary tree from a list of values (level-order traversal)."""
        if not values:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)

            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

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

        while result and result[-1] is None:
            result.pop()

        return result

if __name__ == "__main__":
    root = [1,2,3,4,5,null,null,6] 
    subRoot = [2,4,5]
    solution = Solution()

    p = solution.createTree(root)
    q = solution.createTree(subRoot)

    same = solution.isSubtree(p, q)

    print(f"Tree p (list): {solution.treeToList(p)}")
    print(f"Tree q (list): {solution.treeToList(q)}")
    print(f"Is it a subroot? {same}")
