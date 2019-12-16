class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        stack = [(root, "")]
        res = []
        
        if not root:
            return []
        
        while stack:
            node, strr = stack.pop()
            if not node.left and not node.right:
                res.append(strr + str(node.val))
            if node.left:
                stack.append((node.left, strr + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, strr + str(node.val) + "->"))
        return res
