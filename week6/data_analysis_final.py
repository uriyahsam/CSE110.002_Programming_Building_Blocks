"""
This program analyzes life expectancy data. In addition to meeting the core requirements, 
it allows the user to type in a country to see the minimum, maximum, and average life expectancy for that country across all years.
"""

file_path = "life-expectancy.csv"

# Read the dataset
data = []
with open(file_path, "r") as file:
    header = file.readline()  # Skip the header line
    for line in file:
        parts = line.strip().split(",")
        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        data.append((entity, year, life_expectancy))

# Prompt user for a year
year_of_interest = int(input("Enter the year of interest: "))

# Calculate overall min and max life expectancy
overall_min = min(data, key=lambda x: x[2])
overall_max = max(data, key=lambda x: x[2])

# Display overall statistics
print(f"\nThe overall max life expectancy is: {overall_max[2]:.3f} from {overall_max[0]} in {overall_max[1]}")
print(f"The overall min life expectancy is: {overall_min[2]:.2f} from {overall_min[0]} in {overall_min[1]}")

# Filter data for the specified year
year_data = [entry for entry in data if entry[1] == year_of_interest]

if year_data:
    # Calculate average, min, and max for the specified year
    avg_life_expectancy = sum(entry[2] for entry in year_data) / len(year_data)
    year_min = min(year_data, key=lambda x: x[2])
    year_max = max(year_data, key=lambda x: x[2])

    # Display year-specific statistics
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_life_expectancy:.2f}")
    print(f"The max life expectancy was in {year_max[0]} with {year_max[2]:.3f}")
    print(f"The min life expectancy was in {year_min[0]} with {year_min[2]:.3f}")
else:
    print(f"\nNo data available for the year {year_of_interest}.")

# Allow the user to analyze a specific country
country_of_interest = input("\nEnter the country of interest: ").strip().title()
country_data = [entry for entry in data if entry[0] == country_of_interest]

if country_data:
    avg_life_expectancy_country = sum(entry[2] for entry in country_data) / len(country_data)
    country_min = min(country_data, key=lambda x: x[2])
    country_max = max(country_data, key=lambda x: x[2])

    print(f"\nFor {country_of_interest}:")
    print(f"The average life expectancy across all years was {avg_life_expectancy_country:.2f}")
    print(f"The max life expectancy was {country_max[2]:.3f} in {country_max[1]}")
    print(f"The min life expectancy was {country_min[2]:.3f} in {country_min[1]}")
else:
    print(f"\nNo data available for {country_of_interest}.")
