
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL =  "https://pump.fun/profile/"
DEFAULT_TIMEOUT = 35



def setup_driver():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def getProfile(driver):
    try:
        url = URL + str(input)
        driver.get(url)
        time.sleep(3) # Wait for the page to load
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='radix-:r0:']/button"))
        ).click()
        time.sleep(2)

        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            ec.presence_of_element_located((By.XPATH, "//div[contains(text(),'coins created')]"))
        ).click()

        time.sleep(3)

        page_source = driver.page_source

        soup = BeautifulSoup(page_source, 'html.parser')
        profileName = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]")
        target_div = soup.find('div', {'class': 'max-w-[400px]'})
        hrefs = []
        if target_div:
            hrefs = [a['href'] for a in target_div.find_all('a', href=True)]

        print("given profile name : " ,str(profileName.text))

        if(len(hrefs) > 1):
            print("The given profile have more than one coin")
            print("In this profile there are : ",str(len(hrefs)) +" Coins")
            print("Extracted Coins..")
            print(hrefs)

        if(len(hrefs) == 1):
            print("The given profile have only one coin")


    except Exception as e:
        print(f"Error : {e}")



if __name__ == "__main__":
    input = "4JCxHffMAnaZnuk9mqJAAzwa6hEfPaC2XCTNnq8n5SQT"  ##wallet_address
    driver = setup_driver()
    getProfile(driver)
