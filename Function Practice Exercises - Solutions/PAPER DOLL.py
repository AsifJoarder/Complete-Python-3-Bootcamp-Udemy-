def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

# Check
n1 = paper_doll('Hello')

# Check
n2 = paper_doll('Mississippi')

print(n1,n2)