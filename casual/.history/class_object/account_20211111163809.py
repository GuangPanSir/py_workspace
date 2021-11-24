class Account:
    interest_rate = 0.0668

    def __init__(self, owner, amount):
        self.owner = owner
        self.amout = amount

# cls代表类本身，即Account
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

print("计算利息:")