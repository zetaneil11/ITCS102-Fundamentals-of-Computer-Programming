#Shipping charges

sender = input("Sender name -> ")
item = input("Type of item -> ")
fragile = bool(input("Is it fragile? -> "))
weight = float(input("Weight -> "))
distance = float(input("Distance -> "))
express = bool(eval(input("Is this express delivery? -> ")))
international = bool(eval(input("Is it international? -> ")))

base_cost = (weight * 2.50) + (distance * 0.15)


if weight <= 2.0 and distance <= 100 and express == False and international == False:
	total = 0
elif international == True and express == True:
	total = (base_cost * 1.40) + 50
elif express or (international and weight > 20):
	total = (base_cost * 1.20) + 25
elif weight > 30 or distance > 1000:
	total = base_cost + 30
else:
	total = base_cost

print("Total shipping charge -> $",total)
