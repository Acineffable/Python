def wordFrequency(sentence):
    word = sentence.split()
    lista = []
    lista.append(word)
    n=0
    sentencedict = {i:word.count(i) for i in word}
    print(sentencedict)
                    
