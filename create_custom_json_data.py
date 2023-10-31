import random
import json

# Function to generate a random 10-digit number for param1
def generate_param1():
    return random.randint(10**9, (10**10) - 1)

# Function to generate a random 3-digit number for param2
def generate_param2():
    return random.randint(100, 999)

# Generate a list of JSON objects
num_objects = 10  # You can change this to the number of objects you want
json_objects = []

for _ in range(num_objects):
    param1 = generate_param1()
    param2 = generate_param2()
    
    json_object = {
        "instructions": f"I need info about param1 {param1} param2 {param2}",
        "input": "",
        "output": f"param1 {param1} param2 {param2}"
    }
    
    json_objects.append(json_object)

# Save the list of JSON objects to a JSON file
with open("output.json", "w") as json_file:
    json.dump(json_objects, json_file, indent=4)

print("JSON objects saved to 'output.json'.")
