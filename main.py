import qrcode
# вписываем url
data = "https://index.tatarstan.ru/atp/welcome/"
# имя конечного файла
filename = "site.png"
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл в текущей директории
img.save(filename)
# указываем папку для сохранения
path = '/Users/esemenov/'
# сохраняем qr код в указанную папку
img.save(path+filename)

