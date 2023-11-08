alien_color1 = "yellow"
alien_color2 = "green"
alien_color3 = "red"

input_color = input("Type what color is the alien: ")

if input_color == alien_color1:
    print("You just earned 5 points!")
elif input_color == alien_color2:
    print("You just earned 10 points!")
elif input_color == alien_color3:
    print("You just earned 15 points!")
else:
    print("You just earned 10 points!")