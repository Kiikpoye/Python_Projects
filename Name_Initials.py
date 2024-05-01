num_of_names = int(input("Enter number of names: "))
list = []
for num in range(1, num_of_names + 1):
    num_of_names -= 1
    name = input().split()
    list.append(name[0][0]+name[1][0])
for item in list:
    print(item, end=' ')

