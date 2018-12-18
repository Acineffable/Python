b = open("pilgrimsprogress.txt","r")
bString = b.read()
b.close()
c = 0 
bDictionary = {}
for word in bString:
    bList = bString.split()
    bDictionary[word] = bList[c+1]
    c+=1

print(bDictionary)



##anagramdict = {}
##for word in t:
##    wordList = list(word)
##    sortword = wordList.sort()
##    wTuple = tuple(sortword)
##    if wTuple in anagramdict:
##        anagramdict[wTuple].append(word)
##    else:
##        anagramdict[wTuple] = word
