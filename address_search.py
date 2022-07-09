import requests

@app.route("/", methods=["POST"])


zipcode = "1620055"

response = requests.get(f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}')

address_info = response.json()['results'][0]

prefecture_name = address_info['address1']
city_name = address_info['address2']
town_name = address_info['address3']

address = f'{prefecture_name}{city_name}{town_name}'

print(address)