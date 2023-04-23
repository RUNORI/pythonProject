import zope.interface


class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute('foo')

    def method1(self, x, y, z):
        pass

    def method2(self):
        pass


@zope.interface.implementer(MyInterface)
class MyClass:
    def method1(self, x):
        return x ** 2

    def method2(self):
        return "foo"


obj = MyClass()

print(MyInterface.implementedBy(MyClass))

print(MyInterface.providedBy(MyClass))

print(MyInterface.providedBy(obj))

print(list(zope.interface.implementedBy(MyClass)))

print(list(zope.interface.providedBy(obj)))

print(list(zope.interface.providedBy(MyClass)))
