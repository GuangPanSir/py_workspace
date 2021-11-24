class Account:
    # 私有成员变量
    __interest_rate = 0.0668
    interest_rate = 0.0668

    def __init__(self, owner, amount):
        self.owner = owner
        self.__amount = amount

# cls代表类本身，即Account
# 类方法属于类，第一个参数不是self，而是类本身
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

    def desc(self):
        print("{0}金额: {1} 利率: {2}。".format(
            self.owner, self.__amount, Account.__interest_rate))


# 对类方法通过（类名.类方法）进行访问
interest = Account.interest_by(12000.0)
print("计算利息:{0:.4f}".format(interest))

account = Account('Tony', 800000.0)
account.desc()
print(account.__amount)
print()
