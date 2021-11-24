class Account:
    interest_rate = 0.0668

    def __init__(self,owner,amount) -> None:
        self.owner = owner
        self.amout = amount

    def interest_by(cls,amt):
        