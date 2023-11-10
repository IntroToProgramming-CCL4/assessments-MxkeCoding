#It's just a redo of exercise 1. It's just this time I removed the else function.
colors = []
input_colors = colors

while input_colors != "quit":
    input_colors = input("Type in toppings: ")
    colors.append(input_colors)