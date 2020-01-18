import sqlite3
import os

import datetime
conn = sqlite3.connect('Reminder_db.db')
c=conn.cursor()

# Create table
c.execute("CREATE TABLE IF NOT EXISTS reminders( rem char(30), date1 text)")

# Create a new reminder
def create_rem():
	enter=input("Enter the reminder_name ")	
	enter1=input("Enter the date at which reminder is to be shown ")
	q1="INSERT INTO reminders (rem, date1) VALUES (?, ?)"
	v1=(enter,enter1)
	c.execute(q1,v1)	
	print("Reminder added!")

#update the reminder
def update_rem():
	enter3=input("Enter the reminder_name of the reminder to be updated ")
	enter2=input("Enter the new date ")
	enter4=input("Enter the new time")
	c.execute("UPDATE reminders SET date1 = (?) where rem='"+ enter3 +"'",[enter2])
	

#view the reminders
def view_rem():
	cur = conn.cursor()
	cur.execute("SELECT * FROM reminders")
	rows = cur.fetchall()
	for row in rows:
		print(row)
	
	
# Save  the changes
conn.commit()



#ch = input()


#if(ch != 'y'):

    #exit(0)


print("\n\nWelcome to Reminder app \n")


choices = 4
cont = True


while cont == True:

	choice = 0
    
	print("\nWhat do you want to do ? (press the corresponding choice no.) \n")

	print("1. Add a new reminder in the list \n2. Update the reminder \n3. View all the remainders \n4. Exit the Reminderapp \n")
	while choice <= 0 or choice > choices:

		print(f"\nPlease enter a valid input of choice between 1 and {choices} \n ")

		choice = input()

		try:

			choice = int(choice)
 
		except ValueError:

			choice = 0

			print("OK \n")

	if(choice==1):

		create_rem()

	elif(choice==2):

		update_rem()

	elif(choice==3):

		view_rem()

	else:

		print("Do you want to continue or exit ? (press c to continue and any other key to exit)")	
		cont = input()
		if cont=='e':
			exit()
		elif cont=='c':
			cont=True
		
		else :
			print("Exiting!!!!!")
			print("Exited the Reminder_app")
			exit()

conn.close()

