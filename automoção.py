import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

####Colocar um input que carregara o caminho da planilha

mensagem2 = " \n Somos da Nagano Consignados, Representantes Bancários. \n O motivo do meu contanto é referente a aprovação da margem de 5% \n Temos a simulação desta margem disponivel!\n Caso tenha interesse responda Sim! Enviaremos as simulação \n "
mensagem = "\n Somos da Nagano Consignados, Representante do Banco Itaú Consignado e outros bancos \n estou entrando em contato referente a possibilidade de refinanciar seus contratos \n podendo reduzir suas taxas e liberar um valor em conta sem aumentar sua parcela \n Para receber a simulação digite SIM que irei verificar as melhores condições para te ajudar, ok?, \n Pode também aproveitar e visitar nossa página https://www.naganoconsultoria.com.br \n"
planilha = r"C:\Users\Naga-tour\Desktop\Projetos\Projetos Automoção\Planilhas\planilhamaikon.xlsx"






def enviar_msg(msg, driver):
    try:
        time.sleep(1)
        barra_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        barra_msg.send_keys(msg)

        
        time.sleep(4)
    except:  
        print("Telefone Errado")
        
        time.sleep(4)
def enviar_contato(lista_msg_excel):
    
    driver = webdriver.Chrome(r"C:\Users\Naga-tour\Desktop\Projetos\chromedriver.exe")

    driver.get('https://web.whatsapp.com/')
    time.sleep(3)

    print("Aperte o Enter para Continuar")
    input()




    for index, contato_excel in lista_msg_excel.iterrows():
        time.sleep(3)
        driver.get('https://web.whatsapp.com/send?phone=55'+ str(contato_excel[0]))
        time.sleep(20)

            # Envio da Msg :

        try:
            msg_incial = "Ola, Tudo bem?   " + contato_excel[1] + mensagem2
            enviar_msg(msg_incial, driver)
            
        except: 
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

