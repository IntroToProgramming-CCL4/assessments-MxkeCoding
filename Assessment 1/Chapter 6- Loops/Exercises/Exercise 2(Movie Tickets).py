#tells user to type in the age
age = int(input("Type in the age: "))

#it displays the age group the user has typed in to check the the price of the ticket
if age < 3:
    print("Ticket is free")
elif age < 12:
    print("Ticket is 10$")
elif age > 12:
    print("Ticket is 15$")