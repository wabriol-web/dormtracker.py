print("Dorm Information Log")

room_number = input("Enter your room number: ")
username = input("Enter your name: ")
number_of_roommates = int(input("Enter the number of roommates you have: "))

roommates = []
for i in range(number_of_roommates):
    roommate_name = input(f"Enter the name of roommate #{i + 1}: ")
    roommate_description = input(f"Enter a short description for {roommate_name}: ")
    roommates.append({
        "name": roommate_name,
        "description": roommate_description
    })

almanac = {
    "room_number": room_number,
    "username": username,
    "roommates": roommates
}

print(almanac)
'''Coming Soon: This program will be updated to include a feature that allows users to save their dorm information to a file for future reference. Stay tuned!'''

