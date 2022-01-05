from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")


# ENTRA NO SITE DA ACRONIS
driver = webdriver.Chrome('C:/Users/All Users/Anaconda3/chromedriver', options=options)
driver.get("https://br01-cloud.acronis.com/mc/app;group_id=2754c747-ba0c-41d5-ad4b-ee57eb184397/clients;application_id=6e6d758d-8e74-3ae3-ac84-50eb0dff12eb")
pyautogui.hotkey('win', 'up')

# COLOCA USUÁRIO E SENHA

driver.find_element_by_xpath('/html/body/div/section/section/main/div/div/div/div/div[6]/form/div[3]/div/div[1]/div/div/input').send_keys("matheus.gomes@inorpel.com.br")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/section/section/main/div/div/div/div/div[6]/form/div[4]/div/button/span/span').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/section/section/main/div/div/div/div/div[6]/form[1]/div[3]/div/div[1]/div/div[1]/div/div[1]/input').send_keys("Mg@2021!!!")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/section/section/main/div/div/div/div/div[6]/form[1]/div[4]/div[1]/button/span/span').click()
time.sleep(18)

# ENTRANDO NA ÁREA PRINCIPAL

pyautogui.click(x=398, y=764)
time.sleep(1)
driver.find_element_by_xpath('/html/body/alerts/div/div[2]/div/div/main/clients/div/p-table/div/div/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[1]/span/span[2]/tenant-link/a/span').click()
time.sleep(4)
pyautogui.click(x=394, y=610)
time.sleep(1)
driver.find_element_by_xpath('/html/body/alerts/div/div[2]/div/div/main/overview/div/div/div/div[2]/manage-button/guided-button/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/section/aside/div/div[3]/div[1]/div/div/ul/li[2]/div/span[2]').click()
time.sleep(3)

