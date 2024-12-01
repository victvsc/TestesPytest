import pytest
import requests

# BASE URL da API de Makeup
BASE_URL = "https://makeup-api.herokuapp.com/api/v1/products"

def test_get_all_products():
    # Testar a recuperação de todos os produtos
    response = requests.get(BASE_URL + ".json")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum produto encontrado"
    print(f"Número de produtos retornados: {len(data)}")

def test_get_products_by_brand():
    # Testar a busca de produtos por marca
    brand = "maybelline"
    response = requests.get(BASE_URL + f".json?brand={brand}")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, f"Nenhum produto encontrado para a marca {brand}"
    for product in data:
        assert product["brand"] == brand, f"Produto com marca incorreta: {product['brand']}"
    print(f"Produtos encontrados para a marca {brand}: {len(data)}")

def test_get_products_by_category():
    # Testar a busca de produtos por categoria
    category = "lipstick"
    response = requests.get(BASE_URL + f".json?product_type={category}")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, f"Nenhum produto encontrado para a categoria {category}"
    for product in data:
        assert category in product["product_type"], f"Categoria incorreta no produto: {product['product_type']}"
    print(f"Produtos encontrados na categoria {category}: {len(data)}")

def test_get_product_by_id():
    # Testar a recuperação de um produto específico pelo ID
    product_id = 495
    response = requests.get(BASE_URL + f"/{product_id}.json")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["id"] == product_id, f"ID do produto incorreto: {data['id']}"
    print(f"Produto recuperado: {data['name']}")

def test_invalid_product_id():
    # Testar o comportamento ao buscar um produto com ID inválido
    invalid_id = 999999
    response = requests.get(BASE_URL + f"/{invalid_id}.json")
    assert response.status_code == 404, "O status code deveria ser 404 para um ID inválido"
    print("Teste de ID inválido bem-sucedido")
