from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe",pesel="12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
    def test_account_creation_with_pesel(self):
        account = Account("Jane", "Doe",pesel="12345678901")
        assert account.pesel == "12345678901"
    def test_account_creation_with_invalid_pesel(self):
        account = Account("Jane", "Doe",pesel="12345")
        assert account.pesel == "Invalid"

    def test_account_creation_with_promo_code(self):
        account = Account("Jane", "Doe",pesel="80345678901", promo_code="PROM_110")
        assert account.balance == 50   

    def test_account_creation_with_invalid_promo_code(self):
        account = Account("Jane", "Doe",pesel="80345678901", promo_code="test")
        assert account.balance == 0        

    def test_account_creation_with_promo_code_and_too_old_age(self):
        account = Account("Jane", "Doe",pesel="40345678901", promo_code="PROM_110")
        assert account.balance == 0   

    def test_account_creation_with_invalid_promo_code_and_too_old_age(self):
        account = Account("Jane", "Doe",pesel="40345678901", promo_code="test")
        assert account.balance == 0    

    def test_account_creation_without_promo_code(self):
        account = Account("Jane", "Doe",pesel="12345678901")
        assert account.balance == 0