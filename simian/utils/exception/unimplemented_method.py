class NotOverridenMethod(Exception):

    def __init__(method_message):
        super().__init__("the method"+ method_message +" isn't overridden")
