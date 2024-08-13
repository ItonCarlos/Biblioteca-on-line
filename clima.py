

# Enviando a requisição para a API
import requests
from datetime import datetime

# Enviando a requisição para a API
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Pato%20Branco&appid=d77c765fe183231b80c00659032e10cf&units=metric")
data = response.json()
#print(data)
# Extraindo informações
cidade = data['name']
temperatura = data['main']['temp']
descricao_clima = data['weather'][0]['description']
horario_atualizacao_unix = data['dt']

# Convertendo o horário de atualização de UNIX timestamp para um formato legível
horario_atualizacao = datetime.fromtimestamp(horario_atualizacao_unix).strftime('%d-%m-%Y %H:%M:%S')

# Imprimindo informações
print(f"Cidade: {cidade}")
print(f"Temperatura: {temperatura} °C")
print(f"Descrição do clima: {descricao_clima}")
print(f"Horário da última atualização: {horario_atualizacao}")
