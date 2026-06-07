def natural_numbers():
    num = 1

    while True:      # Infinite loop
        yield num
        num += 1
gen = natural_numbers()

for _ in range(10):
    print(next(gen), end=" ")        