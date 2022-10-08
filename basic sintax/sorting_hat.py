count = 0
name = input()
evil_name = False
while name != "Welcome!":
    for _ in name:
        count += 1
    if name == "Voldemort":
        print("You must not speak of that name!")
        evil_name = True
        break
    elif count < 5:
        print(f"{name} goes to Gryffindor.")
    elif count == 5:
        print(f"{name} goes to Slytherin.")
    elif count == 6:
        print(f"{name} goes to Ravenclaw.")
    elif count > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
    count = 0
if evil_name == False:
    print("Welcome to Hogwarts.")