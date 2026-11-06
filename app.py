from flask import Flask, request, render_template, redirect, url_for
import database
from funcoes import *



app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    medicamentos = resumo_tratamento()
    return render_template('index.html', medicamentos=medicamentos)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        medicamento = request.form['medicamento']
        posologia = int(request.form['posologia'])
        tempo = int(request.form['tempo'])
        database.adicionar_medicamento(medicamento, posologia, tempo)
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)