'''
111. 二叉树的最小深度

给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

输入：root = [3,9,20,null,null,15,7]
输出：2
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        # root 本身就是一层
        step = 1
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                # 判断是否到达终点
                if cur.left is None and cur.right is None:
                    return step
                # 将 cur 的相邻节点加入队列
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # 增加步数
            step += 1