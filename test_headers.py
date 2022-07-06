import requests
class Test_headers:
     def test_headers_method(self):

        response = requests.get('https://playground.learnqa.ru/api/homework_header')
        print(response.headers.items())
        assert 'x-secret-homework-header' in response.headers, 'There is no such field'
        assert 'Some secret value' in response.headers.get('x-secret-homework-header'), 'There is no such value for a header'