"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        copy_dict={}
        copy_dict[head] = Node(head.val)

        placeholder = head
        while head:
            if head.next and head.next not in copy_dict:
                copy_dict[head.next] = Node(head.next.val)
            copy_dict[head].next = copy_dict.get(head.next, None)

            if head.random and head.random not in copy_dict:
                copy_dict[head.random] = Node(head.random.val)
            copy_dict[head].random = copy_dict.get(head.random, None)

            head=head.next
        return copy_dict[placeholder]
        
