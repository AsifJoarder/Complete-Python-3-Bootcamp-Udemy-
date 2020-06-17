def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# Check
n1 = almost_there(90)

# Check
n2 = almost_there(150)

# Check
n3 = almost_there(209)

print(n1,n2,n3)