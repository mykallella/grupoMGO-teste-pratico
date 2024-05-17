from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)


class TestFormularioConviteFesta:

    driver.maximize_window()
    driver.get('https://tinyurl.com/desafioTesterSGE')

    def test_cenario_13_sem_informacao_alergia(self):

        # Locators
        botao_enviar = (By.XPATH, '//*[text()="Enviar"]')
        campo_alergia = (By.XPATH, '//*[text()="Você tem alguma alergia ou restrição alimentar?"]/parent::node()/parent::node()/parent::node()/parent::node()/div[2]/div/div/div/div/input')
        campo_email = (By.XPATH, '//*[text()="Qual é seu endereço de e-mail?"]/parent::node()/parent::node()/parent::node()/parent::node()/div[2]/div/div/div/div/input')
        campo_nome = (By.XPATH, '//*[text()="Seu nome"]/parent::node()/parent::node()/parent::node()/parent::node()/div[2]/div/div/div/div/input')
        campo_quantidade_pessoas_comparecerao = (By.XPATH, '//*[text()="Quantas pessoas comparecerão?"]/parent::node()/parent::node()/parent::node()/parent::node()/div[2]/div/div/div/div/input')
        checkbox_trazer_acompanhamentos = (By.XPATH, '//*[@aria-label="Acompanhamentos/aperitivos"]')
        checkbox_trazer_bebidas = (By.XPATH, '//*[@aria-label="Bebidas"]')
        checkbox_trazer_outro = (By.XPATH, '//*[@aria-label="Outro:"]')
        checkbox_trazer_prato_principal = (By.XPATH, '//*[@aria-label="Prato principal"]')
        checkbox_trazer_salada = (By.XPATH, '//*[@aria-label="Salada"]')
        checkbox_trazer_sobremesa = (By.XPATH, '//*[@aria-label="Sobremesa"]')
        radio_vai_participar = (By.XPATH, '//*[@data-value="Sim, participarei"]')
        select_sobremesa = (By.XPATH, '//*[text()="Escolha uma sobremesa"]/parent::node()/parent::node()/parent::node()/parent::node()/div[2]/div/div/div/div/span[text()="Escolher"]')
        select_sobremesa_pudim = (By.XPATH, '//*[text()="Escolha uma sobremesa"]/parent::node()/parent::node()/parent::node()/parent::node()/div[2]/div/div[2]/div[3]/span[text()="Pudim de leite"]')
        texto_formulario_enviado_sucesso = (By.XPATH, '//*[contains(text(), "Thanks for responding!")]')

        # Digita nome do usuário
        driver.find_element(*campo_nome).send_keys('Myrela Caroline de Barros Silva')

        # Escolhe sobremesa
        driver.find_element(*select_sobremesa).click()
        driver.find_element(*select_sobremesa_pudim).click()

        # Escolhe se pode participar
        driver.find_element(*radio_vai_participar).click()

        # Digita quantidade de pessoas que comparecerão
        driver.find_element(*campo_quantidade_pessoas_comparecerao).send_keys('4')

        # Escolhe o que vai trazer
        driver.find_element(*checkbox_trazer_prato_principal).click()
        driver.find_element(*checkbox_trazer_salada).click()
        driver.find_element(*checkbox_trazer_sobremesa).click()

        # Digita se tem alergia
        # driver.find_element(*campo_alergia).send_keys('alergia e restrição alimentar ')

        # Digita e-mail
        driver.find_element(*campo_email).send_keys('mykallella@gmail.com')

        # Envia o formulário
        driver.find_element(*botao_enviar).click()

        # Verifica se o formulário foi enviado
        texto_formulario_enviado_sucesso_encontrado = driver.find_element(*texto_formulario_enviado_sucesso)
        assert not texto_formulario_enviado_sucesso_encontrado.is_displayed(), f'Esperado que o elemento {texto_formulario_enviado_sucesso_encontrado} não esteja na tela'

        driver.quit()
