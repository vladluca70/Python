import json

with open('example.json', 'r') as file:
    data = json.load(file)

print(data['store']['name'])

for user in data['store']['users']:
    for x in user['addresses']:
        print(x['address'])
print("===========================")

for product in data['store']['products']:
    print(product['name'])
print("===========================")

for user in data['store']['users']:
    for address in user['addresses']:
        print(address['type'], ",",  address['address'])
print("===========================")

for user in data['store']['users']:
    for order in user['orders']:
        for x in order['items']:
            print(x['price'])
print("===========================")
