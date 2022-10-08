number = int(input())
odd = True
for i in range(number):
    count = int(input())
    if count % 2 != 0:
        odd = False
        print(f"{count} is odd!")
        break

if odd == True:

    print("All numbers are even.")
