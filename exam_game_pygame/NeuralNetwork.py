# import uuid
# import requests
# import json
# from parameters_game import Rooms
# from typing import Dict, Set
#
#
# auth = 'MjYyMWExOTItN2IyMy00NDJkLWJlZmUtZjMxNDIxY2NkM2ZkOjM0ZTNiNDQ4LWZiNTUtNDI2Zi04OWJjLWY2NmUxOTQzZjE0ZQ=='
#
# def get_token(auth_token, scope='GIGACHAT_API_PERS'):
#     rq_uid = str(uuid.uuid4())
#     url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
#     headers = {
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'Accept': 'application/json',
#             'RqUID': rq_uid,
#             'Authorization': f'Basic {auth_token}'
#     }
#     payload = {
#             'scope': scope
#     }
#     try:
#         response = requests.post(url, headers=headers, data=payload, verify=False)
#         return response
#     except requests.RequestException as e:
#         return -1
#
# response = get_token(auth)
# if response != 1:
#    giga_token = response.json()['access_token']
#
# def get_chat_completion(user_message):
#     url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
#     payload = json.dumps({
#         "model": "GigaChat:latest",
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": user_message
#                 }
#             ],
#             "temperature": 1,
#             "top_p": 0.1,
#             "n": 1,
#             "stream": False,
#             "max_tokens": 512,
#             "repetition_penalty": 1,
#             "update_interval": 0
#     })
#     headers = {
#             'Content-Type': 'application/json',
#             'Accept': 'application/json',
#             'Authorization': f'Bearer {giga_token}'
#     }
#     try:
#         response = requests.request("POST", url, headers=headers, data=payload, verify=False)
#         return response
#     except requests.RequestException as e:
#         return None
#
# promt = f"""
# составь рандомный уровень из комнат {Rooms.rooms}, где каждая комната представляет собой кортеж из 4 элементов из 0 и 1,
# каждый элемент это наличие двери в комнате: 1 - есть дверь, 0 - нет двери. В кортеже идёт такая нумерация по индексам:
# 0 индекс - левая дверь, 1 - верхняя дверь, 2 - правая дверь, 3 - нижняя дверь. Чтобы комнаты были связаны между собой,
# у меня есть система координат, где каждая комната имеет свою координату: изначально координата (0, 0), если идти по горизонтали
# вправо, то первое значение увеличивается на 1, влево - уменьшается на 1, если идти по горизонтали вверх, то второе значение
# увеличивается на 1, вниз - уменьшается на 1, таким образом я могу возвращаться в предыдущую комнату. Изначально всегда первая
# комната это {Rooms.rooms[0]}, все комнаты должны быть использованы, комнаты с одиночной дверью должны использоваться больше
# одного раза, чтобы не было моментов, когда дверь есть, но она никуда не ведёт.
# Мне нужно, чтобы ты вывел мне только словарь уровня, где ключ это координата комнаты, а значение это её индекс в {Rooms.rooms}
# и больше ничего.
# Вот пример словаря, но он не идеален: [(0, 0): 0, (1, 0): 1, (1, 1): 3, (1, 2): 2, (2, 2): 7, (1, 3): 4, (-1, 0): 6, (1, -1): 5, (2, 0): 7],
# не генерируй этот же.
# """
# level = get_chat_completion(promt).json()['choices'][0]['message']['content']
# level = eval(level[level.find('{'):level.rfind('}')+1])
# print(level)
# def level_map():
#     return level