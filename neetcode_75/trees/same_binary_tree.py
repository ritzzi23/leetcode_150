from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val :
            return False
        return (self.isSameTree(p.left,q.left) and
        self.isSameTree(p.right,q.right))

        

    
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
    p_vals = [4, 7]
    q_vals = [4, None, 7]
    solution = Solution()

    p = solution.createTree(p_vals)
    q = solution.createTree(q_vals)

    same = solution.isSameTree(p, q)

    print(f"Tree p (list): {solution.treeToList(p)}")
    print(f"Tree q (list): {solution.treeToList(q)}")
    print(f"Are the trees the same? {same}")
