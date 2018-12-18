# UK Hydrocarbon Duty (Fuel Tax) is 57.95 pence per litre of petrol.
# VAT (sales tax) is also charged on both the fuel and the duty.

# A garage sells petrol at 37.88p a litre before tax.
# A customer purchases 60 litres of petrol.  Calculate the total cost and how much of that is tax (all to nearest pence).

pricePerL = 37.88    # In pence before tax
quantityL = 60        # Number of litres bought

print("Fuel: £" + str(round(pricePerL*quantityL,2))) # cost before tax
print("Tax: £" + str(round((quantityL*57.95/100)*20 + (pricePerL*quantityL/100)*20,2))) # tax
print("-------")
print("Total: £" + str( round(pricePerL*quantityL,2) + round(quantityL*57.95/100)*20 + pricePerL*quantityL/100*20,2) ) ) # total
