try:
    name = input("Enter your name : ")
    income = int(input("Enter your yearly Income : "))
    income_per_month = income / 12
    print(f"Hello {name}")
    print(f"This is your monthly income : {income_per_month}")

    #in except you have to specify the type of exception that can generate in your code
except ValueError:
    print("Enter you income should be a whole number")
