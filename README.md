# Redis-Chat

1. Запустить контейнер с Redis <br>
  <b>docker run -d --name <cont_redis_name> -p 8080:6379 redis</b> <br><br>
2. Либо <b>python chat.py</b><br>
  (предварительно <b>pip install redis</b>)<br><br>
3. Либо создаём образ в папке проекта <br>
  <b>docker build --no-cache -t <image_name></b><br>
  Далее запускаем сколько-нибудь контейнеров с этим образом <br>
  <b>docker run -ti --name <cont_name> --link <cont_redis_name>:redis_link <image_name></b>
