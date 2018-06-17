
"""
    Throws exception for value that not a string
"""


class TextException(Exception):

    def __init__(self):
        super().__init__("This is not a string")
