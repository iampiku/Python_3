def validator(user_input):
    for test in ('isalnum','isalpha','isupper','islower','isdigit'):
        print(any(eval('b.'+test+'()') for b in user_input))
        # under any() fuction if only one of the condition returns a true value the output of the fuction will be true

if __name__ == "__main__":
    validator(user_input = input())
    