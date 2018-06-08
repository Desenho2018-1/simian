
"""
    Throws exception for value that not a string
"""

class TextException(Exception):

    def __init__(self, message):
        super().__init__("This text not a string")
