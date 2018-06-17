
"""
Exception throw, when a not implmenting methods
that should be overridde
"""


class NotOverriddenMethod(Exception):

    def __init__(self, method_message):
        super().__init__("the method " + method_message + " isn't overridden")
