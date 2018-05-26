import re


project_name_pattern = re.compile(r'[a-zA-z\-]+[0-9]*')


def validate_project_name(project_name):
    """
    Validate if a project name follow the rules of simian
    """
    span = project_name_pattern.search(project_name).span()
    if (span[1]-span[0]) == len(project_name):
        return True
    return False
