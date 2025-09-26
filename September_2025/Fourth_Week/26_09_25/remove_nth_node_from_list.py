class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def remove_nth_node(head,n):
        dummy = Node(0)
        dummy.next = head
        fast=slow=dummy

        for i in range(n):
            fast = fast.next

            while fast.next:
                slow = slow.next
                fast = fast.next

            slow.next = slow.next.next

        return dummy.next
        