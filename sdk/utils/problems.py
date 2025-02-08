import os
from sdk.models.problems import Problem
from sdk.utils.code import codeToReadmeString
from sdk.utils.filecrud import threeDigitIndex, upsert_directory, writePython, writeReadMe


def buildProblemReadme(problem: Problem):
    res = ""

    res += f"## {problem.title}\n\n" 

    tags = ", ".join([f"`{topic}`" for topic in problem.topics])
    
    res += f'**Difficulty**: `{problem.difficulty}` - **Tags**: {tags}\n\n'

    res += f"### Description\n\n{problem.description}\n\n"

    res += f"### Examples\n\n"

    for i, example in enumerate(problem.examples):
        res += f"**Example {i+1}:**\n\n"
        res += f"**Input**: ```{example.input}```\n\n"
        res += f"**Output**: ```{example.output}```\n\n"
    
    res += "### Constraints\n\n"
    
    for constraint in problem.constraints:
        res += f'- `{constraint.body}`\n\n'

    
    res += "### Solution\n\n"
    res += f"**Description**:\n\n{problem.solution.description}\n\n"
    res += f"**Time Complexity**: {problem.solution.timeComplexity} - **Space Complexity**: {problem.solution.spaceComplexity} \n\n"
   
    res += f"```python\n{problem.solution.code}\n```"

    return res

def buildPythonCode(problem: Problem):
    res = ""

    res += problem.solution.code

    return res

def handleProblem(problem: Problem, index: int, parentDirectory: str):
    directory = os.path.join(parentDirectory, threeDigitIndex(problem.title, index))

    upsert_directory(directory)

    writeReadMe(directory, buildProblemReadme(problem))

    writePython(directory, buildPythonCode(problem))

    return