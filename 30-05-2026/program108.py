def reverse(value):
 if isinstance(value, bool):
  return not value
 else:
   return "boolean expected"
print(reverse(False)) 

print(reverse(0)) 