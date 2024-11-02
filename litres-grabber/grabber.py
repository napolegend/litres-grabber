# Получение изображений страниц
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from config import URL_BOOKS, URL_LOGIN
from pynput.keyboard import Key, Controller
import time

# Запускаем эмулятор клавиатуры
kb = Controller()


# Ждем, пока пользователь закроет окно браузера
def check_close(driver):
    closed = False
    s = driver.title
    while not closed:
        try:
            s = driver.title
            time.sleep(1)
        except:
            closed = True


# Создаем клиент браузера
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver


# Эмулируем нажатие ctrl(cmd) + s на странице с одной картинкой
def load_bl_this(path):
    # Для MacOS
    if os.uname().sysname == "Darwin":
        kb.press(Key.cmd_l)
        kb.press("s")
        kb.release(Key.cmd_l)
        kb.release("s")
    # Для Linux и Windows
    else:
        kb.press(Key.ctrl_l)
        kb.press("s")
        kb.release(Key.ctrl_l)
        kb.release("s")
    time.sleep(0.35)
    # Вписываем номер страницы
    kb.type(path)
    time.sleep(0.67)
    kb.press(Key.enter)


# Запускает страницу входа в аккаунт Литрес
def login_litres(driver):
    driver.get(URL_LOGIN)
    time.sleep(18)


# Переключает страницы и заходит конкретно в изображение
def load_books(driver, book_id, width, pages):
    path = "0"
    print("Обработка страницы №0")
    """
    Картинки хранятся и в GIF и в JPG
    Первые для текста и малокрасочных страниц, а вторыми в основном оформлены Схемы и обложка
    Так как гифок больше имеет смысл сначала пробовать зайти на гиф страницу
    """
    driver.get(URL_BOOKS.format(0, "gif", book_id, width))
    """
    Так как самая первая страница требует больше времени на загрузку, 
    выносим загрузку первой страницы в отдельный элемент и ставим везде задержку в 18 секунд,
    а также даем время пользователю нажать CTRL(CMD) + S и сохранить первую страницу в определенную 
    директорию вручную, чтобы потом при нажатии эмулятором этих кнопок директория сохранения оставалась
    той же (чтобы не сохранять все в папку Загрузки)
    """
    try:
        # Смотрим есть ли на странице сообщение об отсутствии такой страницы
        err = driver.find_element(By.CLASS_NAME, "error_block__caption")
    except NoSuchElementException:
        # Если нет такой ошибки, то скачиваем изображение
        time.sleep(18)
        load_bl_this(path)
    else:
        # Если есть, то переходим на JPG и скачиваем изображение
        driver.get(URL_BOOKS.format(0, "jpg", book_id, width))
        time.sleep(18)
        load_bl_this(path)
    for i in range(int(pages) - 1):
        i += 1
        paath = f"{i}"
        print(f"Обработка страницы № {i}")
        driver.get(URL_BOOKS.format(i, "gif", book_id, width))
        try:
            # Смотрим есть ли на странице сообщение об отсутствии такой страницы
            err = driver.find_element(By.CLASS_NAME, "error_block__caption")
        except NoSuchElementException:
            # Если нет такой ошибки, то скачиваем изображение
            load_bl_this(paath)
        else:
            # Если есть, то переходим на JPG и скачиваем изображение
            driver.get(URL_BOOKS.format(i, "jpg", book_id, width))
            load_bl_this(paath)


def litres_loads(book_id, width, pages):
    driver = create_driver()
    driver.maximize_window()
    login_litres(driver)
    load_books(driver, book_id, width, pages)
    time.sleep(1)
    print("Закройте окно браузера")
    check_close(driver)
    print('FINISH! Загрузка изображений завершена')
