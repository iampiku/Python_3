num = int(input())
if (num % 2 == 1):
    print("Weird")
else:
    if (num % 2 == 0 & 2 <= num <= 5):
        print("Not Weird")
    elif (num % 2 == 0 & 6 <= num <= 20):
        print("Weird")
    elif (num % 2 == 0 & num < 20):
        print("Not Weird")