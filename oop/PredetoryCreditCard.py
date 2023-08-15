from CreditCard import CreditCard


class PredetoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr) -> None:
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def purchase(self, price):
        success = super().purchase(price)
        if not success:
            self._balance += 5
        return success

    def interest(self):
        m_in = self._balance * self._apr / 100
        m_in /= 12
        self._balance += m_in
        return


sayeed_card = PredetoryCreditCard(
    "Sayeed Hamoomi", "SBI", 73409382047209374, 500000, 10
)
print(sayeed_card.purchase(250000))
print(sayeed_card.get_balance())
print(sayeed_card.interest())
print(sayeed_card.get_balance())
