import numpy as np
import matplotlib.pyplot as plt

def invest_selic(montante, tempo, taxa):
    taxa_equi_Selic = (1+taxa/100)**(1/252) - 1
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante)*(1+taxa_equi_Selic)
    return VF

def invest_cdi(montante, tempo, taxa):
    taxa_equi_Cdi = (1+taxa/100)**(1/252) - 1
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante) * (1+taxa_equi_Cdi)
    return VF

def invest_ipca(montante, tempo, taxa):
    taxa_equi_Ipca = (1+taxa/100)**(1/252) - 1
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante) *(1+taxa_equi_Ipca)
    return VF

def invest_porcentagem_cdi(montante, tempo, taxa, porcentagem):
    taxa_equi_Cdi = (1+taxa/100)**(1/252) - 1
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante) * (1+(porcentagem/100 * taxa_equi_Cdi))
    return VF

def invest_Ipca_mais(montante, tempo, taxa, mais):
    taxa_equi_Ipca = (1+taxa/100)**(1/252) - 1
    taxa_equivalente_Ipca = (1+mais/100) **(1/252) - 1
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante) * ((1+taxa_equi_Ipca)*(1+taxa_equivalente_Ipca))
    return VF

def calcular_e_listar():
    montante = float(input("Digite o montante do investimento: "))
    tempo = int(input("Digite o período de tempo do investimento (em dias): "))
    taxa = float(input("Digite a taxa de juros (%): "))

    resultados = {
        "SELIC": invest_selic(montante, tempo, taxa),
        "CDI": invest_cdi(montante, tempo, taxa),
        "IPCA": invest_ipca(montante, tempo, taxa),
        "Porcentagem %CDI": invest_porcentagem_cdi(montante, tempo, taxa, 110),
        "+IPCA": invest_Ipca_mais(montante, tempo, taxa, 5.5)
    }

    # Ordenar os resultados do melhor ao pior
    resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

    print("Lista de investimentos do melhor ao pior:")
    for investimento, valor in resultados_ordenados:
        print(f"{investimento}: {valor}")

calcular_e_listar()
