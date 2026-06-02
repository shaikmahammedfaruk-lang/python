def mean(n):
    _str = str(n)
    digit_sum = sum(int(digit) for digit in _str)
    digit_count = len(_str)
    digit_mean = digit_sum / digit_count
    return int(digit_mean) 
print(mean(42))
print(mean(12345))
print(mean(666))
