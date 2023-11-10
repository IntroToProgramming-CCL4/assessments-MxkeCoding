#list of orders
sandwich_orders = ['Egg sandwich', 'pastrami sandwich', 'PBJ', 'pastrami sandwich', 'BLT', 'pastrami sandwich', 'nutella sandwich', 'tuna sandwich']
finished_sandwiches = []

#prints that the deli has ran out of pastrami
print("The deli  has ran out of pastrami")

#checks the orders and removes 'pastrami sandwich' from it
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

#A loop that shows the sandwiches has been made
for current_order in sandwich_orders:
    print("I made your",current_order, "\n")
    
    finished_sandwiches.append(current_order)

print("List of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich,"\n")

