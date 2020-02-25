class SuperTuple:
    def add_to_tuple(self,t = tuple(), *varg):

        print('t = ', t, id(t), type(t))

        l = list(t)
        print('l = ', l, id(l), type(l))
        for x in varg:
            l.append(x)
        print('l = ', l, id(l), type(l))
        t = tuple(l)
        print('t = ', t, id(t), type(t))
        return t


dev = SuperTuple()

myTuple = (10,20,30,50)
print('myTuple original', myTuple, id(myTuple), type(myTuple))

myTuple  = dev.add_to_tuple(myTuple, 100,200,300)
print('myTuple after addition', myTuple, id(myTuple), type(myTuple))