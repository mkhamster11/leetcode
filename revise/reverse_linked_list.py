
from typing import Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    


def reversed_linklist(head:ListNode):
    prev,curr = None,ListNode(head)
    # print("entry",curr.next,curr.val,prev)

    if curr:
        while curr:
            pass    
            # print("in while",curr.next,curr.val,prev)
            # temp = curr.next
            # print("in while >",curr.next,curr.val,prev)
            # curr.next = prev
            # print("in while >>",curr.next,curr.val,prev)
            # prev = curr
            # print("in while >>>",curr.next,curr.val,prev)
            # curr = temp
            # print("in while enddd",curr,prev,temp)

head = [0,1,2,3]

# [3,2,1,0]
print(reversed_linklist(head))