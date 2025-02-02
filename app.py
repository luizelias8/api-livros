import json
from fastapi import FastAPI

app = FastAPI()

def carregar_dados(chave):
    # Carrega o arquivo JSON da raiz do projeto
    caminho_json = 'dados.json'

    try:
        with open(caminho_json, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            # Retorna apenas a lista solicitada
            return dados.get(chave, [])
    except FileNotFoundError:
        return {'erro': 'Arquivo dados.json nao encontrado'}
    except json.JSONDecodeError:
        return {'erro': 'Erro ao decodificar o arquivo JSON'}

@app.get('/livros')
def listar_livros():
    livros = carregar_dados('livros')
    return livros

@app.get('/autores')
def listar_autores():
    autores = carregar_dados('autores')
    return autores

@app.get('/categorias')
def listar_categorias():
    categorias = carregar_dados('categorias')
    return categorias

@app.get('/pedidos')
def listar_pedidos():
    pedidos = carregar_dados('pedidos')
    return pedidos
