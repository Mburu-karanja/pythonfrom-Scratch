import sys
#promp user to enter birth year
birth_year=input("Enter your birth year:")
#calculate age based on birth year
age=2024 -int(birth_year)
#ask for user height in meters
height=float(input("Enter your height in meters:"))
#determine type of each input
print("Data type of birth year:",type(birth_year))
print("Data type of age:",type(age))
print("Data type of height:",type(height))
#determine size of each input
print(sys.getsizeof(birth_year))
print(sys.getsizeof(age))
print(sys.getsizeof(height))
