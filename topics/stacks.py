from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import Topic


stacks = Topic(
    "Stacks",
    "",
    [],
    "",
    [
        Problem(
            "3174",
            "Clear Digits",
            '''You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.''',
            "https://leetcode.com/problems/clear-digits/",
            "Easy",
            ["Strings", "Stacks"],
            [
                Example('s = "abc"', '"abc"'),
                Example('s = "cb34"', '""'),
            ],
            [
                Constraint("1 <= s.length <= 100"),
                Constraint("s consists only of lowercase English letters and digits."),
                Constraint("The input is generated such that it is possible to delete all digits.")
            ],
            Solution(
                '''class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            if c.isalpha():
                stack.append(c)
            else:
                stack.pop()

        return "".join(stack)''',
        "My first glance at this problem told me to use a stack to build the response. Anytime a problem uses the language 'remove the most recent item' or 'the one to the left' that is my first instinct. The only think I needed to do with this problem to make it more efficient is actually rearrange the if statement. At first I had the if checking to see if the number was a number. This was inefficient beacuse the nature of the problem is that there will always be at least as many regular characters as there are numbers. This means that yes there will be some test cases where having the number check first is just as efficient as putting the check to see if it is a number first. But for the majority of scenarios there is going to be more letters than numbers. This means checking for that in the if is going to be greatly more efficient.",
        "O(n)",
        "O(n)"
            )

        ),
        Problem(
            "1910",
            "Remove All Occurrences of a Substring",
            '''Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

    Find the leftmost occurrence of the substring part and remove it from s.

Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.''',
            "https://leetcode.com/problems/remove-all-occurrences-of-a-substring",
            "Medium",
            ["Strings", "Stacks"],
            [Example('s = "daabcbaabcbc", part = "abc"', '"dab"'), Example('s = "axxxxyyyyb", part = "xy"', '"ab"')],
            [Constraint("1 <= s.length, part.length <= 1000"), Constraint("s and part consists of lowercase English letters.")],
            Solution(
                '''class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ""
        n = len(part)
        for i, c in enumerate(s):
            res += c
            if not i < n - 1 and res[-n:] == part:
                res = res[0:-n]
        return res''',
        "This problem begs for some data structure that can pop like a stack. Originally I solved this problem using an array as the stack that I use to build the solution. But ultimately converting that to a string to compare to the part we are removing on every iteration was too costly. So I switched to a string as my 'stack' and would just remove from the end of it on an iteration where the end of the stack matched the part. The reason this solution works is because the only time you would need to remove from the stack when iterating through the input left to right is when the last letters in the stack match the part. Removing all of these letters allows you to still have the chaining affect where removing one set of the part leaves you with another set of the part in a candy crush style combo.",
        "O(n)",
        "O(n)"
            )
        ),
        Problem(
            "1028",
            "Recover a Tree From Preorder Traversal",
            '''We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.''',
            "https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/",
            "Hard",
            ["Tree", "Stacks"],
            [Example('s = "1-2--3--4-5--6--7"', '[[1],[2,5],[3,6],[4,7]]')],
            [Constraint("The number of nodes in the original tree is in the range [1, 1000]"), Constraint("1 <= Node.val <= 109")],
            Solution(
                '''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)

        i = 0
        pre = []
        while i < n:
            curr = 0
            while traversal[i] == "-":
                i += 1
                curr += 1
            
            num = ""
            while i < n and traversal[i] != "-":
                num += traversal[i]
                i += 1
            pre.append((int(num), curr))
        pre = deque(pre)
        rootVal, depth = pre.popleft()
        head = TreeNode(val=rootVal)
        stack = [(depth, head)]

        while pre:
            currVal, currDepth = pre.popleft()

            while stack and stack[-1][0] != currDepth - 1:
                stack.pop()
            
            parent = stack[-1][1]

            newNode = TreeNode(val=currVal)

            if not parent.left:
                parent.left = newNode
            else:
                parent.right = newNode
            
            stack.append((currDepth, newNode))

        return head''',
                "My thought process was obviously to do some sort of dfs as soon as I saw the problem. When I saw the input data I thought to put the data into a queue and build to the tree until the tree is clearly not expanding downwards anymore. When this happens you simply need a way to know where to pick up at in the imaginary stack. Pre process the array to allow for easy depth tracking and maitenance of the Nodes that we may want to append to the right of later on. Pre processing it allows us to think less about the hyphens and the input we are given to just focus on the abnormal dfs we are performing.",
                "O(n)",
                "O(n)"
            )
        )
    ]
)