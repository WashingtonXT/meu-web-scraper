# Importamos a biblioteca requests para fazer requisições na web
import requests

# Definimos o endereço (URL) do site de treino que vamos acessar
url = "https://books.toscrape.com/"

# Fazemos uma requisição do tipo GET (pedindo os dados da página)
resposta = requests.get(url)


if resposta.status_code == 200:
    print("Conexão bem sucedida! ") 
    print(resposta.text[:300])
else:
    print(f"Falha na conexão. Código de status: {resposta.status_code}")