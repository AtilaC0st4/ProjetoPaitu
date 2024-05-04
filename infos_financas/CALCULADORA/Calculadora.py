import numpy as np
import matplotlib.pyplot as plt
import random

SELIC = 12.75
IPCA = 10.2
CDI = SELIC - 0.1

tax_equi_Selic = (1+SELIC/100)**(1/252) - 1
tax_equi_Ipca = (1+IPCA/100)**(1/252) - 1
tax_equi_Cdi = (1+CDI/100)**(1/252) - 1
def invest_selic(montante, tempo):
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante)*(1+tax_equi_Selic)
    return VF
teste1 = invest_selic((300*12/252),1260)

print(f"SELIC: {teste1}") 

def invest_cdi(montante, tempo):
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante) * (1+tax_equi_Cdi)
    return VF
teste2 = invest_cdi((300*12/252), 1260)

print(f"CDI:{teste2}")

def invest_ipca(montante, tempo):
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante) *(1+tax_equi_Ipca)
    return VF
teste3 = invest_ipca((3000*12/252), 1260)

print(f"IPCA : {teste3}")

def invest_porcentagem_cdi(montante, tempo, porcentagem):
    VF = 0
    for cont in range(tempo):
        VF = (VF + montante) * (1+(porcentagem/100 * tax_equi_Cdi))
    return VF
teste4 = invest_porcentagem_cdi((3000*12/252), 1260, 110)

print(f"Porcentagem %CDI: {teste4}")

def invest_Ipca_mais(montante, tempo, mais):
    VF = 0
    taxa_equivalente_Ipca = (1+mais/100) **(1/252) - 1
    for cont in range(tempo):
        VF = (VF + montante) * ((1+tax_equi_Ipca)*(1+taxa_equivalente_Ipca))
    return VF
teste5 = invest_Ipca_mais((300*12/252), 1260, 5.5)

print(f"+IPCA: {teste5}")