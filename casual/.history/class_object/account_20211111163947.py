class Account:
    interest_rate = 0.0668

    def __init__(self, owner, amount):
        self.owner = owner
        self.amout = amount

# cls代表类本身，即Account
#类方法属于类，
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt


interest = Account.interest_by(12000.0)
print("计算利息:{0:.4f}".format(interest))
