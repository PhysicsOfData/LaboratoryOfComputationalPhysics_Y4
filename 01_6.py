class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry


    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)


    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
    def eat(self):
        self.is_hungry=False
        return self.is_hungry
    
    def feed(self):
        if(self.is_hungry==True):
            self.eat()
            return "My dogs are not hungry."
        else:
            return "My dogs are hungry."


if __name__ == "__main__":

    dogs=[('giacomo',10,True),('daniele',12,True),('bree',11,False),('forma',14,False)]

    mydogs=[Dog(dog[0],dog[1],dog[2]) for dog in dogs]

    print('I have %d dogs'%len(mydogs))

    flag=True
    for dog in mydogs:
        print(dog.description())
        if(dog.species != 'mammal'):
            flag=False        
    if flag:
        print("And they're all mammals, of course.")
    #to feed all the dogs
    for dog in mydogs:
        if(dog.is_hungry==True):
            dog.eat()
            print(f"{dog.name} was hungry so i feed it")
        else:
            print(f"{dog.name} is not hungry")
