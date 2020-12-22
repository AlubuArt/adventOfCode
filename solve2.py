lines = open('text.txt').readlines()
validCounter = 0
for line in lines:
    newLine = line.split(" ")
    quota, letter, pw = newLine[0], newLine[1][0], newLine[2]
    quotas = quota.split("-")
    quotaFirst, quotaSecond = int(quotas[0]), int(quotas[1])
    pwList = []
    pwList += pw
    pwList.insert(0, "q")
           
    if pwList[quotaFirst] == letter or pwList[quotaSecond] == letter:
        if pwList[quotaFirst] != pwList[quotaSecond]:
            validCounter += 1

print(validCounter)




            
            
    




        

        
        
        
    
    



        

        
        
        
    
    


