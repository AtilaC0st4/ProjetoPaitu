import pandas as pd
import matplotlib.pyplot as plt
import requests

def CarregaSELIC(data_inicial, data_final):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=csv&dataInicial={data_inicial}&dataFinal={data_final}"
    serie_SELIC = pd.read_csv(url, sep=";")
    
    serie_SELIC['valor'] = serie_SELIC['valor'].str.replace(',', '.').astype(float)
    
    serie_SELIC.plot.line(x="data", y="valor", title="SELIC taxas ao ano", legend=True)
    plt.show()

def main():
    data_inicial = input("Insira a data inicial no formato (AAAA-MM-DD): ")
    data_final = input("Insira a data final no formato (AAAA-MM-DD): ")
    CarregaSELIC(data_inicial, data_final)

if __name__ == "__main__":
    main()
