#eligiblity to vote
age = int(input("enter age:"))
country =input("enter country")
if age >= 18 and country in ("kenya, uganda, tanzania") :
    print ("eastern africa citizen, eligible to vote")
else:
    print ("not eligible to vote")
    
