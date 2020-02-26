class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.prev = None

        def dfs(root):
            if not root:
                return None
            dfs(root.right)
            dfs(root.left)
            
            root.right = self.prev
            root.left = None
            self.prev = root
        dfs(root)
