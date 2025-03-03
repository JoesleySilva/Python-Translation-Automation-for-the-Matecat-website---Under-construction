"""
Abrindo Google Chrome
Carregando o site Matecat
Mudando o idioma de origem para Português
Mudando o idioma de tradução para Italiana
Importa arquivos
Clica no botão Analize
Carrega a página "Translator"
"""

import os
import pyperclip  # Para copiar o texto para a área de transferência
import pyautogui  # Para simular Ctrl+V
import shutil
import subprocess
import time  # Para dar tempo entre as ações

from playwright.sync_api import sync_playwright
from time import sleep
from tkinter import messagebox, Tk

from pycparser.c_ast import Break

############################################## VARIAVEIS #################################################
global pagina, paginas, url_matecat

print('identificado usuário que está logado')
userlogged = os.getenv('USERNAME')

print ("diretório")
diretorio_arquivos_traduzir = fr"C:\Users\{userlogged}\Desktop\DOCUMENTOS PARA TRADUZIR"

userlogged = os.getenv('USERNAME')
if userlogged == "p527488":
    source_folder = f"C:\\Users\\{userlogged}\\Downloads\\Python\\pythonProject\\"
    destination_folder = 'E:\\Backups\\JSS\\Downloads\\Python\\'
else:
    source_folder = "C:\\Program Files\\Python311\\Scripts\\"
    destination_folder = 'E:\\Backups\\JSS\\Downloads\\Python\\'

print('Configurar o driver do Selenium (certifique-se de que o driver do navegador está no PATH)')
#driver = webdriver.Chrome()

##############################################################################################################

def backup_scripts():
    for file_name in os.listdir(source_folder):
        source = source_folder + file_name
        destination = destination_folder + file_name
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('copied', file_name)


def popup_abertura():
    root = Tk()
    root.withdraw()  # Oculta a janela principal

    # Exibir um pop-up de informação
    messagebox.showinfo("Aviso importante para execução do script", "Se o Chrome não abrir da primeira vez, não considere ainda erro. Este script roda melhor da segunda vez que é executado!")

def popup_encerramento():
    root = Tk()
    root.withdraw()  # Oculta a janela principal

    # Exibir um pop-up de informação
    messagebox.showinfo("SUCESSO", "Documentos traduzidos. Boa revisão!")

def fechar_todas_instancias_chrome():
    comando = "taskkill /f /im chrome.exe"
    subprocess.run(comando, shell=True)
    print("Todas as instâncias do Google Chrome foram encerradas.")


def iniciar_chrome_com_debug():
    # Caminho para o executável do Chrome no Windows
    caminho_chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    # Comando para iniciar o Chrome com depuração remota
    comando = [
        caminho_chrome,
        "--remote-debugging-port=9222",
        "--user-data-dir=C:\\tmp\\chrome-debug"  # Diretório temporário no Windows
    ]

    try:
        # Executa o comando de forma não bloqueante
        subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Google Chrome iniciando com depuração remota na porta 9222.")
    except FileNotFoundError:
        print(
            "Erro: Caminho para o Chrome não encontrado. Verifique se o Chrome está instalado no caminho especificado.")


'''
def inserindo_email():
    with sync_playwright() as p:
        # Conectar ao navegador existente via CDP
        navegador = p.chromium.connect_over_cdp("http://localhost:9222")

        # Obter todas as páginas abertas
        paginas = navegador.contexts[0].pages

        print("Buscando a lingua Portuges Brasil para clicar")

        xpath_botao_brasil = '//*[@id="source-lang"]/div[2]/div/div[2]/ul/li[225]/div/div/span'

        for i, pagina in enumerate(paginas):
            print(f"Aba {i+1}: {pagina.title()} - {pagina.url}")
            if "Fazer login nas Contas do Google" in pagina.title():
                print(f"Abrindo página com título: {pagina.title()}")
                pagina.goto(pagina.url)

                print('Preencher email')


                max_retries = 10
                retrY_interval = 1
                #elemento_carregamento = False
                for tentativa in range(max_retries):
                    try:
                        # Verifica o elemento
                        if pagina.locator(xpath_botao_brasil).is_visible():
                            elemento_carregamento = True
                            print("Campo de Inserir Email")
                            break
                    except Exception as e:
                        print(f"Tentativa {tentativa + 1}: Elemento não encontrado ainda. Erro: {e}")
                        continue

                    time.sleep(retrY_interval)

               # Aguarda 5 segundos antes de
                pagina.wait_for_timeout(5000)
                #// *[ @ id = "identifierId"]
                # Element = <input type="email" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="username webauthn" spellcheck="false" tabindex="0" aria-label="E-mail ou telefone" name="identifier" value="" aria-disabled="false" autocapitalize="none" id="identifierId" dir="ltr" data-initial-dir="ltr" data-initial-value="">
                #xpath = "//*[@id="identifierId"]"
                #pagina.fill("input[name='identifier']", "joesleysoares")

                print('Clica no botão "Proximo"')
                xpath_botao_proximo='//*[@id="identifierNext"]/div/button/div[3]'
                pagina.locator(xpath_botao_brasil).click()

                
                break
            else:
                continue
'''

