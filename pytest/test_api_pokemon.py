import pytest
import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_pokemon_by_name():
    # Buscar informações de um Pokémon específico pelo nome
    response = requests.get(f"{BASE_URL}/pokemon/pikachu")
    assert response.status_code == 200, "Erro ao acessar dados do Pokémon"
    data = response.json()
    assert data["name"] == "pikachu", "Nome do Pokémon incorreto"
    assert data["id"] == 25, "ID do Pokémon incorreto"
    print(f"Pokémon encontrado: {data['name']} | ID: {data['id']}")

def test_get_pokemon_by_id():
    # Buscar informações de um Pokémon específico pelo ID
    response = requests.get(f"{BASE_URL}/pokemon/1")  # Bulbasaur
    assert response.status_code == 200, "Erro ao acessar dados do Pokémon"
    data = response.json()
    assert data["name"] == "bulbasaur", "Nome do Pokémon incorreto"
    assert data["base_experience"] > 0, "Experiência base incorreta"
    print(f"Pokémon encontrado: {data['name']} | Experiência base: {data['base_experience']}")

def test_get_pokemon_type():
    # Buscar todos os tipos de Pokémon
    response = requests.get(f"{BASE_URL}/type")
    assert response.status_code == 200, "Erro ao acessar lista de tipos"
    data = response.json()
    assert "results" in data, "Dados de tipos não encontrados"
    assert len(data["results"]) > 0, "Nenhum tipo de Pokémon encontrado"
    print(f"Tipos de Pokémon encontrados: {len(data['results'])}")

def test_get_ability():
    # Buscar informações de uma habilidade específica
    response = requests.get(f"{BASE_URL}/ability/1")  # Stench
    assert response.status_code == 200, "Erro ao acessar dados da habilidade"
    data = response.json()
    assert data["name"] == "stench", f"Nome da habilidade incorreto. Esperado: stench, Recebido: {data['name']}"
    print(f"Habilidade encontrada: {data['name']} | ID: {data['id']}")

def test_invalid_pokemon():
    # Testar com um Pokémon inválido
    response = requests.get(f"{BASE_URL}/pokemon/invalid_name")
    assert response.status_code == 404, "Erro esperado para Pokémon inválido"
    print("Teste de Pokémon inválido bem-sucedido")
