#list of orders
sandwich_orders = ["Egg sandwich", "PBJ", "BLT", "nutella sandwich", "tuna sandwich"]

finished_sandwiches = []

#A loop that shows the sandwiches has been made
for current_order in sandwich_orders:
    print("I made your",current_order, "\n")
    
    finished_sandwiches.append(current_order)
    
print("List of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

