from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

# Esse aqui é dos "Fundos de Investimentos : Liquido"

@app.route('/Liquido')
def dados_coletados():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.22912/dados?formato=json"
    response = requests.get(url)
    if response.status_code == 200:
        dados_ativos = response.json()
        return render_template('dados.html', dados=dados_ativos)
    else:
        return "Erro ao conseguir os dados! Status Code: {}".format(response.status_code)

if __name__ == '__main__':
    app.run(debug=True)

# Esse aqui é dos "Fundos de Investimentos : Aquisição"

@app.route('/Aquisicao')
def dados_2():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.22914/dados?formato=json"
    response = requests.get(url)
    if response.status_code == 200:
        dados_ativos = response.json()
        return render_template('dados2.html', dados=dados_ativos)
    else:
        return "Erro ao conseguir os dados! Status Code: {}".format(response.status_code)
    

@app.route("/Aquisicao")
def dados_3():
    url = ""
    response = requests.get(url)
    if response.status_code == 200:
            dados_ativos = response.json()
            return render_template('dados2.html', dados=dados_ativos)
    else:
            return "Erro ao conseguir os dados! Status Code: {}".format(response.status_code)
        