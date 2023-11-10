#This is the list oftoppings
toppings = []
input_toppings = toppings

'''
A loop that tells the user to keep typing what toppings needed
and will keep asking till user types 'quit' which displays the toppings.
It also removes the word quit from the end of the list.
'''
while input_toppings != "quit":
    input_toppings = input("Type in toppings: ")
    toppings.append(input_toppings)
else:
    toppings.pop()
    print(toppings)
