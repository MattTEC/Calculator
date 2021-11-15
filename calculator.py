from math import sqrt
import pygame, sys
pygame.font.init()
pygame.display.set_caption("Calculator")
fnt = pygame.font.SysFont("Consolas", 50)
screen = pygame.display.set_mode((320, 500))
currentnum = 0
currentnum2 = 0
currentstr = "0"
funcsave = ""
one = pygame.image.load("number-1.png").convert_alpha()
two = pygame.image.load("number-2.png").convert_alpha()
three = pygame.image.load("number-3.png").convert_alpha()
four = pygame.image.load("number-4.png").convert_alpha()
five = pygame.image.load("number-5.png").convert_alpha()
six = pygame.image.load("number-6.png").convert_alpha()
seven = pygame.image.load("number-7.png").convert_alpha()
eight = pygame.image.load("number-8.png").convert_alpha()
nine = pygame.image.load("number-9.png").convert_alpha()
divide = pygame.image.load("divide.png").convert_alpha()
equal = pygame.image.load("equal.png").convert_alpha()
minus = pygame.image.load("minus.png").convert_alpha()
plus = pygame.image.load("plus.png").convert_alpha()
pom = pygame.image.load("plusorminus.png").convert_alpha()
root = pygame.image.load("root.png").convert_alpha()
square = pygame.image.load("square.png").convert_alpha()
zero = pygame.image.load("zero.png").convert_alpha()
dot = pygame.image.load("dot.png").convert_alpha()
x = pygame.image.load("letter-x.png").convert_alpha()
c = pygame.image.load("letter-c.png").convert_alpha()


textsurface = fnt.render(currentstr, False, (0, 0, 0))

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #mouse pos
        pos = pygame.mouse.get_pos()

        #check mouseover and click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0]== 0:
            self.clicked = False
                


        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#coords go:
#10 430
#90 430
#170 430
#250 430
#10 360 

def rightplace():
    if len(currentstr) > 1:
        if currentstr(0) == 0:

    takeaway = len(currentstr)
    takeaway = takeaway * 40
    takeaway = 320 - takeaway
    screen.blit(textsurface,(takeaway,50))


button_one = Button(10, 360, one, 0.12)
button_two = Button(90, 360, two, 0.12)
button_three = Button(170, 360, three, 0.12)
button_four = Button(10, 290, four, 0.12)
button_five = Button(90, 290, five, 0.12)
button_six = Button(170, 290, six, 0.12)
button_seven = Button(10, 220, seven, 0.12)
button_eight = Button(90, 220, eight, 0.12)
button_nine = Button(170, 220, nine, 0.12)
button_divide = Button(250, 150, divide, 0.12)
button_equal = Button(250, 430, equal, 0.12)
button_minus = Button(250, 290, minus, 0.12)
button_plus = Button(250, 360, plus, 0.12)
button_pom = Button(10, 430, pom, 0.12)
button_root = Button(170, 150, root, 0.12)
button_square = Button(90, 150, square, 0.12)
button_zero = Button(90, 430, zero, 0.12)
button_dot = Button(170, 430, dot, 0.12)
button_x = Button(250, 220, x, 0.12)
button_c = Button(10, 150, c, 0.12)




while True:
    

    screen.fill((255, 255, 255))
    

    if button_one.draw():
        if funcsave != "":
            currentstr = currentstr + "1"
            currentnum2 = currentstr
        else:
            currentstr = currentstr + "1"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    if button_two.draw():
        if funcsave != "":
            currentstr = currentstr + "2"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "2"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    if button_three.draw():
        if funcsave != "":
            currentstr = currentstr + "3"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "3"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    if button_four.draw():
        if funcsave != "":
            currentstr = currentstr + "4"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "4"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    if button_five.draw():
        if funcsave != "":
            currentstr = currentstr + "5"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "5"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    if button_six.draw():
        if funcsave != "":
            currentstr = currentstr + "6"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "6"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    if button_seven.draw():
        if funcsave != "":
            currentstr = currentstr + "7"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "7"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    if button_eight.draw():
        if funcsave != "":
            currentstr = currentstr + "8"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "8"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    if button_nine.draw():
        if funcsave != "":
            currentstr = currentstr + "9"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "9"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    
    if button_divide.draw():
        funcsave = "divide"
        currentstr = ""
    
    if button_equal.draw():
        if funcsave == "plus":
            value = float(currentnum) + float(currentnum2)
            currentstr = str(value)
            textsurface = fnt.render(currentstr, False, (0, 0, 0))  
            currentnum = value 

        if funcsave == "minus":
            value = float(currentnum) - float(currentnum2)
            currentstr = str(value) 
            textsurface = fnt.render(currentstr, False, (0, 0, 0))
            currentnum = value   

        if funcsave == "square":
            value = float(currentnum) ** float(currentnum2)
            currentstr = str(value) 
            textsurface = fnt.render(currentstr, False, (0, 0, 0))
            currentnum = value   

        if funcsave == "times":
            value = float(currentnum) * float(currentnum2)
            currentstr = str(value)
            textsurface = fnt.render(currentstr, False, (0, 0, 0))
            currentnum = value

        if funcsave == "divide":
            value = float(currentnum) / float(currentnum2)
            currentstr = str(value)
            textsurface = fnt.render(currentstr, False, (0, 0, 0))
            currentnum = value

        funcsave = ""
    
    if button_minus.draw():
        funcsave = "minus"
        currentstr = ""
    
    if button_plus.draw():
        funcsave = "plus"
        currentstr = ""
    
    if button_pom.draw():
        currentnum = float(currentnum)
        currentnum = currentnum - currentnum - currentnum
        currentstr = str(currentnum)
        textsurface = fnt.render(currentstr, False, (0, 0, 0))

    
    if button_root.draw():
        if value < 0:
            currentstr = "Error"
            currentnum = 0
        else:
            value = sqrt(float(currentnum))
            currentstr = str(value)
            currentnum = value
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    
    if button_square.draw():
        funcsave = "square"
        currentstr = ""
    
    if button_zero.draw():
        if funcsave != "":
            currentstr = currentstr + "0"
            currentnum2 = currentstr
        else:        
            currentstr = currentstr + "0"
            currentnum = currentstr
        textsurface = fnt.render(currentstr, False, (0, 0, 0))

    if button_dot.draw():
        currentstr = currentstr + "."
        #currentnum = float(currentstr)
        textsurface = fnt.render(currentstr, False, (0, 0, 0))
    
    if button_x.draw():
        funcsave = "times"
        currentstr = ""

    if button_c.draw():
        currentstr = "0"
        currentnum = 0
        textsurface = fnt.render(currentstr, False, (0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if len(currentstr) > 1:
        if currentstr[0] == "0":
            currentstr = currentstr[1 : : ]
            textsurface = fnt.render(currentstr, False, (0, 0, 0))
    takeaway = len(currentstr)
    takeaway = takeaway * 27
    takeaway = 320 - takeaway
    #prfloat(takeaway)
    screen.blit(textsurface,(takeaway,90))

    pygame.display.update()