from pygame import *
from tkinter import *
import pyganim
import os
import blocks
import test

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
JUMP_POWER = 10
GRAVITY = 0.5 # Сила, яка тягне вниз
ANIMATION_DELAY = 0.1 # швидкість зміни кадрів
ICON_DIR = os.path.dirname(__file__) #  Повний шлях до каталогу файлів

ANIMATION_RIGHT = [('%s/player/p_right.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/player/p_left.png' % ICON_DIR)]
ANIMATION_JUMP_LEFT = [('%s/player/p_left.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/player/p_right.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/player/p_right.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/player/p_right.png' % ICON_DIR, 0.1)]

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #швидкість пересування. 0 - стояти на місці
        self.startX = x # початкова позиція Х
        self.startY = y
        self.yvel = 0 # шкидкість вертикального пересування
        self.onGround = False #чи знаходиться персонаж на "землі"
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямокутний обєкт
        self.image.set_colorkey(Color(COLOR)) # прозорий фон
#Анимація пересування вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
#Анимація пересування вліво       
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0)) #стоїть
        
        self.boltAnimJumpLeft= pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()
        
        self.boltAnimJumpRight= pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()
        
        self.boltAnimJump= pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()
        

    def update(self, left, right, up, platforms):
        
        if up:
            if self.onGround: # прижок коли можна відштовхнутись від землі
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))
               
                       
        if left:
            self.xvel = -MOVE_SPEED # Ліво = x- n
            self.image.fill(Color(COLOR))
            if up: # прижок вліво(окрема анімація)
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))
 
        if right:
            self.xvel = MOVE_SPEED # Право = x + n
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))
         
        if not(left or right): # стоїть коли немає завдання кудись іти
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))
            
        if not self.onGround:
            self.yvel +=  GRAVITY
            
        self.onGround = False; # чи є персонаж на "землі" 
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим своє положення на xvel
        self.collide(self.xvel, 0, platforms)
   
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): # якщо персонаж дотикається з платформою

                if xvel > 0:                      # якщо рухається вправо
                    self.rect.right = p.rect.left # то не рухається

                if xvel < 0:                      # якщо рухається вліво
                    self.rect.left = p.rect.right # заперечення дії

                if yvel > 0:                      # якщо падає вниз
                    self.rect.bottom = p.rect.top # заперечення дії
                    self.onGround = True          # стає на "землю"
                    self.yvel = 0                 

                if yvel < 0:                      # якщо рухається вверх
                    self.rect.top = p.rect.bottom # заперечення
                    self.yvel = 0                 # енергія прижка пропадає

                if isinstance(p, blocks.BlockDie): #якщо блок-інтеграл то помирає
                    self.die()

                elif isinstance(p, blocks.Test):
                    self.test_t()
                    
     #поведінка героя при зіткнені з "інтегралом"
    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

    def die(self):
        time.wait(500)
        self.teleporting(self.startX, self.startY)

    def test_t(event):
        import tkinter

        class Test(Frame):

            def __init__(self,window):
                super().__init__(window)
                self.grid()
                self.__init_widgets()

            def __init_widgets(self):
                self.__lb1 = Label(self, text = "1) Скільки буде 2+2*2? Відповідь дайте типом float.")
                self.__lb1.grid(row=0, column=0, columnspan=6, sticky=W)

                self.__btn11 = Button(self, text="     6     ",background="pink",activebackground="red", command = self.__false1)
                self.__btn11.grid(row=1, column=0, sticky=W)

                self.__btn12 = Button(self, text="    6.0    ",background="pink",activebackground="green", command = self.__true1)
                self.__btn12.grid(row=1, column=1, sticky=W)

                self.__btn13 = Button(self, text="     8     ",background="pink",activebackground="red", command = self.__false1)
                self.__btn13.grid(row=1, column=2, sticky=W)

                self.__btn14 = Button(self, text="    8.0    ",background="pink",activebackground="red", command = self.__false1)
                self.__btn14.grid(row=1, column=3, sticky=W)

                self.__l1=Label(self, text=" ")
                self.__l1.grid(row=1, column=5, columnspan=6,sticky=W)

                self.__lbl2 = Label(self, text = " ")
                self.__lbl2.grid(row=2, column=0, columnspan=6, sticky=W)

                self.__lb2 = Label(self, text = "2) Вкажіть чому рівне у: dy=0*dx")
                self.__lb2.grid(row=3, column=0, columnspan=4, sticky=W)

                self.__btn21 = Button(self, text="     x     ",background="pink",activebackground="red", command = self.__false2)
                self.__btn21.grid(row=4, column=0, sticky=W)

                self.__btn22 = Button(self, text="     0     ",background="pink",activebackground="red", command = self.__false2)
                self.__btn22.grid(row=4, column=1, sticky=W)

                self.__btn23 = Button(self, text="     C     ",background="pink",activebackground="green", command = self.__true2)
                self.__btn23.grid(row=4, column=2, sticky=W)

                self.__btn24 = Button(self, text="     1     ",background="pink",activebackground="red", command = self.__false2)
                self.__btn24.grid(row=4, column=3, sticky=W)

                self.__l2=Label(self, text=" ")
                self.__l2.grid(row=4, column=5, columnspan=6,sticky=W)

                self.__lbl3 = Label(self, text = " ")
                self.__lbl3.grid(row=5, column=0, columnspan=6, sticky=W)

                self.__lb3 = Label(self, text = "3) Чому дорівнює 1/+0?")
                self.__lb3.grid(row=6, column=0, columnspan=6, sticky=W)

                self.__btn31 = Button(self, text="   +inf    ",background="pink",activebackground="green", command = self.__true3)
                self.__btn31.grid(row=7, column=0, sticky=W)

                self.__btn32 = Button(self, text="   -inf    ",background="pink",activebackground="red", command = self.__false3)
                self.__btn32.grid(row=7, column=1, sticky=W)
                
                self.__btn33 = Button(self, text="     0     ",background="pink",activebackground="red", command = self.__false3)
                self.__btn33.grid(row=7, column=2, sticky=W)

                self.__btn34 = Button(self, text="     1     ",background="pink",activebackground="red", command = self.__false3)
                self.__btn34.grid(row=7, column=3, sticky=W)

                self.__l3=Label(self, text=" ")
                self.__l3.grid(row=7, column=5, columnspan=6,sticky=W)

                self.__lbl4 = Label(self, text = " ")
                self.__lbl4.grid(row=8, column=0, columnspan=6, sticky=W)

                self.__lb4 = Label(self, text = "4) Як позначається 'логічне і'?")
                self.__lb4.grid(row=9, column=0, columnspan=6, sticky=W)

                self.__btn41 = Button(self, text="    ||     ",background="pink",activebackground="red", command = self.__false4)
                self.__btn41.grid(row=10, column=0, sticky=W)

                self.__btn42 = Button(self, text="    ==     ",background="pink",activebackground="red", command = self.__false4)
                self.__btn42.grid(row=10, column=1, sticky=W)

                self.__btn43 = Button(self, text="    %%     ",background="pink",activebackground="red", command = self.__false4)
                self.__btn43.grid(row=10, column=2, sticky=W)

                self.__btn44 = Button(self, text="     &&    ",background="pink",activebackground="green", command = self.__true4)
                self.__btn44.grid(row=10, column=3, sticky=W)

                self.__l4=Label(self, text=" ")
                self.__l4.grid(row=10, column=5, columnspan=6,sticky=W)

                self.__lbl5 = Label(self, text = " ")
                self.__lbl5.grid(row=11, column=0, columnspan=6, sticky=W)

                self.__lb5 = Label(self, text = "5) P(4)(перестановка без повторень)=...?")
                self.__lb5.grid(row=12, column=0, columnspan=6, sticky=W)

                self.__btn51 = Button(self, text="    4^2    ",background="pink",activebackground="red", command = self.__false5)
                self.__btn51.grid(row=13, column=0, sticky=W)

                self.__btn52 = Button(self, text="    4!     ",background="pink",activebackground="green", command = self.__true5)
                self.__btn52.grid(row=13, column=1, sticky=W)

                self.__btn53 = Button(self, text="     4     ",background="pink",activebackground="red", command = self.__false5)
                self.__btn53.grid(row=13, column=2, sticky=W)

                self.__btn54 = Button(self, text="    4^4    ",background="pink",activebackground="red", command = self.__false5)
                self.__btn54.grid(row=13, column=3, sticky=W)

                self.__l5=Label(self, text=" ")
                self.__l5.grid(row=13, column=5, columnspan=6,sticky=W)

                self.__l6=Label(self, text=" ")
                self.__l6.grid(row=14, column=0, columnspan=5, sticky=W)

                self.__btnresult = Button(self, text="Завершити", command=self.result,background="pink")
                self.__btnresult.grid(row=15,column=2, columnspan=5,sticky=W)
                
                self.__result=Label(self, text=" ")
                self.__result.grid(row=16, column=0, columnspan=6,sticky=W)


               

            def __true1(self):
                self.__l1["text"]="True"

            def __false1(self):
                self.__l1["text"]="False"

            def __true2(self):
                self.__l2["text"]="True"

            def __false2(self):
                self.__l2["text"]="False"

            def __true3(self):
                self.__l3["text"]="True"

            def __false3(self):
                self.__l3["text"]="False"

            def __true4(self):
                self.__l4["text"]="True"

            def __false4(self):
                self.__l4["text"]="False"

            def __true5(self):
                self.__l5["text"]="True"

            def __false5(self):
                self.__l5["text"]="False"

            def result(self):
                
                    
                self.__result["text"]="Ви переможець конкурсу найрозумніший"
                
                
                

        main_window=Tk()

        main_window.title("Test")
        main_window.geometry("400x400")
        main_window.iconbitmap("logo.ico")


        test = Test(main_window)
        main_window.mainloop()
        
        

       
                        

   

    
    











        
