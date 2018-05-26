import re


project_pattern = re.compile(r'[a-zA-z\-]+[0-9]*')

def validate_project_name(project_name):
    span = project_pattern.search(project_name).span()
    print(len(project_name))
    if (span[1]-span[0]) == len(project_name):
        return True
    return False