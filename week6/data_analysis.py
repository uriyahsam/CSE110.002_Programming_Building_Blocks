# Milestone: Data Analysis for Life Expectancy
# Tracks the lowest and highest life expectancy values in the dataset.

# Step 1: Load the dataset
file_path = 'life-expectancy.csv'

try:
    with open(file_path, 'r') as file:
        data = file.readlines()
except FileNotFoundError:
    print("Error: Dataset file not found.")
    exit()

# Step 2: Initialize variables
lowest_life_expectancy = float('inf')  # Start with infinity for minimum comparison
highest_life_expectancy = float('-inf')  # Start with negative infinity for maximum comparison

# Step 3: Iterate through the dataset line by line
for line in data[1:]:  # Skip the header row
    parts = line.strip().split(',')

    try:
        life_expectancy = float(parts[3])  # Column index 3 contains the life expectancy

        # Update lowest and highest life expectancy values
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy

        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy

    except (ValueError, IndexError):
        print(f"Skipping invalid or incomplete row: {line.strip()}")

# Step 4: Display results
print(f"The lowest life expectancy in the dataset is: {lowest_life_expectancy}")
print(f"The highest life expectancy in the dataset is: {highest_life_expectancy}")
