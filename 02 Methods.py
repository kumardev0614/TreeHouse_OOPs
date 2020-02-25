# here we will see arguments other than self


class myClass:
    a = 0
    b = 0

    def method1(self):
        print("method1 is called")

    def sum(self, c, d, total = 0, **kwargs):
        print(self.a)
        print(self.b)
        print(c)
        print(d)
        print(total)
        print(kwargs)
        total = total + self.a + self.b + c + d

        fullname = ''
        for key,value in kwargs.items():
            fullname = fullname + value
        print(fullname)
        return total


obj1 = myClass()
obj1.method1()
obj1.a = 5
obj1.b = 10

print(obj1.sum(5,8))        # sum(self = obj1,  c = 5,  d = 8,  total = 0,  kwargs = {})
# ........................... total <==> total = 0  +  obj1.a = 5  +  obj1.b = 10  +  c = 5  +  d = 8
# only c and d are passed


print('----------------')


print(obj1.sum(15,18,100))        # sum(self = obj1,  c = 15,  d = 18,  total = 100,  kwargs = {})
# ........................... total <==> total = 100  +  obj1.a = 5  +  obj1.b = 10  +  c = 15  +  d = 18
# c,d and total are passed


print('----------------')


print(obj1.sum(15,18,total = 200, fname = 'dev',  lname = ' bharti'))
# sum(self = obj1,  c = 15,  d = 18,  total = 200,  kwargs = {'name' = 'dev', 'lname' = ' bharti'})
# total <==> total = 200  +  obj1.a = 5  +  obj1.b = 10  +  c = 15  +  d = 18
# fullname = fname = 'dev'  +  lname = 'bharti'





