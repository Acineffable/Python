# Books cost $20 each.  For every 10 ordered the 11th is free.
# Delivery is $10 for the first book and $2 for each additional book.
# What is the total cost cost for 80 books?

numBooks = 80
# Every 11th book is free so
FreeBooks = (80//11)
costperBook = 20

BookTotal = (numBooks-FreeBooks)*costperBook

deliveryTotal = 10 + 2*79

totalCost = BookTotal + deliveryTotal
print("$" + str(totalCost))
