with open("input.txt", "r") as nums:
    array = []
    for line in nums:
        array.append(line)

value = 0
for num in array:
    if (num[0] == "-"):
        value -= int(num[1:])
    elif (num[0] == "+"):
        value += int(num[1:])

print(value)