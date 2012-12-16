from hy.lang.hyobj import HYObject


class HYSymbol(unicode, HYObject):
    def __init__(self, string):
        self += string

    def eval(self, *args, **kwargs):
        if self.isdigit():
            return float(self)
        return self.namespace[self]
