import pandas as pd
import re
import requests
import time
import os
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def get_asset_url(url):
    url = re.sub('www.', 'assets.', url)
    url = re.sub('.html$', '.pdf', url)
    url = re.sub('-(?=nypd-cases-)', '/', url)
    return url

def download_pdf(url, id_):
    path = os.path.join('pdf', '{}.pdf'.format(id_))
    response = requests.get(asset_url)
    response.raise_for_status()
    with open(path, 'wb') as f:
        f.write(response.content)

def download_text(browser, url, id_):
    path = os.path.join('txt', '{}.txt'.format(id_))
    browser.get(url)
    tab = browser.find_element_by_xpath(r'//*[@id="viewer"]/div/div[1]/div[1]/div[2]/div[1]/div[4]/span')
    tab.click()
    text = browser.find_element_by_class_name('DV-textContents').text
    with open(path, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    driver_path = os.path.join(os.getcwd(), 'geckodriver')
    options = Options()
    options.add_argument('-headless')
    browser = webdriver.Firefox(firefox_options=options, executable_path=driver_path)
    os.makedirs('pdf', exist_ok=True)
    os.makedirs('txt', exist_ok=True)

    df = pd.read_csv('nypd-discipline.csv')
    urls = df['URL'].unique()

    print('Downloading text and PDF data from Buzzfeed...')
    for url in urls:
        asset_url = get_asset_url(url)
        id_ = int(os.path.basename(urlparse(asset_url).path).lstrip('nypd-cases-').rstrip('.pdf'))
        download_pdf(asset_url, id_)
        download_text(browser, url, id_)
        time.sleep(1)
    browser.close()
