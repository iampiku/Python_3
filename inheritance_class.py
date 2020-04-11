#learning about in heritance in python between classes
class Person_age:

    def age(self,age):
        print(f'I am {age} old')

# the person class inherits the Person age class fuction 
class Person(Person_age):

    def talk(self,name):
        print(f'Hey! My name is {name}')


user_name = Person()
user_age = Person()
user_name.talk("Pradipta Chatterjee")
user_age.age(21)
