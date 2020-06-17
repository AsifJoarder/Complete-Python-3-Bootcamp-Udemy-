def master_yoda(text):
    return ' '.join(text.split()[::-1])

# Check
n1 = master_yoda('I am home')

# Check
n2 = master_yoda('We are ready')

print(n1+"  "+n2)