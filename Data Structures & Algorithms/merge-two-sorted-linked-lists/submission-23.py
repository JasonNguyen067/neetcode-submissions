# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Ill create a dummy node, 
        # We'll have the dummy node as a reference to the start of our merged list
        # And curr can perform actions on it via a reference

        dummy = ListNode()
        curr = dummy

        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next

            curr = curr.next #move curr forward after conncting

        curr.next = head1 if head1 else head2

        # Return dummy.next because dummy is just the node dummy.next is the first value in the new linkedlist
        return dummy.next
