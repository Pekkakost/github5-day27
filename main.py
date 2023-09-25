import requests
from send_email import send_email

topic = "tesla"

api_key = "4668a70e6c354de8a9e5c66c5edf6816"
url =   "https://newsapi.org/v2/everything?" \
        f"q={topic}&" \
        "sortBy=publishedAt&" \
        "apiKey=4668a70e6c354de8a9e5c66c5edf6816&" \
        "language=en"

# make request
request = requests.get(url)

#get a dictionery with data
content=request.json()
#access to article with title ans description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject:Today's news" \
            +"\n" + body + article["title"] + "\n"\
            + article["description"] + "\n" \
            + article["url"]+2*"\n"

body = body.encode("utf-8")
send_email(message=body)



