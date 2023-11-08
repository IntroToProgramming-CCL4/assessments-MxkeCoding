Major_rivers = {'nile': 'egypt', 'amazon':'south america','mississippi':'america'}

#displays a sentence about each river
for river, country in Major_rivers.items():
    print("The", river ,"runs through" ,country)

#displays the name of each river
print("\nList of rivers:")
for river in Major_rivers.keys():
    print(river)

#displays the country of each river
print("\nList of countries:")
for country in Major_rivers.values():
    print(country)
