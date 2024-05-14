import requests
import json
import matplotlib.pyplot as plt

def Aquisicao(data_inicial, data_final):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.22914/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
    response = requests.get(url)
    if response.status_code == 200:
        dados_ativos = response.json() 
        if not dados_ativos:
            print("Não há dados disponíveis para o intervalo de datas especificado.")
            return None
        print("Dados de Aquisição coletados:")
        print(dados_ativos)
        return dados_ativos
    else:
        print("Erro ao conseguir os dados de Aquisição!. Status Code:", response.status_code)
        return None



def plotar_grafico(dados, tipo):
    x = [d['data'] for d in dados] 
    y = [d['valor'] for d in dados]

    plt.bar(x, y, color='skyblue')
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.title(f'Gráfico de Barras - {tipo}')



    plt.show()
    

def main():
    print("Escolha o tipo de dados que deseja consultar:")
    print("1 - Aquisição")

    opcao_tipo = input("Digite o número correspondente ao tipo de dados que deseja consultar: ")

    if opcao_tipo == "1":
        tipo = "Aquisição"
    else:
        print("Opção inválida!")
        return

    data_inicial = input("Insira a data inicial no formato (DD/MM/AAAA): ")
    data_final = input("Insira a data final no formato (DD/MM/AAAA): ")

    if opcao_tipo == "1":
        dados = Aquisicao(data_inicial, data_final)
    else:
        print("Opção inválida!")
        return

    if dados is not None:
        visualizar_grafico = input("Deseja visualizar os dados através de um gráfico? (S/N): ")
        if visualizar_grafico.upper() == "S":
            plotar_grafico(dados, tipo)

if __name__ == "__main__":
    main()
