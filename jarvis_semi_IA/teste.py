import pyautogui as pg 
from time import sleep
sleep(2)

p = pg.locateCenterOnScreen('imgs/playlist.png', confidence=0.8)

pg.click(p.x,p.y)