import requests

response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.text)

response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={'method':'GET'})
print(response.text)

response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type', params={'method':'HEAD'})
print(response.text)
print(response.status_code)

methods =['GET', 'POST', 'PUT','DELETE']
for method in methods:
    print(method)
    response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={'method': method})
    print(response.text)
    
    response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': method})
    print(response.text)
    
    response = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': method})
    print(response.text)
    
    response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': method})
    print(response.text)