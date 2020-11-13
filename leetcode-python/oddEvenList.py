# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        h = odd =head 
        if h == None:
            return h
        if h: even = h.next
        s = 0
        flag = 0
        while h.next != None:
            s = s + 1
            temp = h.next
            h.next = h.next.next
            if h.next == None and s % 2 == 1:
                flag = 1
                h.next = even
            h = temp
        if flag == 0:
            h.next = even

        return odd



# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         odd = o = ListNode(0)
#         even = e = ListNode(0)

#         h = head
#         ot = 1
#         et = 0
#         while h != None :
#             if ot:
#                 o.next = h
#                 h = h.next
#                 o = o.next
#                 o.next = None
#                 ot = 0
#                 et = 1
#             elif et:
#                 e.next = h
#                 h = h.next
#                 e = e.next
#                 e.next = None
#                 ot = 1
#                 et = 0
#         o.next = even.next
#         return odd.next









# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next






# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         odd = o = ListNode(0)
#         even = e = ListNode(0)

#         h = head
#         ot = 1
#         et = 0
#         while h != None :
#             if ot:
#                 o.next = h
#                 h = h.next
#                 o = o.next
#                 o.next = None
#                 ot = 0
#                 et = 1
#             elif et:
#                 e.next = h
#                 h = h.next
#                 e = e.next
#                 e.next = None
#                 ot = 1
#                 et = 0
#         o.next = even.next
#         return odd.next



