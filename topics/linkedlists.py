from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import Topic


linkedlists = Topic(
    "Linked Lists",
    "",
    [],
    "",
    [
        Problem(
            "206",
            "Reverse Linked List",
            '''Given the head of a singly linked list, reverse the list, and return the reversed list.''',
            "https://leetcode.com/problems/reverse-linked-list/",
            "Easy",
            ["Linked Lists"],
            [Example("head = [1,2,3,4,5]","[5,4,3,2,1]")],
            [Constraint("The number of nodes in the list is the range [0, 5000]."), Constraint("0 <= Node.val <= 1000")],
            Solution(
                '''# Definition for singly-linked list.
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
        return prev''',
                "This is a textbook problem. You just iterate through the list while setting the next node of the current to the previous one. The return the the node that is last in line.",
                "O(n)",
                "O(1)",
            ),
        ),
        Problem(
            "141",
            "Linked List Cycle",
            '''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.''',
            "https://leetcode.com/problems/linked-list-cycle/",
            "Easy",
            ["Linked Lists", "Cycle Detection"],
            [Example("head = [3,2,0,-4], pos = 1","true")],
            [Constraint("The number of the nodes in the list is in the range [0, 10^4]."), Constraint("pos is -1 or a valid index in the linked-list.")],
            Solution(
                '''# Definition for singly-linked list.
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
        return False''',
                "This problem is a textbook problem. You use two pointers, one that advances twice as fast as the other. The idea is that if there is a cycle eventually the pointers would be running is a circle. If you imagine yourself running is a circle with someone else running at a different spped, eventuall you would meet the other person at the same point. Other wise if you are running in a straight line eventually you would reach the end before the other person if you are the faster one. So iterate through the list until the fast pointer reaches the end or the two pointers meet or the faster one reaches the end.",
                "O(n)",
                "O(1)",
            )
        )
    ]
)