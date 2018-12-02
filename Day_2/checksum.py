with open("input.txt", "r") as nums:
    id_list = []
    for line in nums:
        id_list.append(line)

# Count twices, thrices and checksum
twices = 0
thrices = 0
for code in id_list:
    for letter in code:
        if code.count(letter) == 2:
            twices += 1
            break;
    for letter in code:    
        if code.count(letter) == 3:
            thrices += 1
            break;


print("Checksum: ", twices*thrices)