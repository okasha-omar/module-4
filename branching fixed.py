"""
Name: okasha omar mohammed
Date: 05/03/2024
Description: This program greets a time traveler based on their year of origin.
             It categorizes the year into past (before 1900), present (1900-2020),
             or future (after 2020) and displays an appropriate message.
"""

year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print('Woah, that\'s the past!')
elif year > 1900 and year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")
