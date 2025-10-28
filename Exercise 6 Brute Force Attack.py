correct_password = "12345"
max_attempts = 5
attempts = 0
success = False
while attempts<max_attempts:
    attempt = input("Enter password: ")
    if attempt == correct_password:
        print("Password accepted")
        success = True
        break
    attempts +=1
    remaining = max_attempts - attempts
    print(f"Incorrect password, {remaining} attempts remianing")
if not success:
    print("Maximum attemots reached, Authorities have been alerted")