def opendiretorio():
    time.sleep(7)  # tempo necessário para a primeira abertura da janela de arquivos
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(0.25)
    pyautogui.press("f4")
    time.sleep(0.25)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press("del")
    time.sleep(1)
    pyautogui.write(diretorio_arquivos_traduzir)
    time.sleep(1)
    pyautogui.press("enter")

def movimenta_janela_abrir():
    print("primeiro Tab")
    #pyautogui.press("tab")
    pyautogui.press("f6")
    time.sleep(0.5)

    print("Segundo Tab")
    #pyautogui.press("tab")
    pyautogui.press("f6")
    time.sleep(0.5)

    print("Terceiro Tab")
    #pyautogui.press("tab")
    pyautogui.press("f6")
    time.sleep(0.5)


    print("Inserido todos os arquivo")
    #pyautogui.press("tab")
    # pyautogui.press("f6")
    time.sleep(0.25)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.25)

    print("Enter")
    # pyautogui.press("tab")
    pyautogui.press("Enter")
    time.sleep(0.5)

def list_files_inline_with_quotes(diretorio_arquivos_traduzir):
    try:
        # Verifica se o diretório existe
        if not os.path.exists(diretorio_arquivos_traduzir):
            print(f"O diretório {diretorio_arquivos_traduzir} não existe.")
            return

        print('Lista os arquivos no diretório')
        files = [f'"{file}"' for file in os.listdir(diretorio_arquivos_traduzir) if os.path.isfile(os.path.join(diretorio_arquivos_traduzir, file))]

        # Imprime os arquivos um ao lado do outro, separados por espaço
        print(' '.join(files))

        # Concatena os arquivos em uma string
        result = ' '.join(files)

        # Copia o resultado para a área de transferência
        pyperclip.copy(result)
        print("Os nomes dos arquivos foram copiados para a área de transferência. Use Ctrl+V para colar.")

        # Dá tempo para o usuário focar no campo desejado
        print("Você tem 5 segundos para focar no campo onde deseja colar os nomes dos arquivos...")
        time.sleep(5)

        # Simula Ctrl+V para colar os nomes
        pyautogui.hotkey('ctrl', 'v')
        print("Os nomes dos arquivos foram colados com sucesso!")

        # Dá tempo para o usuário focar no campo desejado
        print("Você tem 5 segundos para focar no campo onde deseja colar os nomes dos arquivos...")
        time.sleep(5)

        print("Apertando o ENTER")
        pyautogui.press("enter")

    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")

class PageLoadTimeoutError(Exception):
    """Exceção customizada para indicar que o tempo limite foi atingido."""
    pass

def verificar_carregamento_pagina(pagina, tempo_total=300, intervalo=30):
    """
    Verifica o estado de carregamento da página a cada intervalo de tempo por até um tempo total.

    :param pagina: Objeto da página do Playwright.
    :param tempo_total: Tempo total para realizar as verificações (em segundos).
    :param intervalo: Intervalo entre as verificações (em segundos).
    """

    if tempo_total <= 0 or intervalo <= 0:
        raise ValueError("Os parâmetros `tempo_total` e `intervalo` devem ser maiores que zero.")

    tempo_inicio = time.time()

    while True:
        try:
            print("Verificando se a página está carregada...")
            pagina.wait_for_load_state("load", timeout=intervalo * 1000)  # Timeout em milissegundos
            print("Página carregada com sucesso!")
            return
        except Exception as e:
            print(f"Página ainda não carregou. Tentando novamente em {intervalo} segundos...")

        # Verifica se o tempo total foi excedido
        if time.time() - tempo_inicio >= tempo_total:
            print("Tempo limite de 5 minutos atingido. A página não foi carregada.")
            return

        # Verifica se o tempo total foi excedido
        if time.time() - tempo_inicio >= tempo_total:
            raise PageLoadTimeoutError(
                f"Tempo limite de {tempo_total // 60} minutos atingido. A página não foi carregada."
            )

        time.sleep(intervalo)


