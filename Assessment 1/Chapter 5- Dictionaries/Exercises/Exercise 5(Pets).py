#List of dicionaries of pets and the owners names
pets = [{'kind': 'Cockatiel','owner': 'Michael'},
        {'kind': 'Frog','owner': 'Mitchel'},
        {'kind': 'Axolotl','owner': 'Mikahel'},
        {'kind': 'Dog','owner': 'Miguel'}]

#displays what type of animal and the name of owner
for pet in pets:
    print("type of Animal:", pet['kind'])
    print("Owner:", pet['owner'], "\n")
