class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def merged_two_linked_list(l1,l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2
        return  tail.next