def wait_for_enabled_button(pagina):
    # Espera dinâmica com verificação de estado completo
    pagina.wait_for_selector('button.uploadbtn:not(.disabled):not([disabled]) >> text="Analyze"', state="visible",
                           timeout=60000)

    # Verificação adicional para garantir clicabilidade
    pagina.wait_for_function("""
        () => {
            const btn = document.querySelector('button.uploadbtn:not(.disabled):not([disabled])');
            return btn && 
                   btn.textContent.trim() === 'Analyze' &&
                   !btn.disabled &&
                   btn.getBoundingClientRect().width > 0;
        }
    """, timeout=60000)


def juncao_botao_usa_portugues_france_italian_confirm():
    global button, pagina, url_matecat

    with sync_playwright() as p:
        # Conectar ao navegador existente via CDP
        navegador = p.chromium.connect_over_cdp("http://localhost:9222")

        # Obter todas as páginas abertas
        paginas = navegador.contexts[0].pages

        print("Janelas/Aba abertas no navegador:")
        for i, pagina in enumerate(paginas):
            print(f"Aba {i + 1}: {pagina.title()} - {pagina.url}")

            # Exemplo: interagir com a primeira aba
            if paginas:
                pagina = paginas[0]
                print(f"\nInteragindo com a : {pagina.title()}")
                url_matecat ="https://www.matecat.com/"
                pagina.goto(url_matecat)
                verificar_carregamento_pagina(pagina)


                print('Botão From')
                termo = "From"
                #xpath_from = '//*[@id="source-lang"]/div/div/span'
                xpathfull_from = ('//'
                                  'html/body/div[2]/div[2]/div[2]/div/div[4]/div/div[1]/div/span')

                max_retries = 10
                retrY_interval = 1
                # elemento_carregamento = False
                for tentativa in range(max_retries):
                    try:
                        # Verifica o elemento
                        if pagina.locator(xpathfull_from).is_visible():
                            print(f"Elemento {termo} carregado e visivel")
                            break
                    except Exception as e:
                        print(f"Tentativa {tentativa + 1}: Elemento não encontrado ainda. Erro: {e}")
                        # continue

                time.sleep(retrY_interval)
                verificar_carregamento_pagina(pagina)
                pagina.locator(xpathfull_from).click()
                print(f'Clicando no botão "{termo}"')



        for i, pagina in enumerate(paginas):
            #print(f"Aba {i + 1}: {pagina.title()} - {pagina.url}")

            # Exemplo: interagir com a primeira aba
            if paginas:
                pagina = paginas[0]

                # Aguarda o estado "load" completo
                verificar_carregamento_pagina(pagina)

                print('Clicando no botão pt-BR')
                xpath_botao_portugues = '//*[@id="source-lang"]/div[2]/div/div[2]/ul/li[225]/div/div/span' #xpath Pt-BR

                max_retries = 10
                retry_interval = 1
                # elemento_carregamento = False
                for tentativa in range(max_retries):
                    try:
                        # Verifica o elemento
                        if pagina.locator(xpath_botao_portugues).is_visible():
                            print("Botão Português visivel")
                            break
                    except Exception as e:
                        print(f"Tentativa {tentativa + 1}: Elemento não encontrado ainda. Erro: {e}")
                        # continue


                time.sleep(retry_interval)
                verificar_carregamento_pagina(pagina)
                pagina.locator(xpath_botao_portugues).click()
                print('Botão Português clicado')

        for i, pagina in enumerate(paginas):

            # Exemplo: interagir com a primeira aba
            if paginas:
                pagina = paginas[0]

                # Aguarda o estado "load" completo
                verificar_carregamento_pagina(pagina)

                print('Clicando no botão French (France)')
                xpath_botao_frances = '//*[@id="target-lang"]/div/span'

                max_retries = 10
                retry_interval = 1
                for tentativa in range(max_retries):
                    try:
                        # Verifica o elemento
                        if pagina.locator(xpath_botao_frances).is_visible():
                            print("Elemento carregado e botão para clicar")
                            break
                    except Exception as e:
                        print(f"Tentativa {tentativa + 1}: Elemento não encontrado ainda. Erro: {e}")
                        # continue

                time.sleep(retry_interval)
                verificar_carregamento_pagina(pagina)
                pagina.locator(xpath_botao_frances).click()


        print('clicando na língua Italiana')
        for i, pagina in enumerate(paginas):

            # Exemplo: interagir com a primeira aba
            if paginas:
                pagina = paginas[0]

                print('Aguarda o estado "load" completo')
                verificar_carregamento_pagina(pagina)

                print('Clicando no botão "it-IT" Italian (Italy)')
                xpath_botao_italy = '//*[@id="matecat-modal-languages"]/div/div[2]/div[2]/ul[2]/li[46]/div/div/span'

                max_retries = 10
                retry_interval = 1
                # elemento_carregamento = False
                for tentativa in range(max_retries):
                    try:
                        # Verifica o elemento
                        if pagina.locator(xpath_botao_italy).is_visible():
                            print("Elemento carregado e botão para clicar Logar")
                            break
                    except Exception as e:
                        print(f"Tentativa {tentativa + 1}: Elemento não encontrado ainda. Erro: {e}")
                        # continue

                time.sleep(retry_interval)
                #pagina.wait_for_load_state("load")
                verificar_carregamento_pagina(pagina)
                pagina.locator(xpath_botao_italy).click()

        print('clicando no botão "CONFIRM"')
        for i, pagina in enumerate(paginas):

            # Exemplo: interagir com a primeira aba
            if paginas:
                pagina = paginas[0]

                print('Aguarda o estado "load" completo')
                #pagina.wait_for_load_state("load")
                verificar_carregamento_pagina(pagina)

                print('Clicando no botão Confirm ()')
                xpath_botao_confirm = '//*[@id="matecat-modal-languages"]/div/div[3]/div[2]/button'

                max_retries = 10
                retry_interval = 1
                for tentativa in range(max_retries):
                    try:
                        # Verifica o elemento
                        if pagina.locator(xpath_botao_confirm).is_visible():
                            print("Elemento carregado e botão para clicar Logar")
                            break
                    except Exception as e:
                        print(f"Tentativa {tentativa + 1}: Elemento não encontrado ainda. Erro: {e}")
                        # continue

                time.sleep(retry_interval)
                #pagina.wait_for_load_state("load")
                verificar_carregamento_pagina(pagina)
                pagina.locator(xpath_botao_confirm).click()

        print('clicando no link "or click here to browseNenhum arquivo escolhido"')
        for i, pagina in enumerate(paginas):

            # Exemplo: interagir com a primeira aba
            if paginas:
                pagina = paginas[0]

                print('Aguardando o estado "load" completo')
                #pagina.wait_for_load_state("load")
                verificar_carregamento_pagina(pagina)

                print('Clicando no no link "or click here to browseNenhum arquivo escolhido"')
                xpath_botao_upload_files = '//*[@id="droptest"]/div[2]/div[1]/div[1]/span/label'

                max_retries = 10
                retry_interval = 1
                for tentativa in range(max_retries):
                    try:
                        # Verifica o elemento
                        if pagina.locator(xpath_botao_upload_files).is_visible():
                            print("Elemento encontrando clicar")
                            break
                    except Exception as e:
                        print(f"Tentativa {tentativa + 1}: Elemento não encontrado ainda. Erro: {e}")
                        # continue

                time.sleep(retry_interval)
                print("Verificar o carregamento da página")
                verificar_carregamento_pagina(pagina)
                pagina.locator(xpath_botao_upload_files).click()


        print("##################################################")
        opendiretorio()


        print("##################################################")
        print('movimenta_janela_abrir')
        print("##################################################")
        movimenta_janela_abrir()


        print("##################################################")
        print("ANALYSE")
        print("##################################################")

        #print("Extrai todo o conteúdo HTML da página")
        #html_content = pagina.content()

        # Extrai todo o conteúdo HTML da página
        #html_content = pagina.content()

        # Verifica se o botão com o texto "Analyze" está presente

        """Opção 1
        if "Analyze" in html_content:
            print("Termo 'Analyze' encontrado no conteúdo da página.")
            try:
                print("MAIS EFICIENTE CLICAR NO BOTÃO XPATH")
                #button = pagina.locator("//button[contains(text(), 'Analyze')]")
                button = pagina.locator("//html/body/div[2]/div[3]/div/button").click()
                #button.click()
                print("Botão 'Analyze' clicado com sucesso!")



            except Exception as e:
                print(f"ERRO AO LOCALIZAR O BOTÃO ANALYZE. ERRO ---->: {e}")
        else:
            print("O botão 'Analyze' não foi encontrado no conteúdo da página.")
        
        # OPÇÃO 2
        # Aguardar e clicar no botão Analyze
        button_selector = 'button.button-component-container.primary.basic.big.uploadbtn >> text="Analyze"'

        try:
            # Esperar pelo botão estar visível (timeout de 30 segundos)
            pagina.wait_for_selector(button_selector, state="visible", timeout=30000)

            # Clicar no botão
            pagina.click(button_selector)
            print("Botão Analyze clicado com sucesso!")

        except Exception as e:
            print(f"Erro ao encontrar/clicar no botão: {e}")
        
        """
        '''
        # OPÇÃO 3  
        try:
            # Função para verificar a transformação do botão
            pagina.wait_for_function("""
                    () => {
                        const btn = document.querySelector('button.uploadbtn');
                        if (!btn) return false;

                        // Verificar se NÃO tem a classe 'disabled' e o texto correto
                        return !btn.classList.contains('disabled') && 
                               btn.textContent.trim() === 'Analyze';
                    }
                """, timeout=40000)

            # Clicar no botão agora habilitado
            pagina.click('button.button-component-container.primary.basic.big.uploadbtn:not(.disabled) >> text="Analyze"')
            print("Botão Analyze clicado com sucesso!")

        except Exception as e:
            print(f"Erro: {e}")
        '''

        '''
        # OPÇÃO 4
        # Aguarda até que o botão não tenha mais a classe 'disabled'
        pagina.wait_for_function("""
            () => {
                let btn = document.querySelector(".button-component-container.uploadbtn");
                return btn && !btn.classList.contains("disabled");
            }
        """)

        # Clica no botão
        pagina.click(".button-component-container.uploadbtn")

        print("Botão clicado com sucesso!")
        
        # OPÇÃO 5 com biblioteca
        # Primeiro espera o botão existir (mesmo que desabilitado)
        pagina.wait_for_selector('button.uploadbtn', state="attached")

        # Espera pela versão habilitada do botão
        wait_for_enabled_button(pagina)

        # Clica com verificação de clique bem-sucedido
        pagina.click('button.uploadbtn:not(.disabled):not([disabled]) >> text="Analyze"', force=True)

        print("Botão clicado com sucesso após habilitação!")
        '''

        """
        Abre um navegador sem uma URL inicial e exibe a URL da página carregada.

        :param tempo_total: Tempo máximo para aguardar a interação ou carregamento (em segundos).
        """
        """
        tempo_total = 60

        try:
            print("Navegador iniciado. Aguarde interações ou carregue uma página manualmente.")

            # Aguarda até que o estado de carregamento seja "load" ou até que o usuário carregue uma página
            pagina.wait_for_load_state("load", timeout=tempo_total * 1000)

            # Obtém e exibe a URL carregada
            url_carregada = pagina.url
            print(f"URL carregada: {url_carregada}")
            return url_carregada

        except Exception as e:
            print(f"Erro ao processar a página: {e}")
        """

        print("##################################################")
        intervalo = 30
        #url_alvo = url_matecat
        try:
            #print(f"Navegador iniciado. Monitore a URL. Alvo: {url_alvo}")

            while True:
                # Obtém a URL atual carregada
                #url_carregada = pagina.url
                #print(f"URL atual carregada: {url_carregada}")

                print('ANALYSE')
                # OPÇÃO 5 com biblioteca
                # Primeiro espera o botão existir (mesmo que desabilitado)
                pagina.wait_for_selector('button.uploadbtn', state="attached")

                # Espera pela versão habilitada do botão
                wait_for_enabled_button(pagina)

                # Clica com verificação de clique bem-sucedido
                pagina.click('button.uploadbtn:not(.disabled):not([disabled]) >> text="Analyze"', force=True)

                print("Botão clicado com sucesso após habilitação!")


                # Verifica se a URL é diferente da URL alvo
                #if url_carregada != url_alvo:
                #    print(f"URL alterada! Nova URL: {url_carregada}")

                #    break

                break
                print(f"URL ainda não alterada. Verificando novamente em {intervalo} segundos...")
                sleep(intervalo)

        except Exception as e:
            print(f"Erro ao monitorar a URL: {e}")




        print("##################################################")
        xpath_loading = "/html/body/div[2]/div[3]/div/button/span"
        termo_buscado = 'Loading'
        print(f'{termo_buscado}')
        print("##################################################")

        while True:
            try:
                pagina.locator(xpath_loading)
                print(f"Botão '{termo_buscado}' clicado com sucesso!")
                break  # Sai do loop após clicar com sucesso
            except Exception as e:
                print("Não foi possível clicar no botão. Tentando novamente em 5 segundos...")
                print(f"Erro ao encontrar ou clicar no botão: {e}")
                time.sleep(5)  # Espera 5 segundos antes da próxima tentativa

        print("##################################################")
        xpath_duvida = '/html/body/div[2]/div[1]/div/span[2]/div/div/button'
        balao_duvida = 'balao_duvida'
        print(f'{balao_duvida}')
        print("##################################################")

        while True:
            try:
                pagina.locator(xpath_duvida)
                print(f"Botão '{balao_duvida}' clicado com sucesso!")
                break  # Sai do loop após clicar com sucesso
            except Exception as e:
                print("Não foi possível clicar no botão. Tentando novamente em 5 segundos...")
                print(f"Erro ao encontrar ou clicar no botão: {e}")
                time.sleep(5)  # Espera 5 segundos antes da próxima tentativa



        print("##################################################")
        nome_analysis = 'Download Analysis Report'
        print(f'{nome_analysis}')
        print("##################################################")

        while True:
            try:
                #print("Tentando clicar no botão Analyze...")
                # Localiza e clica no botão pelo XPath
                #button = page.locator("xpath=/html/body/div[2]/div[3]/div/button")
                #button = page.locator("xpath=/html/body/div[2]/div[3]/div")
                pagina.locator(nome_analysis)
                print(f"Botão '{nome_analysis}' clicado com sucesso!")

                break  # Sai do loop após clicar com sucesso
            except Exception as e:
                print("Não foi possível clicar no botão. Tentando novamente em 5 segundos...")
                print(f"Erro ao encontrar ou clicar no botão: {e}")
                time.sleep(5)  # Espera 5 segundos antes da próxima tentativa


        """
        print("##################################################")
        print('BOTAO TRANSLATE')
        print("##################################################")
        verificar_carregamento_pagina(pagina)
        fullxpath_botao_translate = '//html/body/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]'
        Termo_buscado = 'Translate'
        if Termo_buscado in html_content:
            print(f"Termo '{Termo_buscado}' encontrado no conteúdo da página.")
            try:
                print("MAIS EFICIENTE BUSCA XPATH EM TELA")
                #element_translator = '<div class="open-translate ui primary button open ">Translate</div>'
                #xpathfull_translator = '/html/body/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]'
                #jspath_translator = 'document.querySelector("#analyze-container > div > div > div > div.project-top.ui.grid > div.compare-table.jobs.sixteen.wide.column > div > div > div.chunk.ui.grid.shadow-1 > div.activity-icons > div.activity-button > div.open-translate.ui.primary.button.open")'

                #button = locator.evaluate_handle(jspath_translator)
                #button.click()

                row_locator = pagina.locator("div")
                pagina.get_by_text("Translate").click()
                #button_translator.click()
                print(f"Botão {Termo_buscado} clicado com sucesso!")

            except Exception as e:
                print(f"ERRO AO LOCALIZAR O BOTÃO {Termo_buscado}. ERRO ---->: {e}")
        else:
            print("O botão 'Analyze' não foi encontrado no conteúdo da página.")
        """

#######################################################################################################################
print("INICIO da Execução do Script de Tradução de Documentos")
#######################################################################################################################

if __name__ == "__main__":

    fechar_todas_instancias_chrome()

    popup_abertura()

    iniciar_chrome_com_debug()

    juncao_botao_usa_portugues_france_italian_confirm()

    #list_files_inline_with_quotes(diretorio_arquivos_traduzir)

    popup_encerramento()

    #######################################################################################################################
    print("TERMINO")
    #######################################################################################################################

    #pagina.close()
