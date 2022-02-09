class Variables:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
        def add(self):
            return self.var1 + self.var2



o1 = Variables(1, 2)

def add(var1=0, var2=0, var3=0):
    return var1 + var2 + var3

print(add(1,1,1))