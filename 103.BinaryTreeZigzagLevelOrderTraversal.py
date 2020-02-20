class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, level, direction = [], [root], 1
        
        while level:
            ans.append([node.val for node in level][::direction])
            temp = []
            direction *= -1
            for node in level: 
                temp.extend([node.left, node.right]) 
            level = [leaf for leaf in temp if leaf]            
        return ans
