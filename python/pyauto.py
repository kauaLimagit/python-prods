import pyautogui as pg
from time import sleep
 
cod = 0
continuar = False
 
emails = ['kaua.lima2@fatec.sp.gov.br','vinicius.souza165@fatec.sp.gov.br','aristeu.souza01@fatec.sp.gov.br','caue.nascimento01@fatec.sp.gov.br','joao.silva943@fatec.sp.gov.br','davi.soares4@fatec.sp.gov.br','eduardo.silva338@fatec.sp.gov.br']

while continuar == False:
    codemail = input("digite o codigo de email ou digite ( todos ) para verificar Emails e seus codigos>")
    
    if codemail == 'todos':
        for i in emails:
            print(f'Email cod={cod} corresponde a {i}')
            print('-----------------------------------------')
            cod += 1
    else:
        cod = 0
        continuar = True
    
continuar = False

senha = input('senha da conta >')

codemail = int(codemail)
 
def en():
  pg.press('Enter')
 
pg.hotkey('win', 'r')
 
while continuar == False:
    try:
        fotowinr = pg.locateOnScreen('references/WinR.png',confidence=0.8)
        if fotowinr != None:
            continuar = True
    except:
        try:
            fotowinr = pg.locateOnScreen('references/WinR.png',confidence=0.8)
            if fotowinr != None:
                continuar = True
        except:
            print('tentando achar imagem!!')
 
continuar = False
 
pg.typewrite('chrome')
pg.press('Enter')
 
while continuar == False:
    try:
        sleep(1)
        fototelacheia = pg.locateOnScreen('references/TelaCheia.png',confidence=0.8)
        if fototelacheia != None:
            pg.hotkey('Win', 'up')      
     
    except:
        try:
            fotochromenormal = pg.locateOnScreen('references/ChromeNormal.png', confidence=0.8)
            if fotochromenormal != None:
                continuar = True
        except:
            print('tentando achar chrome!!')
       
 
continuar = False
 
pg.hotkey('Ctrl', 'Shift', 'n')
 
while continuar == False:
    try:
        fotochromeanonimo = pg.locateOnScreen('references/ChromeAnonimo.png',confidence=0.8)
        if fotochromeanonimo != None:
            continuar = True
    except:
        try:
            fotochromeanonimo = pg.locateOnScreen('references/ChromeAnonimo.png',confidence=0.8)
            if fotochromeanonimo != None:
                continuar = True
        except:
            print('tentando achar imagem!!')
 
continuar = False
 
pg.typewrite('https://teams.microsoft.com/v2/')
 
en()
 
while continuar == False:
    try:
        teamserrado = pg.locateCenterOnScreen('references/TeamsErrado.png',confidence=0.8)
        if teamserrado != None:
            pg.click(teamserrado.x,teamserrado.y)
 
    except:
        try:
            quase = pg.locateCenterOnScreen('references/QuaseConta.png',confidence=0.8)
            if quase != None:
                pg.click(quase.x,quase.y)
        except:
            try:
                entrar = pg.locateCenterOnScreen('references/TeamsEntrar.png',confidence=0.8)
                if entrar != None:
                    pg.click(entrar.x,entrar.y)
            except:
                try:
                    fototemsemail = pg.locateOnScreen('references/TeamsEmailId.png',confidence=0.8)
                    if fototemsemail != None:
                        continuar = True
                except:
                    print('tentando achar imagem!!')
       
continuar = False
 
pg.typewrite(emails[codemail])
 
pg.press('Enter')
 
sleep(3)
 
pg.typewrite(senha)
 
pg.press('Enter')
 
sleep(3)
 
pg.hotkey('Ctrl', 't')
 
sleep(1)
 
pg.typewrite('https://web.whatsapp.com/')
 
sleep(1)
 
en()
 
# multiplicidade interfere na construção dos metodos