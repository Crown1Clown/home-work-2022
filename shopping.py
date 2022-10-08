budget = int(input())
while True:
    command = input()
    if command == "End":
        if budget > 0:
            print("You bought everything needed.")
        else:
            print("You went in overdraft!")
        break
    price = int(command)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break