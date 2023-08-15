class CreditCard:
    def __init__(self, customer, bank, account, limit) -> None:
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def purchase(self, price):
        if self._limit < price + self.get_balance():
            return False
        self._balance += price
        return True

    def mk_payment(self, bill):
        self._balance -= bill
        return True


sayeed_card = CreditCard("Sayeed Hamoomi", "SBI", 73409382047209374, 500000)
ark_card = CreditCard("ARK", "DBS", 73345382047209374, 50000000)
print(sayeed_card.get_balance())
print(sayeed_card.get_limit())
print(sayeed_card.purchase(250000))
print(sayeed_card.get_balance())
print(sayeed_card.purchase(250000))
print(sayeed_card.get_balance())

print(sayeed_card.mk_payment(250000))
print(sayeed_card.get_balance())
