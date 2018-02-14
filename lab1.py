"""
Practice with defining functions
lab1.py
Mason Renehan
1/31/2018

"""

def alarm_clock():
	"""
	Calculates ad outputs the time when the alarm goes off based on 
	time current time (in hours) and number of hours to wait for the alarm.
	"""
	current_time_string = input("What is the current time (in hours)? ")
	waiting_time_string = input("How many hours do you have to wait? ")

	current_time_int = int(current_time_string)
	waiting_time_int = int(waiting_time_string)

	hours = current_time_int + waiting_time_int

	timeofday = hours % 24

	print(timeofday)

	print('done') 