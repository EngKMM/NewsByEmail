from dotenv import load_dotenv
from textblob import TextBlob
import os
import requests, smtplib, ssl

load_dotenv()
api_key = os.getenv("API_KEY")
app_password = os.getenv("app_password")
url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=" + api_key

api_request = requests.get(url)
msg_content = ""

content = api_request.json()
for article in content["articles"]:
    text = f"{article['title'] or ''}{article['description'] or ''}"
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment>0:
        msg_content += f"{article['title'] or ''}\n{article['description'] or ''}\n{article['url'] or ''}\n\n"


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "karimgohary.gohary@gmail.com"
    password = app_password

    receiver = "karimgohary.gohary@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode("utf-8"))

send_email(message="Subject: Today's dose of positive news :)"+'\n'+msg_content)
