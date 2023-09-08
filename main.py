import qrcode
# пример данных
data = "https://index.tatarstan.ru/atp/welcome/"
# имя конечного файла
filename = "site.png"
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)

