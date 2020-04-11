def solution():
    line = []
    num = int(input())
    line = input().split()
    if (len(line) == num):
        line = list(map(int, line))
        element = tuple(i for i in line)
        print(str(hash(element)))
    else:
        print("error")

if (__name__ == "__main__"):
    solution()