import speech_recognition as sr
from playsound import playsound
from time import sleep
from random import randint
import pyautogui as pg

# ações

ouvir = False
desativar = False

def ativar():
    codfala = randint(0,1)
    playsound(f'./respostas/ativacao{codfala}.mp3')

def play_song(t):
    playsound('./respostas/Repsom.mp3')

    startnome = 0
    nome = ''

    for i in t:
        if startnome == 1:
            if i == 'ç':
                nome += 'c'
            elif i == 'õ':
                nome += 'o'
            else:
                nome += i

        elif i == ' ':
            startnome = 1

    sleep(1)
    playsound(f'./musicas/{nome.lower()}.mp3')

def pesquisa(t):

    startpesquisa = 0
    pesquisar = ''

    for i in t:
        if startpesquisa == 1:
            pesquisar += i
        elif i == ' ':
            startpesquisa = 1

    playsound('./respostas/pesquisa.mp3')

    seguir = False

    pg.hotkey('Win', 'r')

    while seguir == False:
        cmd = pg.locateOnScreen('imgs/cmd.png', confidence=0.5)
        if cmd != None:
            pg.typewrite('chrome')
            pg.hotkey('Enter')
            seguir = True
    
    seguir = False

    while seguir == False:
        google = pg.locateOnScreen('imgs/google.png', confidence=0.5)
        if google != None:
            pg.typewrite(pesquisar)
            pg.hotkey('Enter')
            seguir = True
    
def standby():
    playsound('./respostas/standby.mp3')

def desligar():
    playsound('./respostas/desligar.mp3')

def aujanela(t):
    playsound('./respostas/aumentarjanela.mp3')

    last_confirm = 0
    last = 0

    valor_a_aumentar = 0

    for i in t:
        last_confirm +=1

    for i in t:
        if last == last_confirm-1:
            valor_a_aumentar += int(i)
        else:
            last+=1

    return valor_a_aumentar

def redjanela():
    playsound('./respostas/janelapadrao.mp3')
    return 0.7

def abrirapp(t):
    playsound('./respostas/abrirapp.mp3')
    app = ''
    contar = 0
    for i in t:
        if contar == 1:
            app += i
        elif i == ' ':
            contar += 1

    pg.hotkey('Win')

    while True:
        win = pg.locateOnScreen('imgs/win.png', confidence=0.7)
        if win != None:
            pg.typewrite(app)
            break
        
    while True:
        abrir = pg.locateOnScreen('imgs/abrirapp.png', confidence=0.7)
        if abrir != None:
            pg.hotkey('Enter')
            break
    
def spotfy():
    pg.hotkey('Win', 'r')
    while True:
        cmd = pg.locateOnScreen('imgs/cmd.png', confidence=0.7)
        if cmd != None:
            pg.typewrite('chrome')
            pg.hotkey('Enter')
            break
        
    while True:
        google = pg.locateOnScreen('imgs/google.png', confidence=0.5)
        if google != None:
            pg.typewrite('spotfy.com')
            pg.hotkey('Enter')
            break
        
    while True:
        try:
            playlist = pg.locateCenterOnScreen('imgs/playlist.png', confidence=0.8)
            if playlist != None:
                pg.click(playlist.x, playlist.y)
                pg.click()
                pg.click()
                break
        except:
            try:
                playlist = pg.locateCenterOnScreen('imgs/playlist.png', confidence=0.8)
                if playlist != None:
                    pg.moveTo(playlist.x, playlist.y)
                    break
            except:
                print('não achei')
            
    while True:
        play = pg.locateCenterOnScreen('imgs/play.png', confidence=0.5)
        if google != None:
            pg.click(play.x,play.y)
            break
        
spotfy()
    
rec = sr.Recognizer()

janela = 0.7

with sr.Microphone() as mic:
    while desativar == False:
        rec.adjust_for_ambient_noise(mic)
        rec.pause_threshold = janela

        print('fale')

        audio = rec.listen(mic,)

        try:
            print('reconhecendo')
            texto = rec.recognize_google(audio, language='pt-BR')
            print(f'voce disse {texto}')

            if 'Jarvis' in texto or 'Tiago' in texto or 'Charles' in texto or 'Thiago' in texto or 'Jar' in texto:
                ouvir = True
                ativar()
            elif ('tocar' in texto or 'escutar' in texto) and ouvir:
                play_song(texto)
            elif ('pesquisar' in texto or 'P esquisar' in texto) and ouvir:
                pesquisa(texto)
            elif ('stand-by' in texto or 'sair' in texto or 'standy by' in texto) and ouvir:
                standby()
                ouvir = False
            elif ('aumentar janela' in texto or 'aumentar a janela' in texto) and ouvir:
                janela = aujanela(texto)
            elif ('reduzir janela' in texto or 'diminuir janela' in texto or 'voltar janela' in texto) and ouvir:
                janela = redjanela()
            elif ('abrir' in texto or 'executar' in texto) and ouvir:
                abrirapp(texto)
            elif ('desligar' in texto or 'amoleça meu') and ouvir == True:
                desligar()
                sleep(1)
                desativar = True
                
        except:
            print('tendi nada')