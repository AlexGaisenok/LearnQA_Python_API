import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
array_of_responses=response.history
print('Количество редиректов: ',len(array_of_responses))
print('\nАдреса на которые идёт редирект:\n')
for resp in array_of_responses:
    print(resp.url)
print('Конечный адрес: ', array_of_responses[len(array_of_responses)-1].url)