"""
Файл запуска программы
"""
import grabber
import pdf_creator


def image_load_starter():
    """
    Эта функция вызывает модуль скачивания книги постранично
    """
    # ID Книги в системе Литрес
    book_id = input("ID КНИГИ: ")
    pages = int(input("Скольно страниц в книге: "))
    # У книг в литрес разная ширина страницы, и ссылки соответственно, так что если она не стандарт, то нужно уточнить
    width = input("Какая ширина в w (если стандарт, то сразу нажмите ENTER): ")
    if width == "":
        width = "1900"
    grabber.litres_loads(book_id, width, pages)


def pdf_create_starter():
    """
    Эта функция вызывает модуль преобразования кучи изображений в единый pdf файл
    """
    dir_path = input("Введите путь к папке с изображениями: ")
    if dir_path[-1] == "/":
        dir_path = dir_path[:-1]
    file_name = input("Как назовете PDF файл: ").split()[0]
    file_path = dir_path + "/" + file_name
    image_files = pdf_creator.get_image_list(dir_path)
    pdf_creator.create_pdf(image_files, file_path)


def main():
    image_load_starter()
    pdf_create_starter()


if __name__ == "__main__":
    main()
