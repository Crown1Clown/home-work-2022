devisor = int(input())
boundary = int(input())
all_numbers = list()
for i in range(1, boundary+1):
    if i % devisor == 0:
        all_numbers.append(i)
print(max(all_numbers))