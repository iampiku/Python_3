def solution():
    num = []
    for i in range(int(input())):
        line = input().split()
        command = line[0]
        element = line[1:]
        element = list(map(int,element))
        if (command.lower() == "insert"):
            pos = element[0]
            ele = element[1]
            num.insert(pos,ele)
        elif (command.lower() == "print"):
            print(num)
        elif (command.lower() == "remove"):
            for i in element:
                num.remove(i)
        elif (command.lower() == "pop"):
            num.pop()
        elif (command.lower() == "append"):
            for i in element:
                num.append(i)
        elif (command.lower() == "reverse"):
            num.reverse()
        elif (command.lower() == "sort"):
            num.sort()

if __name__ == "__main__":
    solution() 