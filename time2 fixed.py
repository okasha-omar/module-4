"""
Name: Okasha Omar Mohammed
Date: 05/03/2024
Description: This program calculates when an alarm will go off based on the current time
             and the number of hours to wait (similar to time.py but with different
             variable names).
"""

str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
