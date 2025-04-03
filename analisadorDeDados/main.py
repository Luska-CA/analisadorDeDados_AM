# importando bibliotecas
import pandas as pd
import matplotlib as plt


# Recebendo arquivo CSV com dados de alunos
caminho_arquivo = input("Entre com o caminho do arquivo a ser manejado: ")

try:
    # Checando se o arquivo recebido é .csv
    if not caminho_arquivo.lower().endswith('.csv'):
        raise ValueError("O arquivo deve ser um arquivo CSV.") # levanta uma exeção de ValueError (erro de entrada)

    dados = pd.read_csv(caminho_arquivo)

    print("---------------Resumo estatístico: ---------------")
    # contando número de homens e mulheres na coluna 'Gender'
    coluna_genero = dados['Gender']
    count_Male = 0
    count_Female = 0
    for item in coluna_genero:
        if item == 'Male': count_Male+= 1
        elif item == 'Female': count_Female+= 1

    # contando número de registros vazios na coluna 'Parent_Education_Level'
    count_vazio_PEL = dados['Parent_Education_Level'].isna().sum()

    print(f"O arquivo {caminho_arquivo} tem {len(dados)} entradas,")
    print(f"onde {count_Male} são homens e {count_Female} são mulheres.")
    print(f"A coluna ['Parent_Education_Level'] tem {count_vazio_PEL} registros vazios.")
    print("--------------------------------------------------")
    input("Pressione Enter para continuar...")
    

except FileNotFoundError:
    print(f"Erro: arquivo {caminho_arquivo} não encontrado. Tente novamente!")
except pd.errors.ParserError:
    print(f"Erro: não conseguimos analisar o arquivo {caminho_arquivo}. Verifique se é um arquivo CSV válido!")
except ValueError as erroInput: # recebendo ValueError
    print(f"Erro: {erroInput}")

# Limpeza de dados
dados.dropna(subset=['Parent_Education_Level'], inplace=True)
dados['Attendance (%)'].fillna(dados['Attendance (%)'].median(), inplace=True)

print(f"O somatório da presença: {dados['Attendance (%)'].sum()}")

print("---------------Consulta de dados: ---------------")
colunas_numericas = dados.select_dtypes(include=['number']).columns # seleciona apenas as colunas numéricas do arquivo

for coluna in colunas_numericas:
    print("- " + coluna)

opcao = input("Digite o nome da coluna que deseja analisar: ")

while opcao not in colunas_numericas:
    print("---------------Opção inválida! Tente novamente.---------------")
    for coluna in colunas_numericas:
        print("- " + coluna)
    opcao = input("Digite o nome da coluna que deseja analisar: ")
        
print(f"---------------Estatísticas da coluna {opcao}: ---------------")
print(f"Média: {dados[opcao].mean()}")
print(f"Mediana: {dados[opcao].median()}")
print(f"Moda: {dados[opcao].mode()[0]}")
print(f"Desvio Padrão: {dados[opcao].std()}")

# Geração dos gráficos (Matplotlib)


# Funções
