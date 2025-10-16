class Account:
    def __init__(self, first_name, last_name,pesel,promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        if promo_code != None and promo_code.startswith("PROM_") and len(promo_code) == 8:
            self.balance += 50
        if pesel != None and len(pesel) != 11:
            self.pesel = "Invalid"
        else:
            self.pesel = pesel