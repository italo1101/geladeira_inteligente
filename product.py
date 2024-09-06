import datetime

class Product:
    def __init__(self, nome, quantidade, data_validade, temperatura_ideal):
        self.nome = nome
        self.quantidade = quantidade
        self.data_validade = data_validade
        self.temperatura_ideal = temperatura_ideal

    def dias_para_vencimento(self):
        hoje = datetime.date.today()
        return (self.data_validade - hoje).days

    def __str__(self):
        dias_validade = self.dias_para_vencimento()
        return (f"Bebida: {self.nome}, Quantidade: {self.quantidade}, "
                f"Dias para vencer: {dias_validade}, "
                f"Temperatura Ideal: {self.temperatura_ideal}°C")
