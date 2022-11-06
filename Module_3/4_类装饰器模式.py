class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class B(object):
    def __init__(self):
        pass


b1 = B()
b2 = B()
print(id(b1), id(b2))
