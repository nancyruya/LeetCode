class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        output = []
        
        self.InOrderTraversal(root, output)
        min_abs = float('inf')
        
        for i in range(1, len(output)):
            min_abs = min(min_abs, output[i] - output[i-1])
        return min_abs
            
    def InOrderTraversal(self, root, output):
        if root == None:
            return
        else:
            self.InOrderTraversal(root.left, output)
            output.append(root.val)
            self.InOrderTraversal(root.right, output)
