## litres-grabber

## Работу сделал
### Шигалугов Мурат Бесланович 468089 U3110

# Установка софта
```
git clone https://github.com/napolegend/litres-grabber; cd litres-grabber; python3 -m pip install -r requirements.txt
```

# Как скачивать книги?
Заходим в Литрес (нужен аккаунт, где есть книга по подписке), нажимаем читать и извлекаем id из адреса.
```
cd litres-grabber; python3 main.py
```
Вводим id, страницу где загрузка оборвалась(если произошла ошибка, если нет, то впишите 0), кол-во страниц книги,ширину страницы(в стандарте 1900, можно увидеть в поле w1900/w1200 в адресе отдельной страницы), если компьютер лагает, то меняем тайминги в time.sleep()

У вас есть 18 секунд, чтобы быстро залогиниться в аккаунт Литреса, где доступна нужная книга, потом нажимаем ctrl + s, чтобы задать директорию сохранения файла (Иначе все фото улетят в папку загрузок)

Наблюдаем за магией

# Как преобразовать кучу фотографий в pdf?
После скачивания будет доступна опция выбора папки, где сохранились фотографии, введите путь к этой папке.
Перед этим необходимо удалить все файлы, которые не подходят под описание "число.gif или число.jpg/jpeg", из нужной директории

## Примечание
Автор не несет ответственности за ущерб причиненный программой. Подобный софт нарушает политику использования сервиса Литрес, действуйте на свой страх и риск!!!

Если с синхроном клавиатуры начинается какая-то ахинея, то стоит подправить коэффициенты пауз между вводами эмулятивной клавиатуры, а также проверьте, что у вас включена английская раскладка (при включенной русской раскладке ничего работать не будет)
