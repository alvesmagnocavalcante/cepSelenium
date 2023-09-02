# Importando as bibliotecas necessárias
from selenium import webdriver as driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import *

# Função para realizar a pesquisa do CEP
def pesquisaCep():
    # Configurando as opções do Chrome WebDriver
    options = Options()
    options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)

    # Inicializando o navegador Chrome
    navegador = driver.Chrome(options=options)

    # Abrindo a página dos Correios para pesquisa de CEP
    navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

    # Aguardando 1 segundo (evitar sobrecarga no servidor)
    navegador.implicitly_wait(1)

    # Localizando o campo de entrada do CEP e inserindo o valor digitado pelo usuário
    campo_cep = navegador.find_element(By.NAME, "endereco")
    campo_cep.clear()
    campo_cep.send_keys(campoDigitavelCEP.get())

    # Clicando no botão de pesquisa
    navegador.find_element(By.NAME, "btn_pesquisar").click()

    # Aguardando 1 segundo para a página carregar
    navegador.implicitly_wait(1)

    # Coletando informações da rua
    rua_elements = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')
    if rua_elements:
        rua = rua_elements[0].text
        lblRua.config(text="Rua: " + rua)

    # Coletando informações do bairro
    bairro_elements = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')
    if bairro_elements:
        bairro = bairro_elements[0].text
        lblBairro.config(text="Bairro: " + bairro)

    # Coletando informações da cidade
    cidade_elements = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')
    if cidade_elements:
        cidade = cidade_elements[0].text
        lblCidade.config(text="Cidade: " + cidade)

    # Coletando informações do CEP
    cep_elements = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')
    if cep_elements:
        cep = cep_elements[0].text
        lblCep.config(text="CEP: " + cep)
    else:
        erro.config(text="Digite um CEP válido!")

    # Fechando o navegador
    navegador.quit()

# Criando a janela principal da interface gráfica
janela = Tk()
janela.geometry("720x400")

# Configurando a estrutura de layout
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)

# Criando um rótulo para instruções
instrucao = Label(text="Digite o CEP: ", font="Arial 20")
instrucao.grid(row=1, column=0, pady=30, sticky="E")

# Criando uma caixa de entrada para o CEP
campoDigitavelCEP = Entry(font="Arial 20")
campoDigitavelCEP.grid(row=1, column=1)

# Criando um botão para iniciar a pesquisa
btnPesquisar = Button(text="Pesquisar", font="Arial 20", command=pesquisaCep)
btnPesquisar.grid(row=2, column=0, columnspan=2, pady=30)

# Criando rótulos para exibir as informações do endereço
lblRua = Label(font="Arial 20")
lblRua.grid(row=3, column=0, columnspan=2, sticky="NSEW")

lblBairro = Label(font="Arial 20")
lblBairro.grid(row=4, column=0, columnspan=2, sticky="NSEW")

lblCidade = Label(font="Arial 20")
lblCidade.grid(row=5, column=0, columnspan=2, sticky="NSEW")

lblCep = Label(font="Arial 20")
lblCep.grid(row=6, column=0, columnspan=2, sticky="NSEW")

# Criando um rótulo para exibir mensagens de erro
erro = Label(font="Arial 20")
erro.grid(row=6, column=0, columnspan=2, sticky="NSEW")

# Iniciando a interface gráfica
janela.mainloop()
