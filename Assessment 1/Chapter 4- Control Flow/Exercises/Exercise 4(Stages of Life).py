#tells user to type in the age
age = int(input("Type in the age: "))

#it displays the age group the user has typed in to check the age
if age < 2:
    print("it is a baby")
elif age < 4:
    print("it is a toddler")
elif age < 13:
    print("it is a kid")
elif age < 20:
    print("it is a teenager")
elif age < 65:
    print("it is an adult")
elif age >= 65:
    print("it is an elder")
