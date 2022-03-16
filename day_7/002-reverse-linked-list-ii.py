'''
92. 反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.successor = None

    def reverseN(self, head, n):
        if n == 1:
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head
        # 以 head.next 为起点, 反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        # 反转之后的节点和后面的节点连接起来
        head.next = self.successor
        return last
        
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # base case
        if left == 1:
            return self.reverseN(head, right)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head