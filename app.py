from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_senha', methods=['POST'])
def gerar_senha():
    tamanho = int(request.form['tamanho'])
    tipo = int(request.form['tipo'])

    if tipo == 1:
        valores = string.ascii_lowercase
    elif tipo == 2:
        valores = string.ascii_letters
    elif tipo == 3:
        valores = string.ascii_letters + string.digits
    elif tipo == 4:
        valores = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Digite uma alternativa válida."

    senha = ''.join(random.choice(valores) for _ in range(tamanho))

    return render_template('senha.html', senha=senha)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


