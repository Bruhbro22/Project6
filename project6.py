num=1
name=str(input("Enter your name in letters only: "))
if name.isalpha():
    print("Hello", name)
else:
    print("Invalid input. Please enter a name with only letters.")