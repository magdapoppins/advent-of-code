with open("input.txt", "r") as nums:
    id_list = []
    for line in nums:
        id_list.append(line)

def countDifference(a, b): 
    diff = 0
    for letter in range(len(a)-1):
        if a[letter] != b[letter]:
            diff+=1
            
    return diff

similarCodes = []

for codeA in id_list:
    for codeB in id_list:
        if countDifference(codeA, codeB) == 1:
            print(codeA, codeB)
            similarCodes.append(codeA)
            similarCodes.append(codeB)
        
difference = []

for i in range(len(similarCodes[0])):
    if similarCodes[0][i] != similarCodes[1][i]:
        difference.append(similarCodes[0][i])

print(similarCodes[0], similarCodes[1], "Diff: ", difference)
