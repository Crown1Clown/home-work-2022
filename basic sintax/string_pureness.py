number_of_words = int(input())
check = True
for _ in range(number_of_words):
    word = input()
    check = True
    for i in word:
        if i == "." or i == "," or i == "_":
            print(f"{word} is not pure!")
            check = False
            break
    if check == True:
        print(f"{word} is pure.")
