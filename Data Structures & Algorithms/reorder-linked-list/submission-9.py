# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # For this we want to be able to reverse the 2nd half of the linked list
        # Cut off the link between the middle 
        # Be able to iterate between the two linked list and reorder it 

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None

        while second:
            nextVal = second.next
            second.next = prev
            prev = second
            second = nextVal

        first = head
        second = prev

        while second:
            firstNextVal = first.next
            secondNextVal = second.next

            first.next = second
            second.next = firstNextVal

            first = firstNextVal
            second = secondNextVal

        