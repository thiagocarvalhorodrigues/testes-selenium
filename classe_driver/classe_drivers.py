import os
from selenium import webdriver


class Argumentos_driver:

    def __init__(self):
        dir_path = os.getcwd()
        self.options = webdriver.ChromeOptions()
        self.arg = ["hide_console",]
        self.options.add_argument('--silent ')
        self.options.add_argument('--log-level=3')
        self.options.add_argument('--lang=pt-BR')
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--window-position=10,10")
        self.options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path= dir_path + r'/driver/chromedriver.exe', chrome_options=self.options, service_args=self.arg)



