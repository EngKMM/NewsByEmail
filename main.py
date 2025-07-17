from dotenv import load_dotenv
import os
import requests, smtplib, ssl

load_dotenv()
api_key = os.getenv("API_KEY")
app_password = os.getenv("app_password")
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-06-16&sortBy=publishedAt&apiKey=" + api_key

api_request = requests.get(url)
msg_content = ""

content = api_request.json()
for article in content["articles"]:
    msg_content += f"{article['title'] or ''}\n{article['description'] or ''}\n\n"


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

send_email(msg_content)
