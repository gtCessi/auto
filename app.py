from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'  # caminho do driver
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_signin(self):
        try:
            btn_signin = self.chrome.find_element_by_link_text('Sign in')
            btn_signin.click()
        except Exception as e:
            print('Erro Sign in:', e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_senha = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('email')
            input_senha.send_keys('senha')
            sleep(5)
            btn_login.click()

        except Exception as e:
            print('Erro no Login:', e)

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
            perfil.click()

        except Exception as e:
            print('Erro:', e)

    def faz_logout(self):
        try:
            perfil2 = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form')
            perfil2.click()

        except Exception as e:
            print('Erro Log out:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    sleep(3)

    chrome.clica_signin()
    chrome.faz_login()

    chrome.clica_perfil()
    sleep(3)
    chrome.faz_logout()

    sleep(10)
    chrome.sair()
