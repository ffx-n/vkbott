import json

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard_start = {
    "one_time": False,
    "buttons": [
        [get_button(label="Начать опрос", color="positive"), get_button(label="Начать опрос", color="positive")]
    ]
}

keyboard_start = json.dumps(keyboard_start, ensure_ascii=False).encode('utf-8')
keyboard_start = str(keyboard_start.decode('utf-8'))


keyboard_first = {
    "one_time": False,
    "buttons": [
        [get_button(label="Apple", color="positive"), get_button(label="LG", color="positive")],
        [get_button(label="Samsung", color="positive"), get_button(label="Huawei", color="positive")]
    ]
}

keyboard_first = json.dumps(keyboard_first, ensure_ascii=False).encode('utf-8')
keyboard_first = str(keyboard_first.decode('utf-8'))

keyboard_second = {
    "one_time": False,
    "buttons": [
        [get_button(label="Omega", color="positive"), get_button(label="Rolex", color="positive")],
        [get_button(label="Longines", color="positive"), get_button(label="Breguet", color="positive")]
    ]
}

keyboard_second = json.dumps(keyboard_second, ensure_ascii=False).encode('utf-8')
keyboard_second = str(keyboard_second.decode('utf-8'))


keyboard_third = {
    "one_time": False,
    "buttons": [
        [get_button(label="Xiaomi", color="positive"), get_button(label="Thomas", color="positive")],
        [get_button(label="Karcher", color="positive"), get_button(label="Philips", color="positive")]
    ]
}

keyboard_third = json.dumps(keyboard_third, ensure_ascii=False).encode('utf-8')
keyboard_third = str(keyboard_third.decode('utf-8'))

keyboard_fourth = {
    "one_time": False,
    "buttons": [
        [get_button(label="Skype", color="positive"), get_button(label="Discord", color="positive")],
        [get_button(label="TeamSpeak3", color="positive"), get_button(label="ICQ", color="positive")]
    ]
}

keyboard_fourth = json.dumps(keyboard_fourth, ensure_ascii=False).encode('utf-8')
keyboard_fourth = str(keyboard_fourth.decode('utf-8'))

keyboard_withdraw = {
    "one_time": False,
    "buttons": [
        [get_button(label="Получить средства", color="positive")]
    ]
}

keyboard_withdraw = json.dumps(keyboard_withdraw, ensure_ascii=False).encode('utf-8')
keyboard_withdraw = str(keyboard_withdraw.decode('utf-8'))

keyboard_verif = {
    "one_time": False,
    "buttons": [
        [get_button(label="Подтвердить личность", color="positive")]
    ]
}

keyboard_verif = json.dumps(keyboard_verif, ensure_ascii=False).encode('utf-8')
keyboard_verif = str(keyboard_verif.decode('utf-8'))

keyboard_check = {
    "one_time": False,
    "buttons": [
        [get_button(label="Проверить оплату♻", color="positive")]
    ]
}

keyboard_check = json.dumps(keyboard_check, ensure_ascii=False).encode('utf-8')
keyboard_check = str(keyboard_check.decode('utf-8'))

