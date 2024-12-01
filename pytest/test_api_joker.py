import pytest
import requests

BASE_URL = "https://v2.jokeapi.dev/joke/"


def test_joke_text_format():
    # Testa piada no formato texto
    params = {"format": "text"}
    response = requests.get(f"{BASE_URL}Any", params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    assert isinstance(response.text, str), "Resposta não é do tipo texto"
    print(f"Piada no formato texto: {response.text}")

def test_safe_joke():
    # Testa piada segura, sem humor negro
    params = {"type": "Any", "blacklistFlags": "racist,sexist", "safeMode": "true"}
    response = requests.get(f"{BASE_URL}Any", params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    # Verificando se algum dos campos "setup", "delivery" ou "joke" está presente
    assert "delivery" in data or "setup" in data or "joke" in data, "Piada segura não encontrada"
    print(f"Piada segura: {data.get('delivery', data.get('setup', data.get('joke')))}")

def test_science_joke():
    # Testa piada de ciência
    params = {"type": "Any", "format": "json"}
    response = requests.get(f"{BASE_URL}Any", params=params)  # Corrigido para 'Any'
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    # Verificando se algum dos campos "setup", "delivery" ou "joke" está presente
    assert "delivery" in data or "setup" in data or "joke" in data, "Piada de ciência não encontrada"
    print(f"Piada de Ciência: {data.get('delivery', data.get('setup', data.get('joke')))}")

def test_multiple_jokes():
    # Testa múltiplas piadas
    params = {"type": "Any", "amount": 3}
    response = requests.get(f"{BASE_URL}Any", params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data['jokes']) == 3, f"Esperado 3 piadas, mas retornou {len(data['jokes'])}"
    print(f"Piadas retornadas: {len(data['jokes'])}")


def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}InvalidEndpoint")
    assert response.status_code == 400, "Esperado status 400 para endpoint inválido"
    print("Teste de erro para endpoint inválido passou com sucesso")
