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
