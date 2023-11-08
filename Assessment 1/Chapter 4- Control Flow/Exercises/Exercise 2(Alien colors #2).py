#tells what color is the alien
alien_color = "yellow"

#lets the user type what color is the alien
input_color = input("Type what color is the alien: ")

#if user types correct color, it displays that they earned 5 points
if input_color == alien_color:
    print("You just earned 5 points!")
#if they did not type the correct color, it displays that they earned 10 points 
else:
    print("You just earned 10 points!")
