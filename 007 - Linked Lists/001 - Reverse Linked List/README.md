## Reverse Linked List

**Difficulty**: `Easy` - **Tags**: `Linked Lists`

### Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

### Examples

**Example 1:**

**Input**: ```head = [1,2,3,4,5]```

**Output**: ```[5,4,3,2,1]```

### Constraints

- `The number of nodes in the list is the range [0, 5000].`

- `0 <= Node.val <= 1000`

### Solution

**Description**:

This is a textbook problem. You just iterate through the list while setting the next node of the current to the previous one. The return the the node that is last in line.

**Time Complexity**: O(n) - **Space Complexity**: O(1) 

**The Code:**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
```