#code by surya kumar 
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Meow")

def animal_sound_in_zoo(animal):
    animal.make_sound()

# Creating instances of Dog and Cat
dog_instance = Dog()
cat_instance = Cat()

# Calling the animal_sound_in_zoo function with instances
print("Dog in the zoo:")
animal_sound_in_zoo(dog_instance)

print("\nCat in the zoo:")
animal_sound_in_zoo(cat_instance)
