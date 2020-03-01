num = 7
unit = 10
for item in range(1,101):
	if not (item % num == 0 or item % unit == num or item // unit == num ):
		print(item)