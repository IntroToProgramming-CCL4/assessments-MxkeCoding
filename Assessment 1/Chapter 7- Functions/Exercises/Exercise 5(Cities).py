#the function
def describe_city(city = 'manila',country = 'philippines'):
    print("The city", city, "is from the", country)
    
#calls out function with default elements from variables
describe_city()

#calls out function but the city variable element has changed to laguna
describe_city('Laguna')

#calls out function but the value elements is not using default elements
describe_city('dubai', 'UAE')