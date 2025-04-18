"""
Этот модуль отвечает за объединение скачанных в одну директорию изображений в единый файл pdf
"""
import os
import img2pdf

def create_pdf(image_files, file_path):
    """
    Передает полученный список файлов в функцию объединения и полученный бинарный результат записывает в новый файл
    """
    pdf_data = img2pdf.convert(image_files)
    # Создает пустой файл, чтобы потом туда записать
    open((file_path + ".pdf"), 'a').close()
    with open((file_path + ".pdf"), "wb") as f:
        f.write(pdf_data)

def get_image_list(dir_path):
    """
    Поиск в заданной директории всех скачанных файлов
    """
    image_files = [i for i in os.listdir(dir_path) if (i.endswith(".jpeg") or i.endswith(".gif") or i.endswith(".jpg"))]
    image_files = sorted(image_files, key=lambda x: int(x.split(".")[0]))
    for i in range(len(image_files)):
        image_files[i] = os.path.join(dir_path, image_files[i])

    return image_files
