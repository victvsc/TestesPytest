from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_youtube_search_esbam():
    # Configurar o driver
    driver = webdriver.Chrome()  # Use webdriver.Firefox() se estiver utilizando o Firefox
    driver.maximize_window()

    try:
        # Abrir o YouTube
        driver.get("https://www.youtube.com")
        time.sleep(3)  # Esperar o carregamento inicial da página

        # Localizar a barra de pesquisa
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("ESBAM")
        search_box.send_keys(Keys.RETURN)  # Pressionar Enter para buscar

        time.sleep(5)  # Esperar os resultados carregarem

        # Obter a lista de vídeos nos resultados
        results = driver.find_elements(By.ID, "video-title")

        # Verificar se existem resultados e clicar no primeiro vídeo
        if results:
            print(f"Vídeo encontrado: {results[0].text}")
            results[0].click()  # Clicar no primeiro vídeo
        else:
            raise Exception("Nenhum vídeo encontrado para 'ESBAM'.")

        # Aguardar o carregamento do vídeo
        time.sleep(10)  # Ajuste conforme necessário para verificar a reprodução do vídeo

    except Exception as e:
        print(f"Erro durante o teste: {e}")

    finally:
        # Fechar o navegador
        driver.quit()

# Executar o teste
test_youtube_search_esbam()
