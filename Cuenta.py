class Cuenta:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo
    
    def get_saldo(self):
        return self.saldo

    def get_numero(self):
        return  self.numero_cuenta


    def set_saldo(self,saldo):
        self.saldo=saldo

    def set_numero(self,numero):
        self.numero_cuenta=numero