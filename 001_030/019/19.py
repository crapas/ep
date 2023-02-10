import math

def days_in(from_y, to_y):
	day_sum = 0
	for i in range(from_y, to_y + 1):
		if i % 4 == 0 and i % 400 != 0:
			day_sum += 366
		else:
			day_sum += 365
	return day_sum

d1 = days_in(1900, 1900) 
d2 = days_in(1900, 2000)

day_from_1900_to_1900 = days_in(1900, 1900)
day_from_1900_to_2000 = days_in(1900, 2000)



sunday_from_1899_last_to_1900 = math.ceil((day_from_1900_to_1900 + 1) / 7)
sunday_from_1899_last_to_2000 = math.ceil((day_from_1900_to_2000 + 1) / 7)

print(sunday_from_1899_last_to_2000 - sunday_from_1899_last_to_1900)
