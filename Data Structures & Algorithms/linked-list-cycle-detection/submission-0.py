# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        if not slow:
            return False
        if fast.next and fast.next.next:
            fast = fast.next.next
        else:
            return False

        while slow != fast:
            if not slow or slow.next == None:
                return False
            if not fast or fast.next == None or (fast.next != None and fast.next.next == None):
                return False
            slow = slow.next
            fast = fast.next.next
        print(slow.val, fast.val)
        return True 
            