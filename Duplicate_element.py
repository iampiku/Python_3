List = [10, 50, 20, 30, 10]
unique_List = []
for i in List:
    if (i not in unique_List):
        unique_List.append(i)
print(unique_List)