# -*- coding: utf8 -*-

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from random import*

vk = vk_api.VkApi(token="cb9a56e7b3efc823259c7834218c9e2e64fe1bef4daa8b938cb35329fa42cee2d8565b29f391a0e1f0767")

vk._auth_token()

vk.get_api()

longpoll = VkBotLongPoll(vk, 198913394)

def write_msg(message):
    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": message, "random_id": 0})
#отправить стикер. Айди стикера.
def st(idst):
    vk.method("messages.send", {"peer_id": event.object.peer_id, "sticker_id": idst, "random_id": 0})
#gui - get user id. незнаю чо это, наверно по айди дает информацию.
def gui(user_id):
    return vk.method('users.get', {'user_ids': user_id})
def beceda(peer_id):
    a = vk.method('messages.getConversationMembers', {'peer_id': peer_id, 'fields': id})
    return choice([item['member_id'] for item in a['items']])
steam_key = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "X", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
kogda = ["Это случится сегодня.", "Это случится завтра.", "Это случится через час.", "Это случится через месяц.", "Это случится через год.", "Это случится послезавтра.", "Это случится когда борщ будет президентом.", "Это случится когда гамеле купит пиар.", "Это случится скоро.", "Это случится когда Иван доделает уроки.", "Этого никогда не случится.", """Это случится когда Миша перестанет писать "Лол"."""]
while 1==1:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.peer_id != event.object.from_id:
                    #Походу получает список информации о пользователе по айди.
                    guis = gui(event.object.from_id)

                    name = guis[-1]['first_name']+","
                    if "!ключ" in event.object.text.lower() or "!Ключ" in event.object.text.lower():
                        write_msg(choice(steam_key)+choice(steam_key)+choice(steam_key)+choice(steam_key)+choice(steam_key)+"-"+choice(steam_key)+choice(steam_key)+choice(steam_key)+choice(steam_key)+choice(steam_key)+"-"+choice(steam_key)+choice(steam_key)+choice(steam_key)+choice(steam_key)+choice(steam_key))
                    if "!помощь" in event.object.text.lower() or "!Помощь" in event.object.text.lower():
                        write_msg(
name+
"""
Мои команды:
!кто [текст] - выбирает рандомного человека из беседы
!когда [текст] - когда случится что-либо
!шанс [текст] - шанс чего-либо
!ключ - генератор ключей Steam
!помощь - команды
Чтобы выйти из команды напиши "помощь"
""")
                    if "секретная команда гамеле" in event.object.text.lower():
                        write_msg(
"""
w s
""")
                    elif "!шанс " in event.object.text.lower() or "!Шанс " in event.object.text.lower():
                        r = randint(1, 100)
                        sh = " "+str(r)+"%"
                        write_msg(
name+
"""
Шанс того, что это случится -"""+sh
)
                    elif "!когда " in event.object.text.lower() or "!Когда " in event.object.text.lower():
                        r = choice(kogda)
                        write_msg(
name+
"""
"""
+r
)
                    elif "!кто " in event.object.text.lower() or "!Кто " in event.object.text.lower():
                        bec = beceda(event.object.peer_id)
                        guis = gui(bec)
                        name_full = "["+"id"+str(bec)+"|"+str(guis[-1]['first_name'])+" "+str(guis[-1]['last_name'])+"]"
                        write_msg(
name+
"""
Я уверен что это -
"""
+name_full
)
                    elif "помощь" in event.object.text.lower() or "Помощь" in event.object.text.lower():
                        if event.object.from_id == 183870598 or event.object.from_id == 385217862:
                            write_msg(
"""
Бог в помощь!
""")
                    elif "лол" in event.object.text.lower() or "Лол" in event.object.text.lower():
                        if event.object.from_id == 465415473:
                            write_msg(
"""
У Миши в жопе кол!
""")
                    elif "справебыдл" in event.object.text.lower() or "Справебыдл" in event.object.text.lower():
                        if "справебыдлоъ" in event.object.text.lower() or "Справебыдлоъ" in event.object.text.lower():
                            st(131)
                        else:
                            st(163)
                    elif "Хех" in event.object.text.lower() or "хех" in event.object.text.lower() or "Хах" in event.object.text.lower() or "хах" in event.object.text.lower() or "Хых" in event.object.text.lower() or "хых" in event.object.text.lower():
                        if event.object.from_id == 559144282:
                            if "Хех" in event.object.text.lower() or "хех" in event.object.text.lower():
                                write_msg("""
Жопой об хехех.
""")
                            if "Хах" in event.object.text.lower() or "хах" in event.object.text.lower():
                                write_msg("""
Жопой об хахах.
""")
                            if "Хых" in event.object.text.lower() or "хых" in event.object.text.lower():
                                write_msg("""
Жопой об хыхых.
""")
    except:
        pass