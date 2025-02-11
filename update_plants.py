import json

# Load the plants.json file
with open("plants.json", "r") as file:
    plants = json.load(file)

# Update plant stages
for plant in plants:
    if plant["current_stage"] < len(plant["stages"]) - 1:
        plant["current_stage"] += 1

# Save the updated file
with open("plants.json", "w") as file:
    json.dump(plants, file, indent=4)

print("Plant growth updated successfully!")
