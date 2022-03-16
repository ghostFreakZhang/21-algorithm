'''
206. 反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case
        if not head or not head.next:
            return head
        # 取得最后一节点
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last