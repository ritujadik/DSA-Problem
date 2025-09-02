
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def remove_nth_node(head,n):
        dummy = Node(0)
        dummy.next = head
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

new_head = Node.remove_nth_node(head,2)

current = new_head
while current:
    print(current.val,end="->")
    current = current.next


