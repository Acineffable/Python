# Script for working with daily currency data provided by ECB.

# url for ECM data in xml format
url = "http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"

#####################################################################
# In this block of code:
# - Python opens the url
# - reads the data
# - stores it as a string
# - closes the url
import urllib.request
page = urllib.request.urlopen(url)
data_bytes = page.read()
data_string = data_bytes.decode('utf-8')
page.close()
dictionary ={}
#####################################################################

#####################################################################
# In this block of code:
# - Python converts the string into an element tree
# - Extracts  the data and create variables:
# Each variable name is a currency code and each
#   value is the rate for 1 euro.
import xml.etree.ElementTree as ET
data_tree = ET.fromstring(data_string)
for child in data_tree[2][0]:
    countryD = child.attrib
    dictionary[countryD["currency"]]= float(countryD["rate"])
    dictionary["EUR"] = int("1")
    exec("%s = %f" % (countryD["currency"], float(countryD["rate"])))
# Note: there is a much better way for Python to handle such data
#   (called a dictionary) but we havn't met that yet. 
#####################################################################

#####################################################################
#Example:
print("One euro is " + str(GBP) + "GBP (Great British Pounds)")
#####################################################################
#
##A. 500 euros to US dollars
EurotoUSD = 500*(USD)
print("500 euros in US dollars is ", EurotoUSD)

##B. 200 GBP in CNY
ChineseYuan = round(200/GBP,2)
print("200 in Chinese Yuan is", ChineseYuan)

##C.
#XDR as a currency
EUR0=1
XDR = (0.423*(EUR0)) + (12.1*(JPY))+ (0.111*(GBP)) + (0.66*(USD))

value = True
valuetoconvert = int(input("What value do you want to convert?"))
currencyvalue = input("Currency:")
convertTo = input("Currency to convert to:")

while value:
  if currencyvalue and convertTo in dictionary:
    value=False
    if currencyvalue == "EUR":
      convert = dictionary[convertTo]
      print(convert*valuetoconvert)
    elif convertTo == "EUR":
      convert = dictionary[currencyvalue]
      print(valuetoconvert/convert)
    else:
      convertFrom = dictionary[currencyvalue]
      print((valuetoconvert/convertFrom)*dictionary[convertTo])
