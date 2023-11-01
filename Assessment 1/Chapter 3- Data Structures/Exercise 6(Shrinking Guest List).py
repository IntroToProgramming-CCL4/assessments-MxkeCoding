#List of people invited
Names = ["Ronn", "Ralph", "Anas", "Des"]


for i in range(2):
    Names.pop()
    
del Names[:]

#Displays the list of invited people using a for loop
for Name in range(len(Names)):
    print("They have said to only invite two people to the table.")
    print(Names[Name], "You have been invited to this dinner.")
    print("Sadly Andrei can't come to the party, hope you'll enjoy when you get here! \n")
    
