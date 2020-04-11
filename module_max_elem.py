# Learning to create module by small pices of code 

def max_element(num_of_elem):

        student_score = []
        for i in range(0, num_of_elem):
            user_input = int(input("Enter the element : "))
            student_score.append(user_input)

        max_score = 0
        for j in student_score:
            if (max_score < j):
                max_score = j

        return max_score

