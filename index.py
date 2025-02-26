from typing import List

from sdk.models.problems import Constraint, Example, Problem, Solution
from sdk.models.topic import SubTopic, Topic
from sdk.utils.filecrud import init
from sdk.utils.topics import handleTopic
from topics.linkedlists import linkedlists
from topics.heaps import heaps
from topics.stacks import stacks
from topics.arraystrings import arraystrings
from topics.hashmaps import hashmaps
from topics.twopointers import twopointers
from topics.dp import dp

topics: List[Topic] = [
    arraystrings,
    twopointers,
hashmaps,
heaps,
    Topic("Sliding Windows"),
   stacks,
   linkedlists,
    Topic("Trees"),
    Topic("Matricies"),
    Topic("Intervals"),
    dp
]

def main():
    init()
   
    for i, topic in enumerate(topics):
        handleTopic(topic, i)


if __name__ == "__main__":
    main()
