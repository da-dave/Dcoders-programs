class Pet:
    # pets created
    pet_number = 0

    # Constructor method
    def __init__(self, pet_name="UNK", owner_name="UNK", pet_type="UNK", pet_breed="UNK", pet_age="UNK"):
        # instance attributes
        self.pet_name = pet_name
        self.owner_name = owner_name
        self.pet_type = pet_type
        self.pet_breed = pet_breed
        self.pet_age = pet_age
        Pet.pet_number += 1

    def change_age(self, pet_age):
        if 0 < pet_age < 30:
            self.pet_age = pet_age
        else:
            print("Invalid age.")

    def __str__(self):
        return (f"Name: {self.pet_name}\n"
                f"Age: {self.pet_age}\n"
                f"Type: {self.pet_type}\n"
                f"Breed: {self.pet_breed}\n"
                f"Owner: {self.owner_name}")


# Example usage
placeholder = Pet()
print(placeholder)
nimmy = Pet("Nimmy", "Anna Wright", "Cat", "Orange", "7")
print(nimmy)
print("---")
nimmy.change_age(11)
print(nimmy)
print("---")
nimmy.change_age(40)
print(nimmy)
print("Number of pets created", nimmy.pet_number)

