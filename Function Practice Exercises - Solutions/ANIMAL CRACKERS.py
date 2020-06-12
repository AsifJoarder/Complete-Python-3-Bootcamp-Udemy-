def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


# Check
result = animal_crackers("Royal tiger")
print(result)
