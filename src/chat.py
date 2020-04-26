import redis
from threading import Thread
from interact.events import conn, chat, pub, unsub, join, close, rooms, msgs, close_chat

host, port = conn()
client = redis.Redis(host=host, port=port)
sys = redis.Redis(host=host, port=port)
channel = client.pubsub()
chats = 'ch'


def listener(channel, client, chat_name):
    channel.subscribe(chat_name)
    sys.hincrby(chats, chat_name, 1)
    for msg in channel.listen():
        if msg['type'] in pub:
            msgs(msg['data'])
        elif msg['type'] in unsub:
            break
        else:
            client.publish(chat_name, join(login))


def publisher(channel, client, chat_name):
    while True:
        message = input()
        if message in unsub:
            close(login)
            channel.unsubscribe(chat_name)
            sys.hincrby(chats, chat_name, -1)
            if sys.hget(chats, chat_name) == b'0':
                sys.hdel(chats, chat_name)
            break
        else:
            client.publish(chat_name, login + ': ' + message)


while True:

    rooms(sys.hkeys(chats))

    login, chat_name = chat()

    listen = Thread(target=listener, args=(channel, client, chat_name), daemon=True)
    publish = Thread(target=publisher, args=(channel, client, chat_name))

    listen.start()
    publish.start()
    listen.join()

    if close_chat():
        break

channel.close()
