from tkinter import *
import pygame
import pyganim
from pygame import *
from player import *
from blocks import *

root = Tk()
root.title("P-Junior")
root.geometry("800x600")
root.iconbitmap("logo.ico")
WIN_WIDTH = 800 #Ширина вікна
WIN_HEIGHT = 640 # Висота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) 

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

        
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемсЯ дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return Rect(l, t, w, h)        

def main(event):
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY) # Створюємо вікно
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Створення відтворюваної поверхні
                                         # фон
    bg = pygame.image.load("fon1.jpg")    # Заливка фону
    
    pygame.mixer.music.load("mix.mp3")
    pygame.mixer.music.play()
    
   
    hero = Player(55,55) # створюємо персонажа по (x,y) координатам
    left = right = False # стоїмо(за замовчуванням)
    up = False
    
    entities = pygame.sprite.Group() # Всі обєкти
    platforms = [] # те об що будемо опиратися
    
    entities.add(hero)

    level = [
       "----------------------------------",
       "-                                -",
       "--------        **  ----------   -",
       "-      ----                      -",
       "-                        ---------",
       "-  --*-------                    -",
       "-           --*-----             -",
       "-----              ---------------",
       "-   ------                       -",
       "-        -----     -----         -",
       "-****                  -----------",
       "-               *                -",
       "-   -----   -----------**------- -",
       "-                                -",
       "-----**       ----   -------------",
       "-      -----                 -----",
       "-         -----                  -",
       "-------       *---------    ------",
       "-       **                       -",
       "-------      ----       ---      -",
       "      ---------       ------**-  -",
       "-                                -",
       "-**-----        ---*-----      T -",
       "----------------------------------"]
       
    timer = pygame.time.Clock()
    x=y=0 # координати
    for row in level: # весь рядок
        for col in row: # кожний символ
            if col == "-":
                #створюємо блок, заливка, малюємо
                pf = Platform(x,y)
                entities.add(pf)
                platforms.append(pf)

            if col == "*":
                bd = BlockDie(x,y)
                entities.add(bd)
                platforms.append(bd)

            if col == "T":
                test = Test(x,y)
                entities.add(test)
                platforms.append(test)

            x += PLATFORM_WIDTH #блоки платфори на ширині блоків
        y += PLATFORM_HEIGHT    #те саме з висотою
        x = 0                   #з кожного нового рядка починаємо з нуля
        #перебираємо двовимірний масив левел і заміняємо символи - на блоки    
    total_level_width  = len(level[0])*PLATFORM_WIDTH # Вираховуємо фактичну ширину
    total_level_height = len(level)*PLATFORM_HEIGHT   # рівня і висоту
    
    camera = Camera(camera_configure, total_level_width, total_level_height) 
    
    while 1: # Основний цикл програми
        timer.tick(60)
        for e in pygame.event.get(): # Обрабка подій
            if e.type == QUIT:
                running = False
                #тобто, якщо нажали клавішу вверх, то прижок, якщо відпустили - зупиняємось
                #так само для "вліво" і "вправо"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True


            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        screen.blit(bg, (0,0))      # Кожну ітерацію все перемальовуємо 


        camera.update(hero) # централізація камери відносно персонажу
        hero.update(left, right, up,platforms) # пересування
        #entities.draw(screen)  #відтворення(для розгиреного екрану текстури летять!!!!)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
    
        pygame.display.update()     # обновлення і вивід всіх змін на екран
    
im2=PhotoImage(file='fon.gif')
l=Label(root,image=im2)
im=PhotoImage(file="start.gif")
l.pack()
btn = Button(image=im,
             background="Black",
             height="100",
             width="400")
btn.place(x=200,y=450)
btn.bind('<Button->', main)
root.configure(background="black")
btn.pack()
root.mainloop()

if __name__ =="__main__":
    main()
