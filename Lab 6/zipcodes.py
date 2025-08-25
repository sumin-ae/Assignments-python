# Define the Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Define the Address class
class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

# Define the Contact class that contains Person and Address
class Contact:
    def __init__(self, person, address):
        self.person = person  # Instance of Person
        self.address = address  # Instance of Address

    # Method to display contact details
    def display_contact(self):
        print("Contact Information:")
        print(f"Name: {self.person.name}")
        print(f"Age: {self.person.age}")
        print(f"Street: {self.address.street}")
        print(f"City: {self.address.city}")
        print(f"Zipcode: {self.address.zipcode}")

# Create instances
person1 = Person("Alice", 28)
address1 = Address("123 Maple Street", "Springfield", "98765")
contact1 = Contact(person1, address1)

# Display the contact information
contact1.display_contact()
