from fastapi.testclient import TestClient
from app import app

cliente = TestClient(app)

def test_rota_livros():
    resposta = cliente.get('/livros')
    assert resposta.status_code == 200

def test_rota_autores():
    resposta = cliente.get('/autores')
    assert resposta.status_code == 200

def test_rota_categorias():
    resposta = cliente.get('/categorias')
    assert resposta.status_code == 200

def test_rota_pedidos():
    resposta = cliente.get('/pedidos')
    assert resposta.status_code == 200
