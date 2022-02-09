from timeit import timeit

class test:
    def __init__(self, var):
        self.var = var
    def doSomething(self):
        print(self.var)

def doSomethingSP():
    print('Hallo')

def doSomethingOOP():
    t1 = test('Hallo')
    t1.doSomething()


def code1():
    doSomethingOOP()

def code2():
    doSomethingSP()

time1 = timeit(code1, number=1000)
time2 = timeit(code2, number=1000)

print(time1)
print(time2)
print(time1 - time2)