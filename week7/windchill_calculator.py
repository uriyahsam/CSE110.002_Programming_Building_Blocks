# Windchill Calculator
# Calculates wind chill for a given temperature in Fahrenheit or Celsius
# Adds creative functionality to allow the user to save the results to a text file

def calculate_wind_chill(temp_f, wind_speed):
    """
    Calculate the wind chill based on temperature (F) and wind speed (mph).
    Formula: Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
    """
    return 35.74 + (0.6215 * temp_f) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp_f * (wind_speed ** 0.16))


def celsius_to_fahrenheit(temp_c):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: (°C × 9/5) + 32 = °F
    """
    return (temp_c * 9/5) + 32


def main():
    print("Welcome to the Windchill Calculator!")
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    if unit == 'C':
        temperature = celsius_to_fahrenheit(temperature)
        print(f"Converted temperature: {temperature:.2f}F")
    elif unit != 'F':
        print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
        return

    print("\nWind Chill Values:")
    results = []
    for wind_speed in range(5, 65, 5):  # Wind speeds from 5 to 60 mph, incrementing by 5
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        result = f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F"
        print(result)
        results.append(result)

    # Additional feature: Save results to a file
    save_option = input("\nWould you like to save the results to a file? (Y/N): ").strip().upper()
    if save_option == 'Y':
        with open("windchill_results.txt", "w") as file:
            file.write("\n".join(results))
        print("Results saved to 'windchill_results.txt'.")

    print("Thank you for using the Windchill Calculator!")


if __name__ == "__main__":
    main()
