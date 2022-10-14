import requests

url = 'https://api.divar.ir/v8/web-search/1/apartment-sell'
last_post_date = 1650392836073764
json = {"json_schema": {"category": {"value": "apartment-sell"}},
        "last-post-date": last_post_date}
headers = {
    "Content-Type": "application/json"
}

list_of_tokens = []

for i in range(4):
    res = requests.post(url, json=json, headers=headers)
    data = res.json()
    last_post_date = data['last_post_date']

    for widget in data['web_widgets']['post_list']:
        print(widget)
        token = widget['data']['token']
        list_of_tokens.append(token)

    json = {"json_schema": {"category": {"value": "apartment-sell"}},
            "last-post-date": last_post_date}

print(list_of_tokens)
print(len(list_of_tokens))
