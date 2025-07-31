from typing import Optional
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution(object):
    def two_merged_ist(self,list1:Optional[ListNode],list2:Optional[ListNode])->Optional[ListNode]:
        result = ListNode(0)
        head = result
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        head.next = list1 if list1 else list2
        return result.next

