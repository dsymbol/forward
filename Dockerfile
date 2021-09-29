FROM python:alpine3.14	

RUN apk add --no-cache git build-base && \
    git clone https://github.com/dsymbol/discord-telegram-bot /app
	
WORKDIR app	

RUN pip3 install --no-cache-dir -r requirements.txt
	
CMD ["python3", "main.py"]