from enum import Enum

class Tag(Enum):
    site = 'http://automationpractice.com/index.php'
    campo_pesquisa = '//*[@id="search_query_top"]'
    campo_pesquisa_texto_Blouse = "Blouse"
    campo_lupa = '//*[@id="searchbox"]/button'
    campo_pesquisa_texto_ProdutoNaoExistente = "ProdutoNãoExistente"
    campo_women = '//*[@id="block_top_menu"]/ul/li[1]/a'
    campo_summer = '//*[@id="block_top_menu"]/ul/li[1]/ul/li[2]/ul/li[3]/a'

