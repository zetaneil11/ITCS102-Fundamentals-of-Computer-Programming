#import demo
import getpass #folder

username = "user1"
password = "Pogi_ako123"

u = input("Input USERNAME ---> ")
p = getpass.getpass("Input PASSWORD ---> ")

if u == username and p == password:
	print("username and password correct")

else:
	print("access denied")
