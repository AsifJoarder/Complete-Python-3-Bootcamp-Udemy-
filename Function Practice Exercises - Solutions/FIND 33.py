def has_33(nums):
    for i in range(0, len(nums) - 1):

        # nicer looking alternative in commented code
        # if nums[i] == 3 and nums[i+1] == 3:

        if nums[i:i + 2] == [3, 3]:
            return True

    return False


# Check
n1 = has_33([1, 3, 3])

# Check
n2 = has_33([3, 1, 3])

# Check
n3 = has_33([1, 3, 1])

print(n1,n2,n3)