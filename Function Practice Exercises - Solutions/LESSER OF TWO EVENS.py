def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

# Check
value1 = lesser_of_two_evens(2,4)

# Check
value2 = lesser_of_two_evens(2,5)

print(value1,value2)
