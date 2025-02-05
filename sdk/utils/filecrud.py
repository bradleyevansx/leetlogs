import os

def upsert_directory(path):
    full_path = os.path.join(os.getcwd(), path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

initIgnore = ["sdk", "index.py"]

def threeDigitIndex(input: str, index: int):
    return f"{str(index+1).zfill(3)} - {input}"
    
def writeReadMe(directory: str, content: str):
    with open(f"{directory}/README.md", "w") as file:
        file.write(content)

    return

def writePython(directory: str, content: str):
    with open(os.path.join(directory, "solution.py"), "w") as file:
        file.write(content)

def init():
    for file in os.listdir():
        if file not in initIgnore:
            try:
                file_path = os.path.join(os.getcwd(), file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    for root, dirs, files in os.walk(file_path, topdown=False):
                        for name in files:
                            os.remove(os.path.join(root, name))
                        for name in dirs:
                            os.rmdir(os.path.join(root, name))
                    os.rmdir(file_path)
            except PermissionError:
                print(f"Permission denied: {file}")