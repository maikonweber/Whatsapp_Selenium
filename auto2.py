import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
####Colocar um input que carregara o caminho da planilha

mensagem = "\n Muito Prazer, Somos da Nagano Consignados. Somos correspondentes bancários do Itaú.\n Verificamos um possibilidade de liberação de crédito disponível. \n Gostaria de verificar os valores que podem ser liberados. \n"


planilha = r"C:\Users\Naga-tour\Desktop\Projetos\Projetos Automoção\Leads06.xlsx"


def enviar_msg(msg, driver, lista_msg_excel):
    try:
        barra_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        barra_msg.send_keys(msg)

        time.sleep(5)
    except:  
        print("Telefone Errado")
        time.sleep(5)
def enviar_contato(lista_msg_excel):
   
    driver = webdriver.Chrome(r"C:\Users\Naga-tour\Desktop\Projetos\chromedriver.exe")

    driver.get('https://web.whatsapp.com/')
    time.sleep(3)

    print("Aperte o Enter para Continuar")
    input()



    
    for index, contato_excel in lista_msg_excel.iterrows():
        driver.get('https://web.whatsapp.com/send?phone=55'+ str(contato_excel[0]))
        time.sleep(20)

            # Envio da Msg :

        try:
            msg_incial = "Ola, " + contato_excel[1] + mensagem 
            enviar_msg(msg_incial, driver)
        except:
            time.sleep(5)
            print('Error')
            


#Metodo Main Carrega os Arquivos no Panda.

def main():

    col_nome = "Nome"
    col_mensagem = "Mensagem"
    col_telefone = "Telefone"

    info_excel = pd.read_excel(planilha)

    lista_msg_excel = (info_excel[[col_telefone,col_nome]])
    lista_telefone = (info_excel[col_telefone])

    df_lista_msg_excel = pd.DataFrame(lista_msg_excel)
    df_telefone_excel = pd.DataFrame(lista_telefone)

    
    enviar_contato(df_lista_msg_excel)
#######################

main( )   

