import requests
class Test_cookies:
     def test_cookies_method(self):

        response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
        print(response.cookies.items())
        assert 'HomeWork' in response.cookies, 'There is no such cookies'
        assert 'hw_value' in response.cookies.get('HomeWork'), 'There is no such value for a cookie'