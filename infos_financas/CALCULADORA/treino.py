import requests
import matplotlib.pyplot as plt

def obter_taxa_selic():
    try:
        response = requests.get("https://brasilapi.com.br/api/taxas/v1/selic")
        data = response.json()
        
        valor_selic = data["valor"]
        return valor_selic
    except Exception :
        print("Erro ao obter o valor do SELIC:")
        return None

def obter_taxa_cdi():
    try:
        response = requests.get("https://brasilapi.com.br/api/taxas/v1/cdi")
        data = response.json()
        taxa_cdi = data["valor"]
        return taxa_cdi
    except Exception :
        print("Erro ao obter a taxa CDI:")
        return None

def obter_taxa_ipca():
    try:
        response = requests.get("https://brasilapi.com.br/api/taxas/v1/ipca")
        data = response.json()
        taxa_ipca = data["valor"]
        return taxa_ipca
    except Exception:
        print("Erro ao obter a taxa IPCA:")
        return None

def calcular_investimento(investimento_inicial, aporte_mensal, periodo, taxa_selic, taxa_cdi, taxa_ipca):
    try:
        valor_total_investido = investimento_inicial
        valor_futuro = investimento_inicial
        juros_totais = 0
        juros_por_mes = []

        for _ in range(periodo):
            juros_mensais = (valor_futuro + aporte_mensal) * (taxa_cdi / 100 / 12)
            juros_por_mes.append(juros_mensais)
            juros_totais += juros_mensais

            valor_futuro = valor_futuro + aporte_mensal + juros_mensais

            valor_total_investido += aporte_mensal

        roi = ((valor_futuro - valor_total_investido) / valor_total_investido) * 100

        imposto_renda = juros_totais * 0.15

        valor_liquido = valor_futuro - imposto_renda

        return {
            "valor_futuro": valor_futuro,
            "roi": roi,
            "valor_total_investido": valor_total_investido,
            "juros_por_mes": juros_por_mes,
            "imposto_renda": imposto_renda,
            "valor_liquido": valor_liquido,
            "juros_totais": juros_totais  
        }
    except Exception:
        print("Erro ao calcular investimento:")
        return None

def gerar_grafico(investimentos_ordenados):
    nomes = [investimento[0] for investimento in investimentos_ordenados]
    rois = [investimento[1] for investimento in investimentos_ordenados]

    plt.figure(figsize=(10, 6))
    for nome, roi, resultado in investimentos_ordenados:
        plt.plot(range(1, len(resultado["juros_por_mes"]) + 1), resultado["juros_por_mes"], label=nome)

    plt.xlabel('Mês')
    plt.ylabel('Juros Mensais (R$)')
    plt.title('Evolução dos Juros Mensais')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('investimentos.png')
    plt.show()

investimento_inicial = float(input("Informe o valor do investimento inicial: "))
aporte_mensal = float(input("Informe o valor do aporte mensal: "))
periodo = int(input("Informe o período de investimento em meses: "))

taxa_selic = obter_taxa_selic()
taxa_cdi = obter_taxa_cdi()
taxa_ipca = obter_taxa_ipca()

investimentos = []

resultado_selic = calcular_investimento(investimento_inicial, aporte_mensal, periodo, obter_taxa_selic(), obter_taxa_selic(), obter_taxa_selic())
if resultado_selic:
    investimentos.append(("SELIC", resultado_selic["roi"], resultado_selic))

resultado_cdi = calcular_investimento(investimento_inicial, aporte_mensal, periodo, obter_taxa_cdi(), obter_taxa_cdi(), obter_taxa_cdi())
if resultado_cdi:
    investimentos.append(("CDI", resultado_cdi["roi"], resultado_cdi))

resultado_ipca = calcular_investimento(investimento_inicial, aporte_mensal, periodo, obter_taxa_ipca(), obter_taxa_ipca(), obter_taxa_ipca())
if resultado_ipca:
    investimentos.append(("IPCA", resultado_ipca["roi"], resultado_ipca))

investimentos_ordenados = sorted(investimentos, reverse=True)

for investimento in investimentos_ordenados:
    nome, roi, resultado = investimento
    print(f"Investimento: {nome}")
    print("Valor Futuro:", resultado["valor_futuro"])
    print("ROI:", f"{roi:.2f}%")
    print("Valor Total Investido:", resultado["valor_total_investido"])
    print("Juros Totais Ganhos:", resultado["juros_totais"])  
    print("Imposto de Renda:", resultado["imposto_renda"])
    print("Valor Líquido:", resultado["valor_liquido"])
    print()

visualizar_grafico = input("Deseja visualizar o gráfico dos investimentos? (S/N): ").upper()

if visualizar_grafico == "S":
    gerar_grafico(investimentos_ordenados)
