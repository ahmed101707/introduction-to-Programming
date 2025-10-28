name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

person = {"name": name, "hometown": hometown, "age": age}
print(person["name"], person["hometown"], person["age"], sep="\n")