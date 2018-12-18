travel = input("How are you going to university? Bus or Run :")

#T=D/S

def bus():
    time=(4/25)*60
    travelByBus=20+time #2minutes*10stops = 20
    print("It will take",travelByBus,"minutes to get there by bus")

def run():
    distance1=(1/7)*60
    distance2=(2/15)*60
    totalTime=distance1+distance2+distance1
    print("It will take",totalTime,"minutes to get there by running")

if travel == "bus":
    bus()
    travel2 = input("Try run as an alternative: ")
    if travel2 == "run":
        run()
        print("Try running instead it's faster and you'll be more healthy")
    
elif travel == "run":
    run()
    travel2 = input("Try bus as an alternative: ")
    if travel2 == "bus":
        bus()
        print("Stick to running it's much faster")


    
