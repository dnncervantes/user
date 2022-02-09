class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

danny = User("Danny")
sara = User("Sara")
matt = User("Matt")

danny.make_deposit(1000)
danny.make_deposit(1000)
danny.make_deposit(1000)
danny.make_withdrawl(3500)
danny.display_user_balance()

sara.make_deposit(5000)
sara.make_deposit(5000)
sara.make_withdrawl(2000)
sara.make_withdrawl(4000)
sara.display_user_balance()

matt.make_deposit(10000)
matt.make_deposit(5000)
matt.make_withdrawl(7000)
matt.make_withdrawl(750)
matt.display_user_balance()

danny.transfer_money(250, matt)