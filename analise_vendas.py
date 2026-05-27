import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor"],
    "Vendas": [10, 5, 2]
}

df = pd.DataFrame(dados)

print("Relatório de vendas")
print(df)

print("\nResumo:")
print(df.describe())
