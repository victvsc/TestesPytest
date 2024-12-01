import pytest
import requests

# Base URL da API JSONPlaceholder
BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("endpoint", [
    f"{BASE_URL}/posts",      # Todos os posts
    f"{BASE_URL}/users",      # Todos os usuários
    f"{BASE_URL}/comments",   # Todos os comentários
    f"{BASE_URL}/albums",     # Todos os álbuns
    f"{BASE_URL}/todos",      # Todas as tarefas
])
def test_api_endpoints(endpoint):
    response = requests.get(endpoint)
    
    # Verificar o status da rota
    assert response.status_code == 200, f"Falha ao acessar a rota: {endpoint} (Status: {response.status_code})"
    print(f"Teste bem-sucedido para a rota: {endpoint}")
    print(f"Status da rota: {response.status_code}\n")

@pytest.mark.parametrize("post_id, expected_title", [
    (1, "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
    (2, "qui est esse"),
    (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut"),
])
def test_post_by_id(post_id, expected_title):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200, f"Falha ao acessar post ID {post_id}"
    data = response.json()
    assert data["title"] == expected_title, f"Esperado: {expected_title}, Recebido: {data['title']}"
    print(f"Post com ID {post_id}: {data['title']} (Status: {response.status_code})\n")

def test_filter_comments_by_post_id():
    # Teste para buscar comentários de um post específico
    post_id = 1
    response = requests.get(f"{BASE_URL}/comments?postId={post_id}")
    assert response.status_code == 200, f"Erro ao buscar comentários para o post ID {post_id}"
    data = response.json()
    assert len(data) > 0, f"Nenhum comentário encontrado para o post ID {post_id}"
    print(f"Comentários encontrados para o post ID {post_id}: {len(data)} (Status: {response.status_code})\n")

def test_user_info_by_id():
    # Teste para verificar informações de um usuário específico
    user_id = 1
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"Erro ao buscar informações do usuário com ID {user_id}"
    data = response.json()
    assert "name" in data and "username" in data, "Nome ou username não encontrados na resposta"
    print(f"Usuário com ID {user_id}: {data['name']} ({data['username']}) (Status: {response.status_code})\n")

def test_album_by_user_id():
    # Teste para buscar álbuns de um usuário específico
    user_id = 1
    response = requests.get(f"{BASE_URL}/albums?userId={user_id}")
    assert response.status_code == 200, f"Erro ao buscar álbuns para o usuário ID {user_id}"
    data = response.json()
    assert len(data) > 0, f"Nenhum álbum encontrado para o usuário ID {user_id}"
    print(f"Álbuns encontrados para o usuário ID {user_id}: {len(data)} (Status: {response.status_code})\n")
