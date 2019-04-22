class A:
    def __init__(self):
        self.__foo = 'foo'
        self._bar = 'bar'


a = A()
print(A.__dict__)
print(a.__dict__)
print(a._bar)
# print(a.__foo)
