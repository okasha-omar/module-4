"""
Name: Mitansh
Date: 05/03/2024
Description: This simple program checks if the user knows the pirate password ("Arrr!").
             If they do, it identifies them as a pirate; otherwise, it greets them
             as a pirate hater.
"""

greeting = input("Hello, possible pirate! What's the password? ")
if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")