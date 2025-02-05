def codeToReadmeString(code: str):
    print(code)
    code = code.replace('\n', '\\n').replace('\t', '\\t')
    print(code)
    return code