def is_disarium(number):
	num_str = str(number)
	digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
	return digit_sum == number
if __name__ == '__main__':
	try:
		num = int(input("Enter a number: "))
	except ValueError:
		print("Invalid input. Please enter a valid number.")
	else:
		if is_disarium(num):
			print(f"{num} is a Disarium number.")
		else:
			print(f"{num} is not a Disarium number.")