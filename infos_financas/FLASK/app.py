from flask import Flask, render_template
 
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html') 

# @app.route('/enviar')
# def enviar():

    #     variaveis de acordo com o forms para salvar 
    
    # return 


 
 
 
 
if __name__ == '__main__':
    app.run()