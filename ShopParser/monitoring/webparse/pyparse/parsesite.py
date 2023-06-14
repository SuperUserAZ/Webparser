from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import date
from .models import MobilePhone
import re
from decimal import Decimal

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_driver_path = r"C:\Users\Shadow\Desktop\test\chromeDriver\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def close_driver(driver):
    driver.quit()

def parse_trendyol():
    driver = init_driver()
    url = "https://www.trendyol.com/cep-telefonu-x-c103498"
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "html.parser")
    cards = soup.find_all("div", class_="p-card-chldrn-cntnr")
    for card in cards:
        title_element = card.find("span", class_="prdct-desc-cntnr-name")
        price_element = card.find("div", class_="prc-box-dscntd")
        link_element = card.find("a", href=True)
        title = title_element.text.strip() if title_element else ""
        raw_price = price_element.text.strip() if price_element else ""
        cleaned_price = re.sub(r'[^\d.,]+', '', raw_price)
        try:
            price = Decimal(cleaned_price.replace(',', '.'))
        except (ValueError, TypeError, Exception):
            price = None
        if title and price and link_element:
            link = "https://www.trendyol.com" + link_element['href']
            MobilePhone.objects.create(
                title=title,
                price=price,
                currency="TL",
                date=date.today(),
                url=link
            )
        print("Идет парсинг страниц... ")
        #print('====[{}]'.format(len(cards)))
    close_driver(driver)

def get_card_count():
    driver = init_driver()

    # Переход на целевую страницу
    url = "https://www.trendyol.com/cep-telefonu-x-c103498"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    cards = soup.find_all("div", class_="p-card-chldrn-cntnr")
    print(len(cards))
    close_driver(driver)
    
