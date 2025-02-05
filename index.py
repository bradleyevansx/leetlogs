from typing import List

from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import SubTopic, Topic
from sdk.utils.filecrud import init
from sdk.utils.topics import handleTopic

topics: List[Topic] = [
    Topic(
        "Arrays and Strings", 
        "Arrays and Strings are two of the most commonly used data structures. Therefore, it is important to be familiar with all of the different ways you can use them. Arrays are the data structure you look to when you want a convenient way to store groups of information. Strings are the data structure most commonly know for storing arrays of characters, otherwise known as words.",
        [
            SubTopic(
                "Basics of accessing elements within a Array/String",
                "The most basic operation you can do with an array is to access an element at a specific index. This is done by using the square brackets operator. For example, if you have an array called `arr`, you can access the first element by using `arr[0]`.",
                []
            ),
        ],
        "Arrays and Strings are the building blocks used in many algorithms you will interact with on a daily basic. Getting familiar with all the different algorithms related to these data structures will help you greatly in the long run.",
        [
            Problem(
                "1790",
                "Check if One String Swap Can Make Strings Equal",
                "You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices. Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.",
                "https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/",
                "Easy",
                ["Hash Table", "String", "Counting"],
                [
                    Example(
                        's1 = "bank", s2 = "kanb"',
                        'True'  
                    ),
                    Example(
                        's1 = "attack", s2 = "defend"',
                        'False'
                    ),
                    Example(
                        's1 = "kelb", s2 = "kelb"',
                        'True'
                    )
                ],
                [
                    Constraint("1 <= s1.length, s2.length <= 100"),
                    Constraint("s1.length == s2.length"),
                    Constraint("s1 and s2 consist of only lowercase English letters"),
                ],
                Solution(
                    """class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        res = 0
        h1, h2 = set(), set()

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                h1.add(s1[i])
                h2.add(s2[i])
                res += 1
        
        if res == 0 or res == 2:
            if h1 == h2:
                return True
        return False""",
                    "The solution is to check if the two strings are equal. If they are, return True. Otherwise, find the indexes of the characters that are different and store them in a list. If the length of the list is not 2, return False. Otherwise, check if the characters at the indexes in the list are equal. If they are, return True. Otherwise, return False.",
                    "O(n)",
                    "O(n)"
                )
            )
        ]
    ),
    Topic("Two Points"),
    Topic("Hash Maps"),
    Topic("Sliding Windows"),
    Topic("Stacks"),
    Topic("Linked Lists"),
    Topic("Trees"),
    Topic("Matricies"),
    Topic("Intervals"),
    Topic("Dynamic Programming"),
]

def main():
    init()
   
    for i, topic in enumerate(topics):
        handleTopic(topic, i)


if __name__ == "__main__":
    main()
