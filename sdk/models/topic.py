from typing import List

from sdk.models.problems import Problem

class Trick:
     def __init__(self, title: str, description: str, code: str):
        self.title = title
        self.description = description
        self.code = code

class ProblemPreview:
    def __init__(self, title: str, link: str, difficulty: str, topics: List[str], tricks: List[Trick] = []):
        self.title = title
        self.link = link
        self.difficulty = difficulty
        self.topics = topics
        self.tricks = tricks

class SubTopic:
    def __init__(self, title: str, body: str, problems: List[ProblemPreview] = []):
        self.title = title
        self.body = body
        self.problems = problems

class Topic:
    def __init__(self, name: str, intro: str = "", subTopics: List[SubTopic] = [], conclusion: str = "", problems: List[Problem] = []):
        self.name = name
        self.intro = intro
        self.subTopics = subTopics
        self.conclusion = conclusion
        self.problems = problems