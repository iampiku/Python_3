# Learnign about classes and object in python

class Largest_Element:

    def max_element(self,num_of_elem):
        student_score = []
        for i in range(0, num_of_elem):
            user_input = int(input("Enter the element : "))
            student_score.append(user_input)

        max_score = 0
        for j in student_score:
            if (max_score < j):
                max_score = j

        print(max_score)

# creating the object of the class as output
output = Largest_Element()

# using the object output to call the fuction max_element
num = int(input("Enter the range of the list : "))
output.max_element(num)

    
