# modelos/assinante.py — quem recebe a newsletter
class Assinante:
    def __init__(self, email):
        self.email = email

    def pode_receber(self) -> bool:
        return True


class Gratis(Assinante):
    def pode_receber(self):
        return True


class Premium(Assinante):
    def pode_receber(self):
        return True
