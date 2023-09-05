import json

# Create a dictionary of Indian states and capitals
indian_states = {
    "Andhra Pradesh": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}

# Write the dictionary to a JSON file
with open(r"C:\Users\Lenovo\PycharmProjects\AssignmentChallenge1task2\indian_states.json", "w") as file:
    json.dump(indian_states, file)

print("JSON file created successfully.")
