#electric bill calc

CustomerID= int(input("enter ID:"))
CustomerName= str(input("enter Name:"))
units= float(input("enter units consumed:"))
def check_number(units):
    if units <= 199:
       return units*1.20
    elif units >= 200 and units < 400:
        return units*1.50
    elif units > 400 and units < 600 :
        return units*1.80
    else: 
          return units*2.00
total_bill=check_number(units)
print("the total bill is:", total_bill, "for:", CustomerName, "ID:", CustomerID)  