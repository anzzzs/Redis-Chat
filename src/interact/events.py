redis_host = 'redis-link'
redis_port = '6379'

sys_port = '8080'

pub = ('message', 'pmessage')
unsub = ('unsubscribe', 'punsubscribe', 'EXIT')


def conn():
    host = (input('Enter ip of host with redis container (default redis-link):') or redis_host)
    return host, redis_port if host == redis_host else sys_port


def chat():
    return input('Enter your login: '), input('Welcome! Enter chat name: ')


def join(login):
    return f'{login} join!'


def rooms(rooms):
    print(f'There are active rooms: {[room.decode() for room in rooms]}')


def close(login):
    print(f'Goodbye, {login}!')


def msgs(msg):
    print(msg.decode('utf-8'))


def close_chat():
    return input('Enter EXIT to close chat ') in unsub
