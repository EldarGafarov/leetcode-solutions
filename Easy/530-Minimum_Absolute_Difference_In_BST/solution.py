# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        values=[]
        new_value=0
        min_value=100000
        #Function to sort the BST in a list
        def inorder(node):
            if node is None:
                return
            inorder(node.left)         
            values.append(node.val)    
            inorder(node.right)
        inorder(root)
        for i in range(len(values)-1):
            new_value = values[i+1]-values[i]
            if new_value < min_value:
                min_value = new_value

        return min_value