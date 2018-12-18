import pickle
f = open("words.txt", "r")
oneGiantString = f.read()
f.close()
wordList = oneGiantString.split()
a = open("PickledWordList.pkl", "wb")
pickle.dump(wordList,a)
a.close()
