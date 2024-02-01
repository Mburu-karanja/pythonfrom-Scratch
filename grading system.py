mark1= int(input("enter mark 1:"))
mark2= int(input("enter mark 2:"))
mark3= int(input("enter mark 3:"))
if mark1>100 and mark2  >100 and mark3  >100:
    
    print("invalid marks enter number between 0 to 100")
elif mark1 <0 and mark2  <0 and mark3  <0:
    print("invalid marks enter number between 0 to 100")

score=(mark1+mark2+mark3)/3
if score <0 :
    print("invalid score")
    
elif score >100:
    print("invalid score")
else:
    print ("avarage score:", score)

if score >=70 and score <=100:
    print("Grade A")
elif score >=60 and score <=69:
    print("Grade B")
elif score >=50 and score <=59:
    print("Grade C")
elif score >=40 and score <=49:
    print("Grade D")
elif score >=0 and score <=39:
    print("Fail")
