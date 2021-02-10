dovid = {
    'Cakes' : {
        'name' : ['Cakes'],
        'adress' : ['Lviv'],
        "rating" : [1],
        "special" : ['cakes']
    },
    'Muff' : {
        'name' : ['Muff'],
        'adress' : ['Uzh'],
        "rating" : [2],
        "special" : ['muffin']
    },
    'Sweet' : {
        'name' : ['Sweet'],
        'adress' : ['Kyiv'],
        "rating" : [3],
        "special" : ['sweets']
    }
}
mode = input('read / add: ')
if mode == 'read':
    factory = input('Enter factory: ')
    request = input('Enter request: ')
    if factory.lower() == 'cakes':
        print(dovid[factory][request])
    elif factory.lower() == 'muff':
        print(dovid[factory][request])
    elif factory.lower() == 'sweet':
        print(dovid[factory][request])
elif mode == 'add':
    print(dovid)
    factory = input('Enter factory: ')
    request = input('Enter request: ')
    request_to_add = input('Request to add: ')
    if factory.lower() == 'cakes':
        if request == 'rating':
            dovid[factory][request].append(int(request_to_add))
        else:
            dovid[factory][request].append(request_to_add)
    elif factory.lower() == 'muff':
        if request == 'rating':
            dovid[factory][request].append(int(request_to_add))
        else:
            dovid[factory][request].append(request_to_add)
    elif factory.lower() == 'sweet':
        if request == 'rating':
            dovid[factory][request].append(int(request_to_add))
        else:
            dovid[factory][request].append(request_to_add)