import pickle

def isThisAWord(S):
    a = open("PickledWordList.pkl", "rb")
    t = pickle.load(a)
    a.close()
    
    if S in t:
        return True
    else:
        return False

anagramdict = {}
for word in t:
    wordList = list(word)
    sortword = wordList.sort()
    wTuple = tuple(sortword)
    if wTuple in anagramdict:
        anagramdict[wTuple].append(word)
    else:
        anagramdict[wTuple] = word

        
