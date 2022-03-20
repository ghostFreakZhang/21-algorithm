'''
114. 二叉树展开为链表

给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历位置
        # 1、左右子树已经被拉平成一条直线
        left = root.left
        right = root.right
        # 2、将左子树作为右子树
        root.left = None
        root.right = left
        # 3、将原先的右子树拼接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right