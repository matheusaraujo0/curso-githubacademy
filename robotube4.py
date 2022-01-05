from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class RoboYoutube():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        self.webdriver = webdriver.Chrome('C:/Users/All Users/Anaconda3/chromedriver', options=options)

    def busca(self, busca, paginas):
        videos=[]
        pagina = 1

        url = "https://www.youtube.com/results?search_query=%s" %busca
        self.webdriver.get(url)

        while pagina <= paginas:

            titulos = self.webdriver.find_elements_by_xpath("//*[@id='video-title']")
            for titulo in titulos:
                print("Video encontrado: %s" %titulo.text)
            self.proxima_pagina(pagina)
            pagina +=1

    def proxima_pagina(self, pagina):
        print("*" * 30)
        print('Mudando para a página %s' %(pagina + 1))
        print("*" * 30)
        bottom = pagina * 10000
        self.webdriver.execute_script("window.scrollTo(0, %s);" %bottom)
        time.sleep(5)




bot = RoboYoutube()
bot.busca("python", 5)

#Ola
