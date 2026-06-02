import math
C = 50
H = 30
def calculate_Q(D):
	return int(math.sqrt((2 * C * D) / H))
input_sequence = input("Enter comma-separated values of D: ")
D_values = [s.strip() for s in input_sequence.split(',') if s.strip()]
result = [calculate_Q(int(D)) for D in D_values]
print(','.join(map(str, result)))