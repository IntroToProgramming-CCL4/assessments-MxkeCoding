#variables
size = input("Type in size of shirt: ")
text = input("Type in text on shirt: ")

#function that summarizes the size and text of the shirt
def make_shirt(size,text):
    print("size of shirt: ", size,"\n", "Text on shirt:", text)

#calls out the function
make_shirt(size,text)