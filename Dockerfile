FROM python:alpine3.14	
	
WORKDIR app

COPY . .

RUN apk add --no-cache build-base \
    && pip3 install --no-cache-dir -r requirements.txt
	
CMD ["python3", "main.py"]
