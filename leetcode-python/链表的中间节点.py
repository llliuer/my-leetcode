

# 876. 链表的中间结点
# https://leetcode-cn.com/problems/middle-of-the-linked-list/
#
# 总结：
#    1. 快慢指针从头一起起步时，两个中间结点，则返回第二个中间结点。
#    2. 当快指针从慢指针后一个节点起步时，两个中间结点，则返回第一个中间结点。前面那个中间节点
#
#   **链表归并时，采取的就是后者
#
#




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        s = f = head
        while not (f == None or f .next == None):
            s = s.next
            f = f.next.next
        return s