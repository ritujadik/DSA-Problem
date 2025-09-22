class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


    def add_two_numbers(l1,l2):
        dummy = Node(0)
        current = dummy
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total//10

            dummy.next = Node(total//10)

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

            if carry:
                dummy.next = Node(carry)

        return current