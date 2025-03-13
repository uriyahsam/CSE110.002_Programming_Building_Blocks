"""
This program will create a properly formatted ID badge
using the information provided by the user.
"""
print("Welcome to the ID Badge Generator")
print("Please enter the following information:")
print()
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email_address = input("Enter your email address: ")
phone_number = input("Enter your phone number: ")
job_title = input("Enter your job title: ")
id_number = input("Enter your ID number: ")
hair_color = input("Enter your hair color: ")
eye_color = input("Enter your eye color: ")
month = input("Enter the month you started: ")
training = input("Have you completed the training? ")


print()
print()
print("\nThe ID Card is: ")
print(f"--------------------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.capitalize()}")
print(f"ID: {id_number}")
print()
print(email_address.lower())
print(phone_number)
print()
print(f"Hair: {hair_color:24} Eyes: {eye_color}") 
print(f"Month: {month:23} Training: {training}")
print(f"--------------------------------------------------")