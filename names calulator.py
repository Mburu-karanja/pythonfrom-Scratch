#list sorting and total names calculation
names = input("Enter a list of names, separated by spaces: ").split()

names = sorted(set(names)) # remove duplicates and sort in alphabetical order

print("Sorted list of names:")

for name in names:
    print(name)
print("Total number of names entered: ", len(names))