'''
450. 删除二叉搜索树中的节点

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。

输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
'''

'''
删除时，需要考虑的情况比较多：
1、目标节点无子节点
2、目标节点只有一个子节点
3、目标节点有左右两个子节点，也最复杂，需要将左子树的最大节点或者右子树的最小节点替换掉目标节点
    下面的解法是将右子树的最小节点替换为目标节点解决的。
    更细致的是，不要只是替换最小节点与目标节点的val值，而是进行完整的节点替换（因为节点中可能定义了复杂的结构）
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            # 处理目标节点无子节点以及只有一个子节点情况
            if not root.left: return root.right
            if not root.right: return root.left
            # 处理目标节点左右子节点都不为空情况
            # 获取右子树的最小节点
            minNode = self.getMin(root.right)
            # 删除右子树的最小节点
            root.right = self.deleteNode(root.right, minNode.val)
            # 用右子树的最小节点替换 root 节点
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def getMin(self, root):
        while root.left: root = root.left
        return root