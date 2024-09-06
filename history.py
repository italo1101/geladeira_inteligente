import datetime

class History:
    def __init__(self):
        self.historico = []

    def adicionar_consumo(self, nome, quantidade):
        consumo = {
            "nome": nome,
            "quantidade": quantidade,
            "data": datetime.date.today()
        }
        self.historico.append(consumo)

    def listar_historico(self):
        for consumo in self.historico:
            print(f"{consumo['quantidade']} unidades de {consumo['nome']} consumidas em {consumo['data']}")
