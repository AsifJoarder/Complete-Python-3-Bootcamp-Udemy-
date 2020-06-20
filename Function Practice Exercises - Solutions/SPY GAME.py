def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1

# Check
n1 = spy_game([1,2,4,0,0,7,5])

# Check
n2 = spy_game([1,7,2,0,4,5,0])

print(n1,n2)