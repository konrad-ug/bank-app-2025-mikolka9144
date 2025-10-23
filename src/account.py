import math

class BaseAccount:
    def __init__(self):
        self.balance = 0
    def transfer_money(self, amount, recipient_account):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
    def express_transfer(self,amount,recipient_account,provision = 0):
        if amount > self.balance:
            return
        self.transfer_money(amount,recipient_account)
        self.balance -= provision


class Account(BaseAccount):
    def __init__(self, first_name, last_name,pesel,promo_code=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        
        if pesel != None and len(pesel) != 11:
            self.pesel = "Invalid"
        else:
            self.pesel = pesel
            if promo_code != None and promo_code.startswith("PROM_") and len(promo_code) == 8 and self.get_age() < 65:
                self.balance += 50
    def get_age(self):
        current_year = 2025 # update this every year pls :)
        year = int(self.pesel[:2])
        if(year > 30):
            year = 1900 + year
        else:
            year = 2000 + year
        return current_year - year
    def express_transfer(self,amount,recipient_account):
        super().express_transfer(amount,recipient_account,1)
    
class CompanyAccount(BaseAccount):
        def __init__(self, company_name, nip_number):
            super().__init__()
            self.company_name = company_name
            if(len(nip_number) != 10):
                self.nip_number = "Invalid"
            else:
                self.nip_number = nip_number
        def express_transfer(self,amount,recipient_account):
            super().express_transfer(amount,recipient_account,5)