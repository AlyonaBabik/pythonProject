class Wallet:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return f'Клиент: {self.name}. Баланс:{self.money}'

wallet_1 = Wallet("Иван Петров", 50)
print(wallet_1.__str__())
