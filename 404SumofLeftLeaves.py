class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, direction = ''):
            if not root:
                return 0
            
            if not root.left and not root.right:
                if direction == 'left':
                    return root.val
                
            left, right = 0, 0
            if root.left:
                left = helper(root.left, 'left')
            if root.right:
                right = helper(root.right, 'right')
            return left + right
        
        return helper(root, '')
