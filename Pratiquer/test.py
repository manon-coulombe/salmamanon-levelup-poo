class Pet:
    def __init__(self, name, greeting = "Hello"):
        self.name = name
        self.greeting = greeting

    def say_hi(self):
        print(f"{self.greeting}, I'm {self.name}!")

    legs = 0
    
    @classmethod
    def legs_count(cls):
        print(f"I have {cls.legs} legs !")

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Meow")

    legs = 4

class Parrot(Pet):

    def __init__(self, name):
        super().__init__(name, "Bonjour")

    def say_hi(self):
        print(f"{self.greeting}, my name is {self.name}!")

    legs = 2

my_pet = Pet("Gaston", "Coucou")
my_pet.say_hi()

cat = Cat("Félix")
cat.say_hi()

parrot = Parrot("Jacquot")
parrot.say_hi()

Cat.legs_count()
Parrot.legs_count()

cat.legs_count()
parrot.legs_count()

