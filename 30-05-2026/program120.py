def compound_interest(p, t, r, n):
    a = p * (1 + (r / n)) ** (n * t)
    return round(a, 2)
print(compound_interest(1000, 1, 0.05, 12))
print(compound_interest(1500, 2, 0.043, 4))
