# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        dummy = ListNode(0)
        newList = dummy

        while l1 and l2:
            if l1.val < l2.val:
                newList.next = l1
                l1 = l1.next
            else:
                newList.next = l2
                l2 = l2.next
            newList = newList.next
        if l1:
            newList.next = l1
        else:
            newList.next = l2

        return dummy.next