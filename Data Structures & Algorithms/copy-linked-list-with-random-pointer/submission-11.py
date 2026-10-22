"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyToNew = {None:None}
        curr = head

        while curr:
            copyToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = copyToNew[curr]
            copy.next = copyToNew[curr.next]
            copy.random = copyToNew[curr.random]
            curr = curr.next

        return copyToNew[head]
        