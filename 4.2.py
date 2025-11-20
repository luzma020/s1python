class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance!")

# ---- User Input ----
acc_no = int(input("Account Number: "))
name = input("Name: ")
acc_type = input("Account Type: ")
balance = float(input("Opening Balance: "))

acc = BankAccount(acc_no, name, acc_type, balance)

d = float(input("Enter amount to deposit: "))
acc.deposit(d)

w = float(input("Enter amount to withdraw: "))
acc.withdraw(w)

print("\nUpdated Balance:", acc.balance)
