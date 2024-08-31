from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

### my solution 
def reverseList(head):
    return head[::-1]

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, ListNode(head)
        if curr:
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev.val
        else:
            return curr.val

head = [0,1,2,3]
print(Solution().reverseList(head))
