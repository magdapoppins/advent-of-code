with open("input.txt", "r") as nums:
    array = []
    for line in nums:
        array.append(line)


searching = True
freqs = [0]
value = 0

while(searching):
    for num in array:
        value += int(num)

        if value in freqs:
            print(value)
            searching = False
            break
        
        freqs.append(value)

    print(value)





