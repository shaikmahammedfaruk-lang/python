from collections import OrderedDict
def check_order(string, reference):
	string_dict = OrderedDict.fromkeys([c for c in string if c in reference])
	reference_dict = OrderedDict.fromkeys(reference)
	return list(string_dict.keys()) == list(reference_dict.keys())
input_string = "hello world"
reference_string = "helo wrd"
if check_order(input_string, reference_string):
	print("The order of characters in the input string matches the reference.")
else:
	print("The order of characters in the input string does not match the reference.")