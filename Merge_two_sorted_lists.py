#Leetcode link: https://leetcode.com/problems/merge-two-sorted-lists/
#Suresh G --> Python3

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = sort_list = ListNode(0)
        
        while(l1 and l2):
            if (l1.val < l2.val):
                sort_list.next = l1
                l1 = l1.next
                sort_list = sort_list.next
                
            elif (l1.val >= l2.val):
                sort_list.next = l2
                l2 = l2.next
                sort_list = sort_list.next

        sort_list.next = l1 or l2
        return head.next
