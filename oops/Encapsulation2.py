class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return False

        self.balance -= amount
        print(f"Withdrawn ₹{amount}")
        return True

    def transfer_to(self, other_account, amount):
        if self.withdraw(amount):     
            other_account.deposit(amount)  
            print(f"Transferred ₹{amount} to {other_account.owner}")

acc1 = BankAccount("Faruk", 5000)
acc2 = BankAccount("Ali", 2000)

acc1.transfer_to(acc2, 1000)

print("Faruk Balance:", acc1.balance)
print("Ali Balance:", acc2.balance)