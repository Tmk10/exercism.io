from threading import Lock

class BankAccount():


    def __init__(self):
        self.status = False
        self.balance = 0
        self.lock = Lock()

    def get_balance(self):
        if self.status:
            return self.balance
        else:
            raise ValueError(BankAccount.__name__ + " is closed")


    def open(self):
        self.status = True

    def deposit(self, amount):
        if self.status:
            if amount > -1:
                with self.lock:
                    self.balance +=amount
            else:
                raise ValueError("Cannot deposit negative value")
        else:
            raise ValueError(BankAccount.__name__ + " is closed")

    def withdraw(self, amount):
        if self.status:
            if amount > self.balance:
                raise ValueError("Lack of money to withdraw")
            elif amount > -1:
                with self.lock:
                    self.balance -=amount
            else:
                raise ValueError("Cannot withdraw negative value")

        else:
            raise ValueError(BankAccount.__name__ + " is closed")

    def close(self):
        self.status = False
