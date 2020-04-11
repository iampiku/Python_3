# Learning Nested list comprihension 

num_student = int(input())
database = [[input(), float(input())] for i in range(num_student)]

# passing all the scores element from a set to avoid repetetion
scores = list(set([database[x][1] for x in range(num_student)]))

# again coverting the scores to list to perform sorting
scores.sort()

database = [x[0] for x in database if x[1] == scores[1]]
database.sort()  

for i in database:
    print(i)
