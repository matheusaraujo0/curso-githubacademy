from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando nosso robô...")

workbook = xlrd.open_workbook(r'C:\Users\Lenovo\Documents\CURSO PYTHON BOT\Projeto 1\excel.xls')
sheet = workbook.sheet_by_name('Plan1')
rows = sheet.nrows
columns = sheet.ncols

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

driver = webdriver.Chrome('C:/Users/All Users/Anaconda3/chromedriver', options=options)
driver.get("https://registro.br/")


for curr_row in range(0, rows):
    x = sheet.cell_value(curr_row, 0)
    pesquisa = driver.find_element_by_id("is-avail-field")
    time.sleep(3)
    pesquisa.clear()
    time.sleep(1)
    pesquisa.send_keys(x)
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(5)

    #driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong')


    print("Domínio: %s - %s" %(x, driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))
    time.sleep(1)


driver.close()