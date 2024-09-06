from fridge import Fridge
import datetime

# Criando a geladeira
minha_geladeira = Fridge()

# Adicionando bebidas
minha_geladeira.adicionar_bebida("Cerveja", 6, datetime.date(2024, 9, 15), 4)
minha_geladeira.adicionar_bebida("Suco", 1, datetime.date(2024, 9, 10), 5)
minha_geladeira.adicionar_bebida("Refrigerante", 5, datetime.date(2024, 10, 1), 7)

# Listando bebidas no estoque
print("\nEstoque de bebidas atual:")
minha_geladeira.listar_bebidas()

# Notificações de Estoque Baixo
print("\nNotificações de Estoque Baixo:")
minha_geladeira.notificar_estoque_baixo()

# Removendo bebida (consumo)
print("\nRemovendo 1 unidade de 'Cerveja':")
minha_geladeira.remover_bebida("Cerveja", 2)

# Sugestão de Compras
print("\nSugestões de Compras:")
minha_geladeira.sugerir_compras()

# Previsão de Consumo
print("\nPrevisão de Consumo:")
minha_geladeira.prever_consumo()

# Listando histórico de consumo
print("\nHistórico de Consumo:")
minha_geladeira.historico_consumo.listar_historico()
