class node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def reverse_a_link_list(head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return  prev


