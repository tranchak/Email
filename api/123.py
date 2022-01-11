import pyshorteners as pyshorteners

link = input('Введите ссылку которую желаете сократить: ')
s = pyshorteners.Shortener()
print(s.tinyurl.short(link))

# https://tinyurl.com/yybc7w7x