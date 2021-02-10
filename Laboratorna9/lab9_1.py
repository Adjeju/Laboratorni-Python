dovid = {
    'uzh' : {
        'adress' : ['Uzh'],
        'num' : [12345],
        "level" : [1],
        "rating" : [1]
    },
    'lviv' : {
        'adress' : ['Lviv'],
        'num' : [1234567],
        "level" : [2],
        "rating" : [2]
    },
    'kyiv' : {
        'adress' : ['Kyiv'],
        'num' : [123456789],
        "level" : [3],
        "rating" : [3]
    }
}
mode = input('read / add: ')
if mode == 'read':
    city = input('Enter city: ')
    request = input('Enter request: ')
    if city.lower() == 'uzh':
        print(dovid[city][request])
    elif city.lower() == 'lviv':
        print(dovid[city][request])
    elif city.lower() == 'kyiv':
        print(dovid[city][request])
elif mode == 'add':
    print(dovid)
    city = input('Enter city: ')
    request = input('Enter request: ')
    request_to_add = input('Request to add: ')
    if city.lower() == 'uzh':
        if request == 'num' or request == 'level' or request == 'rating':
            dovid[city][request].append(int(request_to_add))
        else:
            dovid[city][request].append(request_to_add)
    elif city.lower() == 'lviv':
        if request == 'num' or request == 'level' or request == 'rating':
            dovid[city][request].append(int(request_to_add))
        else:
            dovid[city][request].append(request_to_add)
    elif city.lower() == 'kyiv':
        if request == 'num' or request == 'level' or request == 'rating':
            dovid[city][request].append(int(request_to_add))
        else:
            dovid[city][request].append(request_to_add)
    print(dovid[city][request])