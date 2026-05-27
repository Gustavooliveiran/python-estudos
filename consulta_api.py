import requests

url = "https://viacep.com.br/ws/01001000/json/"

resposta = requests.get(url)

dados = resposta.json()

print("Dados do endereço:")
print(dados)
