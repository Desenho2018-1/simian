class BaseScene(object):

    name = ''

    def __init__(self):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError
