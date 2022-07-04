import requests, json, time

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
obj = json.loads(response.text)
job_token=obj['token']
delay = obj['seconds']
print('Задача создана!')
print(response.text)
ask_job = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token':job_token})
print('Проверяем состояние: ')
print(ask_job.text)
print('Подождём', delay, ' секунд')
time.sleep(delay)
ask_job_again = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token':job_token})
print('Задача выполнена!')
print(ask_job_again.text)