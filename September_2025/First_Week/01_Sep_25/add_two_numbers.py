"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
"""
Ex-1 l1 = [2,4,3],l2=[5,6,4]
output = [7,0,8]
explanation = 342 + 465 = 807

Ex-2 L1= [0],l2=[0]
output = [0]

Ex-3 L1 = [9,9,9,9,9,9,9],L2=[9,9,9,9]
output = [8,9,9,9,0,0,1]
"""

# the number of nodes in each linked list is in the range [1,100]
# 0<=Node.val<=9
# it is guaranteed that the list represents a number that does not have leading zeros


class node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def add_two_number(self,l1,l2):
       dummy = node(0)
       current = dummy
       carry = 0

       while l1 or l2 or carry:
           val1 = l1.val if l1 else 0
           val2 = l2.val if l2 else 0

           total = val1 + val2 + carry

           carry = total//10

           current.next = node(total%10)

           current = current.next

           if l1:
               l1 = l1.next
           if l2:
               l2 = l2.next

       return dummy.next


l1 = node(2)
l1.next = node(4)
l1.next.next = node(5)

l2 = node(4)
l2.next = node(5)
l2.next.next = node(6)


sol = node(0)
result = sol.add_two_number(l1,l2)

while result:
    print(result.val,end=" -> " if result.next else "\n")
    result = result.next
