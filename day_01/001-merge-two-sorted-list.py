'''
21. 合并两个有序链表

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
'''

# 注意使用虚拟头节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 虚拟头节点
        dummy = ListNode()
        p = dummy
        p1, p2 = list1, list2
        while p1 and p2:
            # 比较 p1 和 p2
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        if p1:
            # p1 还有剩余
            p.next = p1
        if p2:
            # p2 还有剩余
            p.next = p2
        # 返回虚拟头节点下一个
        return dummy.next