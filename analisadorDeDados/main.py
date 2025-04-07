import pandas as pd
import matplotlib.pyplot as plt

# Solicita o caminho do arquivo CSV com dados de alunos
caminho_arquivo = input("Entre com o caminho do arquivo a ser manejado: ")

try:
    # Verifica se o arquivo é um CSV
    if not caminho_arquivo.lower().endswith('.csv'):
        raise ValueError("O arquivo deve ser um arquivo CSV.")

    # Lê os dados do arquivo
    dados = pd.read_csv(caminho_arquivo)

    print("--------------- Resumo estatístico: ---------------")

    # Conta número de homens e mulheres na coluna 'Gender'
    coluna_genero = dados['Gender']
    count_male = 0
    count_female = 0

    for item in coluna_genero:
        if item == 'Male':
            count_male += 1
        elif item == 'Female':
            count_female += 1

    # Conta registros vazios na coluna 'Parent_Education_Level'
    count_vazio_pel = dados['Parent_Education_Level'].isna().sum()

    print(f"1. O arquivo {caminho_arquivo} tem {len(dados)} entradas.")
    print(f"2. Onde {count_male} são homens e {count_female} são mulheres.")
    print(f"3. A coluna 'Parent_Education_Level' tem {count_vazio_pel} registros vazios.")
    print("--------------------------------------------------")

    input("Pressione Enter para continuar...")

except FileNotFoundError:
    print(f"Erro: arquivo {caminho_arquivo} não encontrado. Tente novamente!")

except pd.errors.ParserError:
    print(f"Erro: não conseguimos analisar o arquivo {caminho_arquivo}. Verifique se é um CSV válido!")

except ValueError as erro_input:
    print(f"Erro: {erro_input}")

# Limpeza de dados
dados.dropna(subset=['Parent_Education_Level'], inplace=True)
dados['Attendance (%)'].fillna(dados['Attendance (%)'].median(), inplace=True)

# Soma da presença
print(f"O somatório da presença: {dados['Attendance (%)'].sum()}")

print("--------------- Consulta de dados: ---------------")

# Seleciona colunas numéricas
colunas_numericas = dados.select_dtypes(include=['number']).columns

for coluna in colunas_numericas:
    print(f"- {coluna}")

# Solicita coluna para análise
opcao = input("Digite o nome da coluna que deseja analisar: ")

while opcao not in colunas_numericas:
    print("--------------- Opção inválida! Tente novamente. ---------------")
    for coluna in colunas_numericas:
        print(f"- {coluna}")
    opcao = input("Digite o nome da coluna que deseja analisar: ")

# Estatísticas da coluna escolhida
print(f"--------------- Estatísticas da coluna {opcao}: ---------------")
print(f"Média: {dados[opcao].mean()}")
print(f"Mediana: {dados[opcao].median()}")
print(f"Moda: {dados[opcao].mode()[0]}")
print(f"Desvio Padrão: {dados[opcao].std()}")

# Gráfico de dispersão: "Horas de Sono" x "Nota Final"
plt.figure(figsize=(8, 6))
plt.scatter(dados['Sleep_Hours_per_Night'], dados['Final_Score'])
plt.title('Gráfico de Dispersão: Horas de Sono x Nota Final')
plt.xlabel('Horas de Sono')
plt.ylabel('Nota Final')
plt.show()

# Gráfico de barras: "Idade" x "Média das Notas Intermediárias"
idade_midterm_mean = dados.groupby('Age')['Midterm_Score'].mean()

plt.figure(figsize=(8, 6))
idade_midterm_mean.plot(kind='bar', color='skyblue')
plt.title('Gráfico de Barras: Idade x Média das Notas Intermediárias')
plt.xlabel('Idade')
plt.ylabel('Média das Notas Intermediárias')
plt.xticks(rotation=0)
plt.show()

# Gráfico de pizza: Distribuição de Idades
idade_bins = [0, 17, 21, 24, float('inf')]
idade_labels = ['Até 17', '18 a 21', '22 a 24', '25 ou mais']
dados['Age_Group'] = pd.cut(dados['Age'], bins=idade_bins, labels=idade_labels)

age_group_counts = dados['Age_Group'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(age_group_counts, autopct='%1.1f%%', startangle=90)
plt.legend(age_group_counts.index, loc="lower left")
plt.title('Gráfico de Pizza: Distribuição de Idades')
plt.show()

print("--------------- FIM DO PROGRAMA ---------------")