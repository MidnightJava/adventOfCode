import inspect

class Foo():
    def __init__(self):
        self._foo = None
        for m in inspect.getmembers(Foo, predicate=inspect.isdatadescriptor):
            a = m[1]
            if a.__class__ == property:
                a.fset(self, 'bar')

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, foo):
        print(f'SETTING foo to {foo}')
        self._foo = foo


f = Foo()
fa = getattr(Foo, 'foo')
print(f.foo)
f.foo = 'yahoo'
print(f.foo)