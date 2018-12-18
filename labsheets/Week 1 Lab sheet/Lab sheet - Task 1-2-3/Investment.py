#Product A

#investment money
s3=10000
#percentage
i3=1
#year
t3=3
#Compound interest formula for 3 years
valuea=s3*(1+(i3/100))**t3

#percentage
i2=1
#year
t2=2
#compound interest formula for the last 2 years
valuea1=valuea*(1+(i2/100))**t2

#Product B

#investment money
s4=10000
#percentage
i4=1
#year
t4=4
#compound interest formula for the last 4 years
valueb=s4*(1+(i4/100))**t4

#percentage
i1=10
#year
t1=1
#compound interest formula for the last year
valueb1=valueb*(1+(i1/100))**t1
    

#Product C

#investment money
s=10000
#percentage
i=2
#year
t=5
#compound interest formula
valuec=s*(1+(i/100))**t

#comparing the products
if valuea1 > valueb1 and valuea1 > valuec:
    print("Product A is the best option")

if valueb1 > valuea1 and valueb1 > valuec:
    print("Product B is the best option")

if valuec > valuea1 and valuec > valueb1:
    print("Product C is the best option")
