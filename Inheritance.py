class animal:
    def speak(self):
        print("Hi I'm an animal")

class cat(animal):
    def meow(self):
        print("Meowwww!")

a=cat()
a.speak()
a.meow()