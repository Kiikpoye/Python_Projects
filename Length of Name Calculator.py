#This code calculates the number of characters in name.

print("Length of Name Calculator\n")
name = input("Enter your full name:\n")
count = 0
for i in name:
    if(i.isalpha()):
        count = count + 1
print(f"\nYour name has {count} characters.")
input()
