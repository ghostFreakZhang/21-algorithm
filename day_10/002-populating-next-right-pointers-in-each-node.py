'''
116. 填充每个节点的下一个右侧节点指针

给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        self.connect_two(root.left, root.right)
        return root
    # 辅助函数
    def connect_two(self, node1, node2):
        if not node1 or not node2:
            return
        # 前序遍历位置, 连接传入的两个节点
        node1.next = node2
        # 连接相同父节点的两个子节点
        self.connect_two(node1.left, node1.right)
        self.connect_two(node2.left, node2.right)
        # 连接跨父节点的两个子节点
        self.connect_two(node1.right, node2.left)