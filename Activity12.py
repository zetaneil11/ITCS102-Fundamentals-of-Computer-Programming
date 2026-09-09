# multiple if and elif conditions

#Create a python program that would capture age group

name = input("Enter your name ---> ")

age = int(input("Enter your age ---> "))

if age >= 0 and age <= 5:
	print("That age is considered as infant")

elif age >= 6 and age <= 12:
	print("That age is considered as kid")

elif age >= 13 and age <= 15:
	print("That age is considered as pre teen")

elif age >= 16 and age <= 19:
	print("That age is considered as teenager")

elif age >= 20 and age <= 29:
	print("That age is considered as early adult")

elif age >= 30 and age <= 58:
	print("That age is considered as adult")

elif age >= 59 and age <= 150:
	print("That age is considered as senior")

else:
	print("age invalid")
