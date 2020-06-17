def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20  #returning boolean by checking

# Check
n1 = makes_twenty(20,10)

# Check
n2 = makes_twenty(12,8)

print(n1,n2)