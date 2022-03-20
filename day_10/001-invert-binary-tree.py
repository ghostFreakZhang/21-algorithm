'''
226. 翻转二叉树

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
'''

'''
解决二叉树类的问题，要搞清楚当前root节点，应该做什么以及什么时候做。
针对该题目，要翻转二叉树所有结点的值，就把每个节点的左右值翻转。
也就是说，针对当前root节点，需要交换左右节点；
至于什么时候做，在先序或者后序的位置都可以。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if not root:
            return
        # 先序遍历位置，交换两个节点值，然后递归的交换所有节点的左右位置
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root