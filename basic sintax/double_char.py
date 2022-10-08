word = ""
doble_word = ""
while word != "End":
    if word == "SoftUni":
        word = str(input())
        continue
    for i in word:
        doble_word += i
        doble_word += i
    print(doble_word)
    doble_word = ""
    word = str(input())