
# enum for difficulty

from typing import List


class Example:
    def __init__(self, input: str, output: str):
        self.input = input
        self.output = output

class Constraint:
    def __init__(self, body: str):
        self.body = body

class Solution:
    def __init__(self, code: str, desription: str, timeComplexity: str, spaceComplexity: str):
        self.code = code
        self.description = desription
        self.timeComplexity = timeComplexity
        self.spaceComplexity = spaceComplexity

class Problem:
    def __init__(self, id: int, title: str, description: str,  link: str, difficulty:str, topics: List[str], examples: List[Example], constraints: List[Constraint], solution: Solution):
        self.id = id
        self.title = title
        self.description = description
        self.link = link
        self.difficulty = difficulty
        self.topics = topics
        self.examples = examples
        self.constraints = constraints
        self.solution = solution