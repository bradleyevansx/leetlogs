from typing import List

from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import SubTopic, Topic
from sdk.utils.filecrud import init
from sdk.utils.topics import handleTopic
from topics.heaps import heaps
from topics.stacks import stacks
from topics.arraystrings import arraystrings
from topics.hashmaps import hashmaps
from topics.twopointers import twopointers

topics: List[Topic] = [
    arraystrings,
    twopointers,
hashmaps,
heaps,
    Topic("Sliding Windows"),
   stacks,
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
