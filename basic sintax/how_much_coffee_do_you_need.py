count_of_coffees = 0
command = input()
while command != "END":
    if command == "coding":
        count_of_coffees += 1
    elif command == "CODING":
        count_of_coffees += 2
    elif command == "dog" or command == "cat":
        count_of_coffees += 1
    elif command == "DOG" or command == "CAT":
        count_of_coffees += 2
    elif command == "movie":
        count_of_coffees += 1
    elif command == "MOVIE":
        count_of_coffees += 2
    command = input()
if count_of_coffees > 5:
    print("You need extra sleep")
else:
    print(count_of_coffees)