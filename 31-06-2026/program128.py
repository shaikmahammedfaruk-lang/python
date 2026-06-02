def multiply_nums(nums_str):
    nums = [int(num) for num in nums_str.split(", ")]
    result = 1
    for num in nums:
        result *= num
    return result
print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("5, 6, 7, 8"))