import numpy as np
import matplotlib.pyplot as plt
import requests

def invest_selic(montante, tempo, taxa, aporte_mensal=0):
    taxa_equi_Selic = (1+taxa/100)**(tempo/365) - 1
    valor_total = montante
    for _ in range(int(tempo)):
        valor_total *= (1 + taxa_equi_Selic)
        valor_total += aporte_mensal
    return round(valor_total, 2)

def invest_cdi(montante, tempo, taxa, aporte_mensal=0):
    taxa_equi_Cdi = (1+taxa/100)**(tempo/365) - 1
    valor_total = montante
    for _ in range(int(tempo)):
        valor_total *= (1 + taxa_equi_Cdi)
        valor_total += aporte_mensal
    return round(valor_total, 2)

def invest_ipca(montante, tempo, taxa, aporte_mensal=0):
    taxa_equi_Ipca = (1+taxa/100)**(tempo/365) - 1
    valor_total = montante
    for _ in range(int(tempo)):
        valor_total *= (1 + taxa_equi_Ipca)
        valor_total += aporte_mensal
    return round(valor_total, 2)

def invest_porcentagem_cdi(montante, tempo, taxa, porcentagem, aporte_mensal=0):
    taxa_equi_Cdi = (1+taxa/100)**(tempo/365) - 1
    valor_total = montante
    for _ in range(int(tempo)):
        valor_total *= (1 + porcentagem/100 * taxa_equi_Cdi)
        valor_total += aporte_mensal
    return round(valor_total, 2)

def invest_Ipca_mais(montante, tempo, taxa, mais, aporte_mensal=0):
    taxa_equi_Ipca = (1+taxa/100)**(tempo/365) - 1
    taxa_equivalente_Ipca = (1+mais/100)**(tempo/365) - 1
    valor_total = montante
    for _ in range(int(tempo)):
        valor_total *= (1 + taxa_equi_Ipca * taxa_equivalente_Ipca)
        valor_total += aporte_mensal
    return round(valor_total, 2)

def get_selic_rate():
    try:
        response = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json")
        data = response.json()
        selic_rate = float(data[-1]['valor']) / 100  
        print(f"Taxa SELIC: {selic_rate}")
        return selic_rate
    except Exception as e:
        print(f"Erro ao obter taxa SELIC: {e}")
        return None

def get_cdi_rate():
    try:
        response = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados/ultimos/1?formato=json")
        data = response.json()
        cdi_rate = float(data[-1]['valor']) / 100  
        print(f"Taxa CDI: {cdi_rate}")
        return cdi_rate
    except Exception as e:
        print(f"Erro ao obter taxa CDI: {e}")
        return None

def get_ipca_rate():
    try:
        response = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados/ultimos/1?formato=json")
        data = response.json()
        ipca_rate = float(data[-1]['valor']) / 100  
        print(f"Taxa IPCA: {ipca_rate}")
        return ipca_rate
    except Exception as e:
        print(f"Erro ao obter taxa IPCA: {e}")
        return None

def calcular_e_listar():
    montante = float(input("Digite o montante do investimento: "))
    tempo_anos = float(input("Digite o período de tempo do investimento (em anos): "))
    aporte_mensal = float(input("Digite o valor do aporte mensal: "))

    tempo_dias = tempo_anos * 365

    selic_rate = get_selic_rate()
    cdi_rate = get_cdi_rate()
    ipca_rate = get_ipca_rate()

    if selic_rate is None or cdi_rate is None or ipca_rate is None:
        print("Não foi possível obter as taxas atualizadas. Por favor, tente novamente mais tarde.")
        return

    print(f"Período: {tempo_anos} anos")

    resultados = {
        "SELIC": invest_selic(montante, tempo_dias, selic_rate, aporte_mensal),
        "CDI": invest_cdi(montante, tempo_dias, cdi_rate, aporte_mensal),
        "IPCA": invest_ipca(montante, tempo_dias, ipca_rate, aporte_mensal),
        "Porcentagem %CDI": invest_porcentagem_cdi(montante, tempo_dias, cdi_rate, 110, aporte_mensal),
        "+IPCA": invest_Ipca_mais(montante, tempo_dias, ipca_rate, 5.5, aporte_mensal)
    }

    resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

    print("Lista de investimentos do melhor ao pior:")
    for investimento, valor in resultados_ordenados:
        print(f"{investimento}: {valor}")

calcular_e_listar()
