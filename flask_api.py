import pandas as pd
import requests
#import pyspark.pandas as ps 
from flask import Flask, jsonify, request, make_response


# app.config["JSON_SORT_KEYS"] = False

app = Flask(
    __name__
)  # instância o método Flask com o nome do app igual ao nome do arquivo.py



dados = pd.read_csv('./code.csv')
noticias_por_data = pd.read_csv('./noticias_por_data.csv')
noticias_por_fonte = pd.read_csv('./noticias_por_fonte_autor.csv')
aparicoes_keyWords = pd.read_csv('./aparicoes_palavras_chave.csv')

@app.route("/", methods=["GET"])  # define o endpoint da página e qual método ela aceita
def homepage():

    return jsonify({"mensagem": "olá, você está na página principal", "pagina": 1})

@app.route("/dados", methods=["GET"])  # define o endpoint da página e qual método ela aceita
def todos_dados():

    
    return jsonify(
        dados.to_json())

@app.route("/dados/<int:id>", methods = ["GET"])
def retorna_id(id):

    try:
        df_id = dados.loc[[id]].to_json()
        return jsonify(
            df_id)
    except:
        print("id não encontrado")
        return jsonify(
            dados.to_json())

@app.route("/dados/noticias_data", methods=["GET"])  # define o endpoint da página e qual método ela aceita
def noticias_dada():

    
    return jsonify(
        noticias_por_data.to_json())

@app.route("/dados/noticias_fonte", methods=["GET"])  # define o endpoint da página e qual método ela aceita
def noticias_fonte():

    
    return jsonify(
        noticias_por_fonte.to_json())

@app.route("/dados/aparicoes_palavraschaves", methods=["GET"])  # define o endpoint da página e qual método ela aceita
def aparicoes_chaves():

    
    return jsonify(
        aparicoes_keyWords.to_json())


@app.route("/dados", methods = ["POST"])
def recebe_noticia():

    novo_artigo = request.get_json()
    df_novoArtigo = pd.DataFrame(novo_artigo, index = [0])

    df = pd.read_csv('code.csv', index_col=0)

    df = pd.concat([df, df_novoArtigo]
            ).reset_index(drop = True)
    

    if df.duplicated(subset=['title', 'author']).sum() >=0:
        print("Artigo ja existente no banco de dados!")

        return jsonify(novo_artigo)

    # export.
    else:
        df.to_csv('code.csv')

        return jsonify(df.to_json())




##

if __name__ == "__main__":
    app.run(port = 5001, debug=True)