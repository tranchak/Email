# import pyshorteners as pyshorteners
#
# link = input('Введите ссылку которую желаете сократить: ')
# s = pyshorteners.Shortener()
# print(s.tinyurl.short(link))

# https://tinyurl.com/yybc7w7x
# z = z = input().split()

# link = ['Ipona', 'Master Sword']
# alin = link
# link[0] = 'Zelda'
# print(link)
# > ['Zelda', 'Master Sword']
#
# print(alin)
# > ['Zelda', 'Master Sword']

# a = ['a', 'b', 'c']
# b = a
# a[0] = 0
# b[-1] = 11
# print(a)
# print(b)





def stas(z):
    for i in z.split(' '):
        yield i

s = stas('Итератор это объект у которого есть метод next()')
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))