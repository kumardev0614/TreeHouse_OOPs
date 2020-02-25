# Here we will see basic structure of class in python
# Here we will make a class Thief, every instance of thief class can be sneaky (property),
# and can do pickpocketing(method)


class Thief:        # Here by convention we define class name in camel case ThisIsMyClass
    sneaky = True   # Property of instance of class Thief

    def pickpocket(self):       # Behaviour of instance of class thief
        if self.sneaky is True:
            print(self, 'is sneaky in nature. He is able to pick pocket')
        else:
            print(self, 'is not sneaky in nature. He is not able to pick pocket')


raju = Thief()
print(raju.sneaky)
raju.pickpocket()

dev = Thief()
dev.sneaky = False
print(dev.sneaky)
dev.pickpocket()

print()
# here we can call sneaky directly by class also
print('Called by Class:', Thief.sneaky)
# but we cannot call method by class, because it is expecting an object of class not the class itself
# Thief.pickpocket()
# To call the method directly by class we have to pass object explicitly
Thief.pickpocket(dev)


# What is self at here?
# self -- methods are functions that is belong to a class. But they are used by an instance (object) not by the actual
# class. Because of that, Methods always take at least one parameter, which represent the instance that is using
# the method
# now by convention that parameter is always called SELF, we can call anything we want in our own class
# we don't give any argument to self when we use the method
