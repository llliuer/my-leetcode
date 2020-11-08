/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return head
    }

    var pre *ListNode
    pre = head
    nex := head.Next
    head = head.Next 
    pre.Next = nil
    
    
    for nex != nil{//要保存一个指向前一个节点的指针
        nex = head.Next
        head.Next = pre
        pre = head
        head = nex
    }
    return pre
}
