# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        curr = head
        inf = float('inf')
        while list1 or list2:

            one = list1.val if list1 else inf
            two = list2.val if list2 else inf

            if one < two:
                curr.next = ListNode(one)
                list1 = list1.next
            else:
                curr.next = ListNode(two)
                list2 = list2.next
            curr = curr.next
        return head.next
