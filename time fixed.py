"""
Name: Okasha Omar Mohammed
Date: 05/03/2024
Description: This program calculates what time it will be after a specified number
             of hours have passed from the current time (given in 24-hour format).
"""

currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)
