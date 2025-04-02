# importando bibliotecas
import pandas as pd
import matplotlib as mpl


# Recebendo arquivo CSV com dados de alunos
caminho_arquivo = input("Entre com o caminho do arquivo a ser manejado: ")
try:
  dados = pd.read_csv(caminho_arquivo)
  print(dados)
except FileNotFoundError:
  print(f"Erro: arquivo {caminho_arquivo} não encontrado. Tente novamente!")
except pd.errors.ParserError:
  print(f"Erro: não conseguimos analisar o arquivo {caminho_arquivo}. Verifique se é um arquivo CSV válido!")
# Limpeza de dados

# Consulta aos dados

# Geração dos gráficos (Matplotlib)