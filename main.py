# ============================================================
# ATIVIDADE - MEDIDAS DE DISPERSÃO COM DADOS DO TABNET
# Tema: Internações hospitalares por ano em Palmas/TO
# Recorte: Capítulo CID-10 XV - Gravidez, parto e puerpério
# Período: 2008 a 2025
# Fonte: TABNET/DATASUS - http://tabnet.datasus.gov.br
# ============================================================
# REGRA: Nenhuma função estatística pronta ou biblioteca de
#        cálculo foi utilizada. Todos os cálculos são manuais.
# ============================================================


# ── LEITURA DO CSV ───────────────────────────────────────────

def ler_csv(caminho):
    # Abre o arquivo e lê todas as linhas
    arquivo = open(caminho, "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    valores = []

    # Percorre as linhas ignorando o cabeçalho (primeira linha)
    for linha in linhas[1:]:
        linha = linha.strip()          # remove espaços e quebras de linha
        if linha:                      # ignora linhas vazias
            partes = linha.split(",")  # separa pelo delimitador ","
            valores.append(float(partes[1]))  # pega a segunda coluna (internações)

    return valores


# ── FUNÇÃO: MÉDIA ────────────────────────────────────────────

def media(lista):
    # Soma todos os valores da lista manualmente
    soma = 0
    for num in lista:
        soma += num

    # Divide a soma pelo total de elementos
    return round(soma / len(lista), 2)


# ── FUNÇÃO: AMPLITUDE ────────────────────────────────────────

def amplitude(lista):
    # Inicia maximo com valor muito baixo e minimo com valor muito alto
    # para garantir que qualquer valor da lista substitua esses extremos
    maximo = -999999
    minimo =  999999

    for num in lista:
        if num > maximo:
            maximo = num   # atualiza o maior valor encontrado
        if num < minimo:
            minimo = num   # atualiza o menor valor encontrado

    # Amplitude = maior valor - menor valor
    return round(maximo - minimo)


# ── FUNÇÃO: DESVIO MÉDIO ─────────────────────────────────────

def desvio_medio(lista):
    med = media(lista)    # calcula a média da lista
    soma = 0

    for num in lista:
        resultado = num - med    # desvio de cada valor em relação à média

        # Garante que o desvio seja positivo (valor absoluto)
        # sem usar a função abs()
        if resultado < 0:
            resultado *= -1

        soma += resultado        # acumula os desvios absolutos

    # Desvio médio = soma dos desvios absolutos / total de elementos
    return round(soma / len(lista), 2)


# ── FUNÇÃO: VARIÂNCIA ────────────────────────────────────────

def variancia(lista):
    med = media(lista)    # calcula a média da lista
    soma = 0

    for num in lista:
        resultado = num - med    # desvio de cada valor em relação à média
        resultado **= 2          # eleva ao quadrado
        soma += resultado        # acumula os quadrados dos desvios

    # Variância amostral: divide por (n - 1) — corrige o viés da amostra
    return round(soma / (len(lista) - 1), 2)


# ── FUNÇÃO: DESVIO PADRÃO ────────────────────────────────────

def desvio_padrao(lista):
    med = media(lista)    # calcula a média da lista
    soma = 0

    for num in lista:
        resultado = num - med    # desvio de cada valor em relação à média
        resultado **= 2          # eleva ao quadrado
        soma += resultado        # acumula os quadrados dos desvios

    # Desvio padrão amostral: raiz quadrada da variância amostral
    # A raiz quadrada é calculada com expoente 0.5, sem usar math.sqrt()
    return round((soma / (len(lista) - 1)) ** 0.5, 2)


# ── FUNÇÃO: COEFICIENTE DE VARIAÇÃO ──────────────────────────

def coeficiente(lista):
    # CV = (desvio padrão / média) * 100
    # Expressa a dispersão em porcentagem em relação à média
    return round((100 * desvio_padrao(lista) / media(lista)), 2)


# ── EXECUÇÃO PRINCIPAL ───────────────────────────────────────

# Lê os dados do arquivo CSV
dados = ler_csv("internacoes_palmas_to.csv")

# Exibe os dados carregados
print("=" * 55)
print("  MEDIDAS DE DISPERSÃO – TABNET/DATASUS")
print("  Internações CID-10 Cap. XV – Palmas/TO (2008–2025)")
print("=" * 55)

print("\nDados carregados do CSV:")
anos = list(range(2008, 2026))
for i in range(len(dados)):
    print(f"  {anos[i]}: {int(dados[i])}")

# Calcula e exibe cada medida
print("\n" + "=" * 55)
print("RESULTADOS")
print("=" * 55)
print(f"  Média:                   {media(dados)}")
print(f"  Amplitude Total:         {amplitude(dados)}")
print(f"  Desvio Médio:            {desvio_medio(dados)}")
print(f"  Variância:               {variancia(dados)}")
print(f"  Desvio Padrão:           {desvio_padrao(dados)}")
print(f"  Coeficiente de Variação: {coeficiente(dados)}%")

# ── INTERPRETAÇÃO ────────────────────────────────────────────

print("\n" + "=" * 55)
print("INTERPRETAÇÃO")
print("=" * 55)

print(f"\n1. Qual foi a média do conjunto de dados?")
print(f"   A média foi de {media(dados)} internações por ano.")

print(f"\n2. A amplitude indica grande variação entre valores?")
print(f"   Sim. A amplitude de {amplitude(dados)} internações mostra")
print(f"   variação considerável entre o menor e o maior valor do período.")

print(f"\n3. O desvio padrão é alto em relação à média?")
print(f"   Não. O desvio padrão ({desvio_padrao(dados)}) representa apenas")
print(f"   {coeficiente(dados)}% da média, indicando dispersão baixa a moderada.")

print(f"\n4. O CV indica dados homogêneos ou heterogêneos?")
cv = coeficiente(dados)
if cv < 15:
    print(f"   Homogêneos. CV = {cv}% (abaixo de 15%).")
elif cv < 30:
    print(f"   Moderadamente homogêneos. CV = {cv}% (entre 15% e 30%).")
else:
    print(f"   Heterogêneos. CV = {cv}% (acima de 30%).")

print(f"\n5. O fenômeno apresenta grande variabilidade ao longo do tempo?")
print(f"   Não. Houve oscilações, mas os valores ficaram concentrados")
print(f"   em torno da média. Destaque para a queda em 2018 (2766)")
print(f"   e o pico em 2014 (5188).")

print("\n" + "=" * 55)
print("Fonte: TABNET/DATASUS – http://tabnet.datasus.gov.br")
print("=" * 55)