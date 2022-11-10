import requests
ph = input('введите номер телефона:  ')


    spam = True
    while spam:
        r = requests.post("https://api.fix-price.com/buyer/v2/registration/phone/request", data = {"phone": ph})
        if r.status_code == 400:
            print('ошибка')
            print(r)
        elif r.status_code == 200:
            print("смс отправлено")
        else:
            print('чё?')
            print(r)