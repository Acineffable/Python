spend = int(input("Enter the amount you spent:"))
user = input("Are you a student or uni staff:")
if user == "student":
    reduced = spend*(1-0.20)
    extra = input("Are you involved in 121COM:")
    if extra == "yes":
             anotherdiscountoff = reduced * (1-0.05)
             print(anotherdiscountoff)
    else:
             print(reduced)
elif user == "uni staff":
    reduced = spend*(1-0.10)
    extra = input("Are you involved in 121COM:")
    if extra == "yes":
             anotherdiscountoff = reduced * (1-0.05)
             print(anotherdiscountoff)
    else:
             print(reduced)
else:
    print("Your bill is",spend)
    
