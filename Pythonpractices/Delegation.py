class Base:
    def __init__(self,name):
       self.x = name
    def xprint(self):
        print("I am in Base class", self.x)
        
class derived(Base):
    def __init__(self):
        print(" I am in Derive class")
        Base.__init__(self, 'Manas')
x = derived()
x.xprint()
y = Base("David" )
y.xprint()