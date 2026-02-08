class Demo:
    a = 4

o = Demo()
print(o.a) # Demo: This is just the name we gave our blueprint.

a = 4: #This is a Class Attribute. Because it is inside the blueprint, every house built from this blueprint starts with the knowledge that a is 4.
o.a = 0 # o: This is our actual house (the Object).

Demo(): #This tells Python to "Look at the Demo blueprint and build me a house." Now, the variable o represents that specific house.
print(o.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute
