num_of_student = int(input())

# using map we can apply a single fuction over multiple data
# while typing the map fuction we first specify the fuction which is converting to integer
# then we specify the data to iterate over
score = map(int, input().split())

# implementing set for removal of duplicate data
score = list(set(list(score)))
score = sorted(score)
print(score[len(score) - 2])
