##QUESTION 1

# Fix this buggy code
options = ["Eat an Apple", "World Peace", "Destroy the World"]
print("Here are your options:")
count=1
for opt in options:
    print(str(count) + ". " + opt)
    count=count+1
x = int( input("What would you like to do? ") )
print("Ok... " + options[x-1])

# Note: It's a silly example, but a serious point.
# Such logic erros can be really hard to find and have big consequences!

##QUESTION 2
timestable = int(input("What timestable do you want?"))
for i in range(1,13):
    multiply=i*timestable
    print(i,"x",timestable,"=",multiply)
    
##QUESTION 3
shopList = []
while True:
    shoppingList = input("Add item to the shopping list:")
    if shoppingList in shopList:
        continue
    elif shoppingList == "END":
        break
        continue
    elif shoppingList not in shopList:
        shopList.append(shoppingList)
        
print(shopList)


##QUESTION 4
def wordFrequency(sentence):
    word = sentence.split()
    sentencedict = {i:word.count(i) for i in word}
    print(sentencedict)

