for item in range(1,101):
	if item%7 == 0:
		continue
	elif '7' in str(item):
		continue
	else:
		print(item)