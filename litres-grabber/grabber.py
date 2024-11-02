# Получение изображений страниц
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from config import URL_BOOKS, URL_LOGIN
from pynput.keyboard import Key, Controller
import time

book_id = input("ID КНИГИ: ")
error_place = int(input("Номер страницы ошибки? (Если ошибок не было напишите 0): "))
pages = int(input("Скольно страниц в книге: "))
width = input("Какая ширина в w (если не стандарт): ")
if width == "":
    width = "1900"
kb = Controller()


def check_close(driver):
    """
    wait until user closed browser window
    :param driver:
    :return:
    """
    closed = False
    s = driver.title
    while not closed:
        try:
            s = driver.title
            time.sleep(1)
        except:
            closed = True


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    # chrome_service = Service("c:/temp/chromedriver.exe")
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver


def load_bl_this(path):
    if os.uname().sysname == "Darwin":
        kb.press(Key.cmd_l);
        kb.press("s")
        kb.release(Key.cmd_l);
        kb.release("s")
    else:
        kb.press(Key.ctrl_l);
        kb.press("s")
        kb.release(Key.ctrl_l);
        kb.release("s")
    time.sleep(0.35)
    kb.type(path)
    time.sleep(0.67)
    kb.press(Key.enter)


def login_litres(driver):
    driver.get(URL_LOGIN)
    time.sleep(18)


def scroll_down(driver):
    count = 0
    while True:
        page = driver.find_element(by=By.TAG_NAME, value="html")

        page.send_keys(Keys.END)
        driver.implicitly_wait(1)
        page.send_keys(Keys.END)
        driver.implicitly_wait(1)
        page.send_keys(Keys.END)
        count += 1
        print(f'scroll down {count}')
        driver.implicitly_wait(1)
        footer = driver.find_element(by=By.CLASS_NAME, value='footer-wrap')
        if footer and footer.is_displayed():
            loader_button = driver.find_element(by=By.ID, value='arts_loader_button')
            if loader_button and not loader_button.is_displayed():
                break

    print(f'scroll down exit after {count} scrolls')


def load_books(driver):
    path = "0"
    print("Обработка страницы №0")
    driver.get(URL_BOOKS.format(0, "gif", book_id, width))
    try:
        err = driver.find_element(By.CLASS_NAME, "error_block__caption")
    except NoSuchElementException:
        time.sleep(10)
        load_bl_this(path)
    else:
        driver.get(URL_BOOKS.format(0, "jpg", book_id, width))
        time.sleep(10)
        load_bl_this(path)
    for i in range(int(pages) - (error_place + 1)):
        i += (error_place + 1)
        paath = f"{i}"
        print(f"Обработка страницы № {i}")
        driver.get(URL_BOOKS.format(i, "gif", book_id, width))
        try:
            err = driver.find_element(By.CLASS_NAME, "error_block__caption")
        except NoSuchElementException:
            load_bl_this(paath)
        else:
            driver.get(URL_BOOKS.format(i, "jpg", book_id, width))
            load_bl_this(paath)


def litres_loads():
    driver = create_driver()
    driver.maximize_window()
    login_litres(driver)
    load_books(driver)
    time.sleep(1)

    check_close(driver)
    print('FINISH!')


def main():
    litres_loads()


if __name__ == '__main__':
    main()
