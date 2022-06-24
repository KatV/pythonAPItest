# from json.decoder import JSONDecodeError
import requests
#
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")

# response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(first_response.url)
# print(second_response.url)

payload = {"login": "secret_login", "password": "secret_pass2"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookies_value = response1.cookies.get('auth_cookie')
cookies = {}
if cookies_value is not None:
    cookies.update( {'auth_cookie': cookies_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)