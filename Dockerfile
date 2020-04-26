FROM python:3 

WORKDIR ./scr/

RUN pip install --no-cache-dir redis

COPY . .

CMD ["python", "./src/chat.py"]
