import requests
from send_email import send_email

api_key = "4668a70e6c354de8a9e5c66c5edf6816"
url = "https://newsapi.org/v2/everything?q=tesla& \
       from=2023-08-25&sortBy=publishedAt&apiKey=" \
       "4668a70e6c354de8a9e5c66c5edf6816"
# make request
request = requests.get(url)

#get a dictionery with data
content=request.json()
print(content['articles'])

print(len(content["articles"]))

#access to article with title ans description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] +2*"\n"

body = body.encode("utf-8")
send_email(message=body)



