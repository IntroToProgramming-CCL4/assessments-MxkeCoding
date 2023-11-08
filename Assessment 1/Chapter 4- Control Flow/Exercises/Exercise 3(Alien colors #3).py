#tells what color is the alien
alien_color1 = "yellow"
alien_color2 = "green"
alien_color3 = "red"

#lets the user type what color is the alien
input_color = input("Type what color is the alien: ")

#Displays how many points users get depending on the color they input
if input_color == alien_color1:
    print("You just earned 5 points!")
elif input_color == alien_color2:
    print("You just earned 10 points!")
elif input_color == alien_color3:
    print("You just earned 15 points!")
else:
    print("You just earned 10 points!")
