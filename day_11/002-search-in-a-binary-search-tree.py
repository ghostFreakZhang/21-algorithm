'''
700. 二叉搜索树中的搜索

给定二叉搜索树（BST）的根节点 root 和一个整数值 val。

你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。

输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]
'''

'''
注意 return
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        # 去左子树查找
        if root.val > val:
            return self.searchBST(root.left, val)
        # 去右子树查找
        if root.val < val:
            return self.searchBST(root.right, val)
        return root