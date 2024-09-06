from product import Product
from history import History

class Fridge:
    def __init__(self):
        self.estoque_bebidas = []
        self.historico_consumo = History()

    # Adicionar bebida com Controle de Temperatura Inteligente
    def adicionar_bebida(self, nome, quantidade, data_validade, temperatura_ideal):
        categorias_bebidas = ["água", "refrigerante", "suco", "cerveja", "vinho", "leite", "café", "chá"]
        if nome.lower() not in categorias_bebidas:
            print(f"Erro: '{nome}' não é uma bebida válida!")
            return
        bebida = Product(nome, quantidade, data_validade, temperatura_ideal)
        self.estoque_bebidas.append(bebida)
        self.ajustar_temperatura_ideal(bebida)
        print(f"Bebida {nome} adicionada com sucesso!")

    # Controle de Temperatura Inteligente
    def ajustar_temperatura_ideal(self, bebida):
        print(f"Ajustando a temperatura ideal para {bebida.nome}: {bebida.temperatura_ideal}°C")

    def remover_bebida(self, nome, quantidade):
        for bebida in self.estoque_bebidas:
            if bebida.nome == nome:
                if bebida.quantidade >= quantidade:
                    bebida.quantidade -= quantidade
                    self.historico_consumo.adicionar_consumo(nome, quantidade)
                    if bebida.quantidade == 0:
                        self.estoque_bebidas.remove(bebida)
                else:
                    print(f"Erro: quantidade disponível de {bebida.nome} é menor que {quantidade}")
                return
        print(f"Bebida {nome} não encontrada!")

    # Listar bebidas no estoque
    def listar_bebidas(self):
        for bebida in self.estoque_bebidas:
            print(bebida)

    # Notificações de Estoque Baixo
    def notificar_estoque_baixo(self):
        bebidas_baixas = [bebida for bebida in self.estoque_bebidas if bebida.quantidade < 2]
        if bebidas_baixas:
            print("Notificações de Estoque Baixo:")
            for bebida in bebidas_baixas:
                print(f"Atenção! Estoque de {bebida.nome} está baixo: {bebida.quantidade} unidade(s) restante(s).")
        else:
            print("Todos os itens estão com estoque adequado.")

    # Sugestão de Compras
    def sugerir_compras(self):
        bebidas_baixas = [bebida for bebida in self.estoque_bebidas if bebida.quantidade < 2]
        if bebidas_baixas:
            print("Sugestões de Compras:")
            for bebida in bebidas_baixas:
                print(f"Sugestão: Compre mais {bebida.nome}, apenas {bebida.quantidade} unidade(s) no estoque.")
        else:
            print("Estoque de bebidas está suficiente no momento.")

    # Previsão de Consumo
    def prever_consumo(self):
        consumo_semanal = sum([consumo["quantidade"] for consumo in self.historico_consumo.historico])
        if consumo_semanal > 0:
            print(f"Previsão: Com base no histórico de consumo, você deve consumir {consumo_semanal} unidade(s) nesta semana.")
        else:
            print("Sem dados de consumo para prever a demanda.")
