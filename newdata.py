from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
no='9052030587'
password='haseena'
search='tshirts for women'

driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Desktop\phyton\chromedriver_win32\chromedriver.exe')

driver.get('https://www.flipkart.com/')
time.sleep(5)
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys(no)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys(password)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button').click() #loginbutton
time.sleep(5)
driver.find_element(By.CLASS_NAME,'_3704LK').click() #search button
driver.find_element(By.CLASS_NAME,'_3704LK').send_keys(search)
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
time.sleep(5)

