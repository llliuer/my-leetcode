# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        h1f = head
        h1 = head.next
        while h1 != None:
            # print(h1.val)
            h2f = None
            h2 = head
            while h2 != h1:
                # print(h2.val)
                if h2.val < h1.val:
                    flag = 0
                    h2 = h2.next
                    if h2f == None:
                        h2f = head
                    else:
                        h2f = h2f.next
                else:
                    # 将h1放到h2前
                    # ->h2->
                    # ->h1->

                    temph1 = h1.next
                    temph1f = h1f
                    flag = 1
                    if h2f == None:
                        h1f.next = h1.next
                        head = h1
                        h1.next = h2

                    else:
                        h1f.next = h1.next
                        h2f.next = h1
                        h1.next = h2

                    break
            if flag == 0:
                h1f = h1f.next
                h1 = h1.next
            else :
                h1 = temph1
                h1f = temph1f
        return head


l = [2,1,3]
head = ListNode(4)
h = head
for i in l:
    newnode = ListNode(i)
    h.next = newnode
    h = h.next

S = Solution()
S.insertionSortList(head)