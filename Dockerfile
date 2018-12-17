FROM python:2.7-alpine3.7
RUN pip install Flask && pip install SkPy && pip install requests && pip install pyTelegramBotAPI
COPY ./server_web /server_web
