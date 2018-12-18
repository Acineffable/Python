cut1 = "|"
cut2 = "-"
list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
print("x", "\t", cut1, str(list)[1:-1])
print(cut2*60)

for i in list:
    multiply = list[i]*i
    print(i, "\t", cut1, multiply)
    i+=1
    
