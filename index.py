from typing import List

from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import SubTopic, Topic
from sdk.utils.filecrud import init
from sdk.utils.topics import handleTopic
from topics.arraystrings import arraystrings
from topics.hashmaps import hashmaps

topics: List[Topic] = [
    arraystrings,
    Topic("Two Pointers"),
hashmaps,
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
