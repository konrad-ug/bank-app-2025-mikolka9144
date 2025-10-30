import math

class Account:
    def __init__(self, first_name, last_name,pesel,promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.history = []
        self.balance = 0
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