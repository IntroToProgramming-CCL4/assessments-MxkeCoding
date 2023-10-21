#This displays the desired output with multiple print functions

print("This is the first version: \n\n", str.lstrip("\t\ttwinkle, twinkle, little star,\t"))
print("\tHow I wonder what you are!\t")
print(str.rstrip("\t\tUp above the world so high,\t"))
print(str.rstrip("\t\tLike a diamond in the sky.\t"))
print(str.lstrip("\t\tTwinkle, twinkle, little star,\t"))
print("\tHow I wonder what you are\t")

#This displays the desired output with a single print function
print("\n\n", "This is the second version: \n\n", str.lstrip("\t\ttwinkle, twinkle, little star,\t") \
    , "\n\tHow I wonder what you are!\t", str.rstrip("\n\t\tUp above the world so high,\t") \
    , str.rstrip("\n\t\tLike a diamond in the sky.\t"), "\n", str.lstrip("\t\tTwinkle, twinkle, little star,\t") \
    , "\n\tHow I wonder what you are\t")