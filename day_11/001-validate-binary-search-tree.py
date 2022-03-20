'''
98. 验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

输入：root = [2,1,3]
输出：true
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 限定以 root 为根的子节点, 必须满足 max.val > root.val > min.val
        def helper(root, min, max):
            # base case
            if not root:
                return True
            # 若 root.val 不符合 max 和 min 的限制，则不是合法的 BST
            if max and root.val >= max.val: return False
            if min and root.val <= min.val: return False
            # 限定左子树的最大值为root.val, 右子树的最小值为root.val
            return helper(root.left, min, root) and helper(root.right, root, max)
        return helper(root, None, None)