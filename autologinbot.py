from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def startBot(username, password, url):
    path = r"C:\Users\hp\Downloads\chromedriver.exe"
    service = Service(path)
    
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.find_element(By.NAME, "username_field_name").send_keys(username)
    driver.find_element(By.NAME, "password_field_name").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()

username = "Enter your username"
password = "Enter your password"
url = "https://example.com/login"

startBot(username, password, url)