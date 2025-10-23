from src.account import Account


class TestAccount:
    def setup_method(self):
        self.ext_account = Account("John","Doe","321")
        self.ext_account.balance = 100
        self.recv_account = Account("John","Trump","123")
        self.recv_account.balance = 10

    def test_normal_transfer(self):
        self.setup_method()
        self.ext_account.transfer_money(50, self.recv_account)
        assert self.ext_account.balance == 50
        assert self.recv_account.balance == 60

    def test_insufficient_money_transfer(self):
        self.setup_method()
        self.ext_account.transfer_money(500000, self.recv_account)
        assert self.ext_account.balance == 100
        assert self.recv_account.balance == 10