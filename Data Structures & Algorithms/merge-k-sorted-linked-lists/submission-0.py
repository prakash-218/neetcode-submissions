import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Wrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode(0)
        tmp = head
        for l in lists:
            heapq.heappush(heap, (l.val, Wrapper(l)))

        while heap:
            ele, node = heapq.heappop(heap)
            tmp.next = ListNode(ele)
            tmp = tmp.next
            if node.node.next:
                heapq.heappush(heap, (node.node.next.val, Wrapper(node.node.next)))
        return head.next
