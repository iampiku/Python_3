message = input("Mood : ")
emojis = {":)": "😁", ":(": "😔", ":p": "😛", "B)": "😎"}
print(emojis.get(message, "Mood not found"))
