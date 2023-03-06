import random
import time

chars = '@#$%&*()/\|!?`-_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

print('Вас приветствует генератор паролей PyGen!')
number = input('Пожалуйста, укажите количество паролей: '+ "\n")
length = input('Укажите длину пароля: '+ "\n")
number = int(number)
length = int(length)

for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
    
time.sleep(30)
print('истекло время ожидания')
time.sleep(3)
