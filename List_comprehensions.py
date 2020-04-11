x = int(input())
y = int(input())
z = int(input())
num = int(input())
# list comprehension is a format for list where you can provide constrains and repetation in the list itself to generate the disered format of list
list_coordinates = [[i, j, r] for i in range(x + 1) for j in range(y + 1)
                    for r in range(z + 1) if ((i + j + r) != num)]
print(list_coordinates)