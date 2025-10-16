from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
    def test_account_creation_with_balance(self):
        account = Account("Jane", "Doe", 100)
        assert account.first_name == "Jane"
        assert account.last_name == "Doe"
        assert account.balance == 100