from datetime import datetime
from time import sleep
from os import system

# print(datetime.now())

# agora = datetime.now()
# year = agora.year 
# month = agora.month
# day = agora.day
# hours = agora.hour
# minutes = agora.minute
# seconds = agora.second

# print(f'{day}/{month}/{year} - {hours}:{minutes}:{seconds}')

while True:
    system('cls')
    agora = datetime.now()
    year = agora.year 
    month = agora.month
    day = agora.day
    hours = agora.hour
    minutes = agora.minute
    seconds = agora.second
    print(f'{day}/{month}/{year} \n{hours}:{minutes}:{seconds}')
    sleep(1)