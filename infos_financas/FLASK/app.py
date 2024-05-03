from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)


@app.route('/')
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
