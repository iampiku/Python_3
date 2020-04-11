num = int(input())
for i in range(num) :
    number = input()
    if(number[0] == "9" or number[0] == "7" or number[0] == "8") :
        if(number.isdigit() == False) :
            print("NO")
        elif(len(number) == 10) :
            print("YES")
        else:
            print("NO")
    else :
        print("NO")
