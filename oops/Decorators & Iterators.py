class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            num = self.current
            self.current += 1

            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                return num

        raise StopIteration
c1 = PrimeIterator(10)
for prime in c1:
    print(prime)