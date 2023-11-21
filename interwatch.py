import requests
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

url = 'http://46.17.108.113:8666/STH/v1/contextEntities/type/Oximeter/id/urn:ngsi-ld:Oxi:001/attributes/identity?lastN=30'
headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/'
}

response = requests.get(url, headers=headers)

# Verifique se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    data = response.json()

    timestamps = [entry['recvTime'] for entry in data['contextResponses'][0]['contextElement']['attributes'][0]['values']]
    values = [entry['attrValue'] for entry in data['contextResponses'][0]['contextElement']['attributes'][0]['values']]

    # Converter timestamps para objetos de data
    date_objects = [datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ') for timestamp in timestamps]

    # Plotar o gráfico
    plt.plot(date_objects, values, marker='o')
    plt.gcf().autofmt_xdate()  # Rotacionar rótulos do eixo x para melhor legibilidade
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.xlabel('Tempo')
    plt.ylabel('Batimentos')
    plt.title('Gráfico de Batimentos em Função do Tempo')
    plt.show()

else:
    print(f"Erro na solicitação. Código de status: {response.status_code}")
    print(response.text)
