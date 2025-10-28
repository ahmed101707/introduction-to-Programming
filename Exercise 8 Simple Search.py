names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = input("Enter a name to search for: ")

if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")
    