lst = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
dct = {}

for item in lst:
    key = item['item']
    amount = item['amount']
    if key in dct:
        dct[key] += amount
    else:
        dct[key] = amount

print(dct)
