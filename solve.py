file = open('text.txt')
lines = file.readlines()

list = []
counter = 0
validCounter = 0

for line in lines:
    newLine = line.split(" ")
    
    for row in newLine:
        quota, letter, pw = newLine[0], newLine[1][0], newLine[2]
        quotas = quota.split("-")
        quotaMin = quotas[0]
        quotaMax = quotas[1]
        
    
    for letters in pw:
        if letters == letter:
            counter +=1
            
    if counter >= int(quotaMin) and counter <= int(quotaMax) :
        print("valid")
        counter = 0
        validCounter +=1
    else:
        print("invalid")
        counter = 0



print(validCounter)
        

        
        
        
    
    


