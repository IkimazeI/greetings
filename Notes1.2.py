'''
чтобы не было скучно, использовал встроенный модуль, позволяющий работать с
датой и временем в программе. Дата создания заметки не должно указываться вручную и
уж тем более не с помощью обновления кода каждый день
(я уже учился на программиста C#, поэтому некоторые знания имею)
'''
from datetime import datetime

created_date = datetime.now() # указывается текушая дата включая в себя от года до милисекунд
issue_date = input('\nВведите дату окончания заметки в формате 31-12-2025: ')

# Выводим результат без года, используя индексы
print('Дата создания заметки:', created_date.strftime("%d-%m"))
print('Дата окончания срока заметки:', issue_date[0:5])