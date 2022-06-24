import json
import requests

# string_as_json_format = '{"answer": "Hello, Kate"}'
# obj = json.loads(string_as_json_format)
#
# key = "answer"
# if key in obj:
#     print(obj[key])
# else:
#     print(f"Key {key} is not existed")

response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_response_text = response.json()
print(parsed_response_text["answer"])