import time
from selenium.webdriver.common.action_chains import ActionChains
import PySimpleGUI as sg
from tags.tag import Tag
from classe_driver.classe_drivers import Argumentos_driver
from selenium.common.exceptions import NoSuchElementException
from logs.whats_log import funcao_debug, funcao_error, funcao_info


class wppbot:

    def iniciar(self):
        funcao_debug("DEBUG")

        bot = Argumentos_driver()

        #### Testes WEB ####
        ## PESQUISAR PRODUTOS EXISTENTES ##
        #### Acessar página home do site. ####
        #### Digitar o nome do produto "Blouse" no campo de pesquisa.####
        #### Clicar no botão de pesquisa ####


        sg.Popup(" 1 - Acessar página home do site. "
                 "\n 2 - Digitar o nome do produto 'Blouse' no campo de pesquisa.\n"
                 " 3 - Clicar no botão de pesquisa.", custom_text="Prosseguir")
        try:
            bot.driver.get(Tag.site.value)
            campo_pesquisa = bot.driver.find_element_by_xpath(Tag.campo_pesquisa.value)
            campo_pesquisa.send_keys(Tag.campo_pesquisa_texto_Blouse.value)
            campo_lupa = bot.driver.find_element_by_xpath(Tag.campo_lupa.value)
            campo_lupa.click()
            sg.Popup(" TEST PASS", custom_text="Prosseguir")
            time.sleep(2)
            funcao_info(" TEST PASS PESQUISAR PRODUTOS EXISTENTES")

        except NoSuchElementException:
            sg.Popup(" TEST PESQUISAR PRODUTOS EXISTENES FAILED, Não encontrou o elemento", custom_text="Ok")
            funcao_error("TEST PESQUISAR PRODUTOS EXISTENES FAILED, Não encontrou o elemento - Linha 35")







        ## PESQUISAR PRODUTOS NÃO EXISTENTES ##
        #### Acessar página home do site. ####
        #### Digitar o nome do produto "ProdutoNãoExistente" no campo de pesquisa.####
        #### Clicar no botão de pesquisa. ####

        try:
            bot.driver.get(Tag.site.value)
            sg.Popup(" 1 - Acessar página home do site. "
                     "\n 2 - Digitar o nome do produto 'ProdutoNãoExistente' no campo de pesquisa.\n"
                     " 3 - Clicar no botão de pesquisa.", custom_text="Prosseguir")
            campo_pesquisa = bot.driver.find_element_by_xpath(Tag.campo_pesquisa.value)
            campo_pesquisa.send_keys(Tag.campo_pesquisa_texto_ProdutoNaoExistente.value)
            campo_lupa = bot.driver.find_element_by_xpath(Tag.campo_lupa.value)
            campo_lupa.click()
            sg.Popup(" TEST PASS", custom_text="Prosseguir")
            funcao_info(" TEST PASS PESQUISAR PRODUTOS NÃO EXISTENTES")
        except NoSuchElementException:
            sg.Popup(" TEST PESQUISAR PRODUTOS NÃO EXISTENTES FAILED, Não encontrou o elemento", custom_text="Ok")
            funcao_error("TEST PESQUISAR PRODUTOS NÃO EXISTENTES FAILED, Não encontrou o elemento - Linha 60")


        ## LISTAR PRODUTOS ##
        #### Acessar página home do site. ####
        #### Passar o mouse por cima da categoria "Women", no menu principal superior de categorias. ####
        #### Clicar na sub-categoria "Summer Dresses".  ####

        try:
            bot.driver.get(Tag.site.value)
            sg.Popup(" 1 - Acessar página home do site. "
                     "\n 2 - Passar o mouse por cima da categoria 'Women', no menu principal superior de categorias..\n"
                     " 3 - Clicar na sub-categoria 'Summer Dresses'", custom_text="Prosseguir")
            campo = bot.driver.find_element_by_xpath(Tag.campo_women.value)
            hover = ActionChains(bot.driver).move_to_element(campo)
            hover.perform()
            time.sleep(5)
            campo_summer = bot.driver.find_element_by_xpath(Tag.campo_summer.value)
            bot.driver.implicitly_wait(30)
            campo_summer.click()
            sg.Popup("TEST PASS\n Todos Testes WEB Realizado com sucesso", custom_text="Finalizar")
            funcao_info(" TEST PASS LISTAR PRODUTOS")
            bot.driver.close()

            print("Testes Finalizados")

        except NoSuchElementException:
            sg.Popup(" TEST LISTAR PRODUTO FAILED, Não encontrou o elemento", custom_text="Ok")
            funcao_error("TEST LISTAR PRODUTO FAILED, Não encontrou o elemento - Linha 84")





