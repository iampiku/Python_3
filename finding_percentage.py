def solution():
    database = {}
    for i in range(int(input())):

        # creating a list for input data
        line = input().split()
        name = line[0] 
        score = line[1:]
        score = list(map(float, score))
        database.update({name:score})
        
    user_input = input()
    result = database[user_input]
    print('%.2f' %(sum(result)/len(result)))

solution()