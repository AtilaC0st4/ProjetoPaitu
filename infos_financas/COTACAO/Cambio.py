import requests
from datetime import date

def obter_cotacao(moedas):
    link = f"https://economia.awesomeapi.com.br/last/{','.join(moedas)}"
    dados = requests.get(link)
    if dados.status_code == 200:
        return dados.json(), date.today()
    else:
        print("Erro ao obter os dados de cotação!")
        return None, None

def main():
    print("Bem-vindo ao verificador de cotações!")
    moedas = input("Por favor, insira as moedas que deseja verificar, por exemplo: USD-BRL: ").upper().split(",")
    
    cotacao, data_atual = obter_cotacao(moedas)
    
    if cotacao:
        for moeda, valor in cotacao.items():
            print(f"A cotação de {moeda} hoje ({data_atual}) é {valor['high']}")
    else:
        print("Não foi possível obter a cotação.")

if __name__ == "__main__":
    main()
