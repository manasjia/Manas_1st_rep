class test :
    def __init__(self, n):
        self.x = n

    def leprint(self):
        print(self.x)
class specialclass:
    def amethod(self):
        print("Special")
class normalclass:
    def amethod(self):
        print("Normal class")

def appropriatecase(isnormal = 0):
    if isnormal: return normalclass()
    else: return specialclass()
x = int(input('enter isnormal value'))
aninstance= appropriatecase(isnormal= x)
aninstance.amethod()

class baseclass:
    def greet(self,name):
        print("Welcome :", name)
class sub (baseclass):
    def greet(self,name):
        print(" Welcome Mat and ", name)
        baseclass.greet(self,name)
x = sub ()
x.greet('Sonu')

anotherinstance = test(20)
anotherinstance.leprint()
