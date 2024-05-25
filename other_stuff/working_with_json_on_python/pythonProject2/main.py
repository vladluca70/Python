import json

with open('example.json', 'r') as file:
    data=json.load(file)

print(data['company']['name'])
print(data['company']['location'])
print()

for department in data['company']['departments']:
    print(department['name'])
print()

for department in data['company']['departments']:
    for employee in department['employees']:
        print(employee['id'], employee['name'])
print("=====================")

for department in data['company']['departments']:
    for employee in department['employees']:
        print(employee['id'], employee['name'])
        if 'sales_performance' in employee:
            print(employee['sales_performance']['yearly_sales'])
            for month_sale in employee['sales_performance']['monthly_sales']:
                print(month_sale, end=', ')
            print(" ")
            print("============")
print("===================================")

for department in data['company']['departments']:
    if department['name']=='Marketing':
        for employee in department['employees']:
            print(employee['id'], employee['name'])
            print('---marketing----')
print()

for department in data['company']['departments']:
    if department['name']=='Marketing':
        for employee in department['employees']:
            for campain in employee['campaigns']:
                print(campain['id'], campain['name'])
print()

for department in data['company']['departments']:
    if department['name']=='Marketing':
        for employee in department['employees']:
            for campaign in employee['campaigns']:
                for channel in campaign['channels']:
                    print(channel, end=',')
                print()
print()

for product in data['company']['products']:
    print(product['id'], product['name'])
    for data in product['sales_history']:
        print(data)
    print("-**************-")
print()
