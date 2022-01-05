from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:/Users/All Users/Anaconda3/chromedriver')
driver.get("https://registro.br/")

pesquisa = driver.find_element_by_id("is-avail-field")
pesquisa.clear()
pesquisa.send_keys("roboscompython.com.br")
pesquisa.send_keys(Keys.RETURN)

time.sleep(8)
driver.close()