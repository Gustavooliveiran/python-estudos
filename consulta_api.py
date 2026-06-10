import requests

cep = "01001000"
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()

    print("Dados do endereço:")
    print(f"CEP: {dados['cep']}")
    print(f"Rua: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")

except requests.exceptions.RequestException as erro:
    print(f"Erro ao consultar o CEP: {erro}")
