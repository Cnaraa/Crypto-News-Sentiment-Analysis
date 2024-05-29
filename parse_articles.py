import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import json

url = 'https://www.cryptocompare.com/news/list/latest/?feeds=coindesk&categories=BTC' #ссылка на страницу с новостями

def get_source_html(url):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path="chromedriver.exe", options=chrome_options
    )
    
    driver.maximize_window()
    
    try:
        driver.get(url=url)
        time.sleep(3)
        html = driver.find_element(By.TAG_NAME, 'html')
        cnt_articles = 0
        n = 0
        while True:
            html.send_keys(Keys.END)
            time.sleep(3)
            find_date = driver.find_elements(By.XPATH, "//div[@class='col-body']/div[@class='news-data']/div[@class='news-date ng-binding']")
            if cnt_articles == len(find_date):
                if n == 10:    
                    with open("page_source_coindesk", "w", encoding='utf-8') as file:
                        file.write(driver.page_source)
                        break
                else:
                    n += 1
            else:
                cnt_articles = len(find_date)
                n = 0
            print(f'Текущая дата - {find_date[-1].text}. Статей обработано {cnt_articles}')
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_source_html(url=url)

if __name__ == '__main__':
    main()