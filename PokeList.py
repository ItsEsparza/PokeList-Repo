import csv

# Go from CSV File to list of lists
with open("Pokemon.csv", "r") as data:
    reader = csv.reader(data)
    pokemon_list = list(reader)

# Functionality one
Requested_type = input("Please enter if you want to know the average speed of a legendary or nonlegendary pokemon: ") #Ask user for pokemon type and store it
if Requested_type == "legendary": # Change Requested_Type to match list of lists
    Requested_type = "True"
elif Requested_type == "nonlegendary":
    Requested_type = "False"
else:
    print("Incorrect input")
    exit()


for i in range(0,721): # Transform speed list from string to integer
    pokemon_list[i+1][10] = int(pokemon_list[i+1][10])

average = 0
count = 0

for i in range(0, 722): # Loop to verify if pokemon is the requested type
    if Requested_type == pokemon_list[i+1][12]:
        average += pokemon_list[i+1][10] # If the pokemon is the requested type it adds the value of its speed
        count +=1 # Ammount of requested type pokemons

average /= count # Calculate average
print(f"the average speed is: {average}\n") # Print average

# Functionality Two
printed = []

# List of pokemon elements
print("Pokemon elemnts", end=": ")
for i in range(0, 722):
    if pokemon_list[i+1][2] not in printed: # Verify if Type1 has been printed
        print(pokemon_list[i+1][2], end = ", ")
    printed += [pokemon_list[i+1][2]] # Add printed Type1 to printed list
    if pokemon_list[i+1][3] not in printed: # Verify if Type2 has been printed
        print(pokemon_list[i+1][3], end = ", ")
    printed += [pokemon_list[i+1][3]] # Add printed Type2 to printed list

element = input("\nFrom which element pokemons would you like to get the info: ") # User introduces desired element

print("\n\n")

for i in range(0, 722): # Loop to verify element and if its legendary
    if element == pokemon_list[i+1][2] or element == pokemon_list[i+1][3]:
        if pokemon_list[i+1][12] == "True":
            print(*pokemon_list[i+1])
