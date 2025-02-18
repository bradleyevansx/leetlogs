## Linked List Cycle

**Difficulty**: `Easy` - **Tags**: `Linked Lists`, `Cycle Detection`

### Description

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

### Examples

**Example 1:**

**Input**: ```head = [3,2,0,-4], pos = 1```

**Output**: ```true```

### Constraints

- `The number of the nodes in the list is in the range [0, 10^4].`

- `pos is -1 or a valid index in the linked-list.`

### Solution

**Description**:

This problem is a textbook problem. You use two pointers, one that advances twice as fast as the other. The idea is that if there is a cycle eventually the pointers would be running is a circle. If you imagine yourself running is a circle with someone else running at a different spped, eventuall you would meet the other person at the same point. Other wise if you are running in a straight line eventually you would reach the end before the other person if you are the faster one. So iterate through the list until the fast pointer reaches the end or the two pointers meet or the faster one reaches the end.

**Time Complexity**: O(n) - **Space Complexity**: O(1) 

**The Code:**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```