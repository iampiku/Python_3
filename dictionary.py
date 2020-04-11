num = {
    #keys  #values
    "1": "One",  #include comma at the end of each pair
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
user_input = input()
# output is used to store the values of the keys
output = ""
# using a for loop to iterate through user inputs
for i in user_input:
    output += num.get(i, "Value not found") + " "
print(output)
