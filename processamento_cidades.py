import pandas as pd

# Caminho para o arquivo CSV
csv_path = 'dados/municipio.csv'

# Leitura do arquivo CSV
df = pd.read_csv(csv_path)

# Exibe as primeiras linhas do DataFrame

# Leitura do arquivo de cidades digitais
df_cidadesdigitais = pd.read_csv('dados/dadosabertos_cidadesdigitais_jan.csv', sep=";")


# Replace 'CÓDIGO IBGE' with the actual column name if different
df_merged = pd.merge(df, df_cidadesdigitais, left_on='codigo_ibge', right_on='CÓDIGO IBGE', how='inner')

# Exibe as primeiras linhas do DataFrame mesclado
df_merged.to_csv("dados/cidades_digitais_mesclado.csv")

