from flask import render_template,request,url_for
from flask_app import app
from api_use import Tempo



@app.route('/', methods=['POST','GET'])
def home():
    cidades = request.form.get('cidade')
    tempo = Tempo(cidades)
   
    return render_template("index.html",
                         tempo = tempo.pesquisa(),
                         cidade = cidades
                           )