from urllib import request, parse
import random
import json

with open('words.json') as f:
    data = json.load(f)

def get_key(val): 
    for key, value in data.items(): 
        if val == value: 
            return key

def random_word():
    return random.choice(list(data.keys()))

while True:
    i = 0 

    digit = []
    for _ in range (0,9):
        num = random.randint(0,9)
        digit.append(str(num))    
    digi =  str("".join(digit))

    street_ran = random.randint(0,300)
    email = digi + "@me.com"
    phone = digi
    location = str(random.randint(1000,4000)) + " " + random_word()
    organization = random_word()

    url="https://docs.google.com/forms/u/0/d/e/1FAIpQLSdR8CPrywE-DP-mFqWVI37Mkz9Zhq6p4CV4xaPlZniBpfrZ1g/formResponse" 

    text_entry_field={'emailAddress':email, 'entry.1694974203':phone, 'entry.1701240965':f'{random.randint(1000,4000)} {random_word()}', 'entry.470917288':organization, } 

    try:
        dataenc = parse.urlencode(text_entry_field)
        data_bytes = bytes(dataenc, 'utf8')
        req = request.Request(url, data=data_bytes)
        response = request.urlopen(req)
    except Exception as e:
        print(e)