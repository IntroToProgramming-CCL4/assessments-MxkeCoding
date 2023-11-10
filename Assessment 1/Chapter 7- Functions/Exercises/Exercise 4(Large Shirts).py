#function that summarizes the size and text of the shirt
def make_shirt(size = 'Large',text = 'I love python'):
    print("size of shirt: ", size, "\nText on shirt:", text)

#calls out the function
make_shirt()

#calls out the function with different element in variable
make_shirt(size = 'medium')

#calls out the function with different element in both variables
make_shirt(size = 'small', text = 'Keep Coding!')