# Definition for singly-linked list.
from tabnanny import check


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def doubleIt(self, head):
        num_str = ""
        while head:
            num_str += str(head.val)
            head = head.next
        double_num_str = str(int(num_str) * 2)
        dummy = ListNode()
        while double_num_str:
            dummy.next = ListNode(int(double_num_str[0]))
            dummy = dummy.next
            double_num_str = double_num_str[1:]
        return dummy

    def getNum(first, second):
        min_num = min(first, second)
        if first % min_num == 0 and second % min_num == 0:
            return min_num
        num = min_num/2
        while num > 1:
            if first % num == 0 and second % num == 0:
                return num
            else:
                num = num-1
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """




