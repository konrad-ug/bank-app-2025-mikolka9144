import unittest

from src.account import Account  # Adjust the import based on your project structure

class TestAccountHistory:


    def test_transaction_standard_transfers(self):
        account = Account("Joe","Smith","")
        account2 = Account("Joe","Smith","")
        account2.balance = 200

        assert account.history == []

if __name__ == '__main__':
    unittest.main()