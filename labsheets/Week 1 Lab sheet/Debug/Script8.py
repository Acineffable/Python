# This is a script to calculate the variance in a set of 10 numbers
# This is defined as the average square difference from the mean

# Here is the data
n1 = 2
n2 = 4
n3 = 4
n4 = 4
n5 = 5
n6 = 5
n7 = 7
n8 = 9
n9 = 11
n10 = 13

# First calculate the mean average
meanAverage = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10/10

# Next calculate the square deviations
d1 = (n1-meanAverage)**2
d2 = (n2-meanAverage)**2
d3 = (n3-meanAverage)**2
d4 = (n4-meanAverage)**2
d5 = (n5-meanAverage)**2
d6 = (n6-meanAverage)**2
d7 = (n7-meanAverage)**2
d8 = (n8-meanAverage)**2
d9 = (n9-meanAverage)**2
d10 = (n10-meanAverage)**2


# Then take the average of these
var = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10/10

print("Variance: " + str(var))
