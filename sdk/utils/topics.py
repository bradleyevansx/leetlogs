
from sdk.models.topic import Topic
from sdk.utils.filecrud import threeDigitIndex, upsert_directory, writeReadMe
from sdk.utils.problems import handleProblem


def buildTopicReadme(topic: Topic):
    res = ""

    res += f"# {topic.name}\n\n"
    
    res += f"{topic.intro}\n\n"

    res += f"---\n\n"

    res += f"## Fundamentals in {topic.name}\n\n"

    for i, subTopic in enumerate(topic.subTopics):
        res += f"### {i}. {subTopic.title}\n\n"
        res += f"{subTopic.body}\n\n"

        if len(subTopic.problems) > 0:

            res += f"#### Learn more about {subTopic.title}\n\n" 

            for problem in subTopic.problems:
                res += f"[{problem.title}]({problem.link}) - {problem.difficulty}\n\n"
    return res



def handleTopic(topic: Topic, index: int):
    directory = threeDigitIndex(topic.name, index)

    print(directory)    

    upsert_directory(directory)

    content = buildTopicReadme(topic)

    writeReadMe(directory, content)

    for i, problem in enumerate(topic.problems):
        handleProblem(problem, i, directory)

    return