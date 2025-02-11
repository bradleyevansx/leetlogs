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

        )
    ]
)