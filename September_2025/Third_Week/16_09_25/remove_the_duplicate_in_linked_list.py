"""
Remove a duplicate from sorted linked list
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


    def remove_duplicate(head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next

            else:
                current = current.next

        return head


