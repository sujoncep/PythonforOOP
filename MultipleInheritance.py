class A:
    def classAMethod(self):
        return "I am a class A method"

    def hello(self):
        return "hello from A class"


class B:
    def classBMethod(self):
        return "I am a class B method"

    def hello(self):
        return "hello from B class"


class C(A, B):
    pass


instanceA = A()
instanceB = B()
instanceC = C()

print(instanceA.classAMethod())
print(instanceB.classBMethod())
print(instanceC.classAMethod())
print(instanceC.hello())

# print(help(instanceC))

print(C.mro())
