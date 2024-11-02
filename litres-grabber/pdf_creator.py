import os
import img2pdf

# Создает сам пдф файл
def create_pdf(image_files, file_path):
    pdf_data = img2pdf.convert(image_files)
    # Создает пустой файл, чтобы потом туда записать
    open((file_path + ".pdf"), 'a').close()
    with open((file_path + ".pdf"), "wb") as f:
        f.write(pdf_data)

# Ищет все файлы в директории, которые являются снимками страницы
def get_image_list(dir_path):
    image_files = [i for i in os.listdir(dir_path) if (i.endswith(".jpeg") or i.endswith(".gif") or i.endswith(".jpg"))]
    image_files = sorted(image_files, key=lambda x: int(x.split(".")[0]))
    for i in range(len(image_files)):
        image_files[i] = os.path.join(dir_path, image_files[i])

    return image_files
