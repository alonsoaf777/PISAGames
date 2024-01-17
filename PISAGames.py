import pygame, math, time
import random
from pygame.locals import *
import sys
import os

mainClock = pygame.time.Clock()
#INVASION DE MULTIPLOS: fuente del multiplo score
SCREEN_WIDHT = 760
SCREEN_HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('PISA Games')
control = 0
global t 
#--------------------------------------------------- Paths
main_Path = os.path.dirname(os.path.abspath(__file__))
path_sonidos = os.path.join(main_Path, 'Assets' , 'Sonidos')
path_imagenes = os.path.join(main_Path, 'Assets', 'Imagenes')

#--------------------------------------------------- FUENTES
font = pygame.font.SysFont('comicsans', 30, True)
fontM = pygame.font.SysFont('comicsans', 40, True)
fontS = pygame.font.SysFont('comicsans', 23, True)
#--------------------------------------------SONIDOS
winf = pygame.mixer.Sound(path_sonidos + '\Win.wav')
losef = pygame.mixer.Sound(path_sonidos + '\Fail.wav')
correctf = pygame.mixer.Sound(path_sonidos + '\Correct.wav')
incorrectf = pygame.mixer.Sound(path_sonidos + '\Incorrect.wav')
disparo = pygame.mixer.Sound(path_sonidos + '\disparo.wav')
explosion = pygame.mixer.Sound(path_sonidos + '\explosion.wav')
naveColision = pygame.mixer.Sound(path_sonidos + '\\naveColision.wav')
naveDestroy = pygame.mixer.Sound(path_sonidos + '\\naveDestroy.wav')
medioLost = pygame.mixer.Sound(path_sonidos + '\medioLost.wav')
medioWinn = pygame.mixer.Sound(path_sonidos + '\medioWin.wav')
#----------------------------------------------------
FiguraRan = random.randint(0,3)
multiplo = random.choice([2, 3, 5])
print(multiplo)
avance4 = pygame.image.load(path_imagenes + '\FondoAvance4.jpg').convert()
indicador = pygame.image.load(path_imagenes + '\indicador.png').convert_alpha()
multiplo2 = pygame.image.load(path_imagenes + '\multiplos2.png').convert_alpha()
multiplo3 = pygame.image.load(path_imagenes + '\multiplos3.png').convert_alpha()
multiplo5 = pygame.image.load(path_imagenes + '\multiplos5.png').convert_alpha()
lados_3 = pygame.image.load(path_imagenes + '\lados_3.png').convert_alpha()
lados_4 = pygame.image.load(path_imagenes + '\lados_4.png').convert_alpha()
lados_0 = pygame.image.load(path_imagenes + '\lados_0.png').convert_alpha()
lados_5 = pygame.image.load(path_imagenes + '\pentagonoA.png').convert_alpha()
reintentar = pygame.image.load(path_imagenes + '\\reintentar.png').convert_alpha()
#------------------------------------------------------------CLASES FACIL
class player(object):
    fondoD_Facil = pygame.image.load(path_imagenes + '\FondoDFACIL.jpg').convert()
    mistake = pygame.image.load(path_imagenes + '\mistake.png').convert_alpha()
    cubeta = pygame.image.load(path_imagenes + '\cubeta.png').convert_alpha()
    avance1 = pygame.image.load(path_imagenes + '\FondoAvance1.jpg').convert()
    avance2 = pygame.image.load(path_imagenes + '\FondoAvance2.jpg').convert()
    avance3 = pygame.image.load(path_imagenes + '\FondoAvance3.jpg').convert()
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.score = 0
        self.lost = 0
        self.hitbox = (self.x , self.y, 85, 80)
    def draw(self, screen):
        screen.blit(self.fondoD_Facil, (0,0))                
#----------------------------------------------SCORE       
        if self.score >= 5:
            screen.blit(self.avance1, (0,0))
        if self.score >= 10: 
            screen.blit(self.avance2, (0,0))    
        if self.score >= 15:
            screen.blit(self.avance3, (0,0))
        if self.score == 20:
            winf.play()
            postFacil()
#--------------------------------------------------PLATAFORMA
        pygame.draw.rect(screen, (0, 0, 0),(0, 540, 760, 60))
#----------------------------------------------PERDER  
        if self.lost >= 1:
            screen.blit(self.mistake, (660,530))
        if self.lost >= 2:
            screen.blit(self.mistake, (680,530))   
        if self.lost >= 3:
            screen.blit(self.mistake, (700,530))
        if self.lost >= 4:
            screen.blit(self.mistake, (640,530))
        if self.lost >= 5:
            losef.play()
            lostFacil()
#-----------------------------------------------------DIBUJAR
        self.hitbox = (self.x , self.y, 85, 80)
        text = font.render('Score: ' + str(self.score), 1, (255,255,255))
        screen.blit(text, (10, 545))
        screen.blit(self.cubeta, (self.x, self.y))   
class figura(object):
    figurasDraw = [pygame.image.load(path_imagenes + '\cuadrado.jpg'), pygame.image.load(path_imagenes + '\\triangulo.png'), pygame.image.load(path_imagenes + '\circulo.png'), pygame.image.load(path_imagenes + '\pentagono.png')]
    def __init__(self, x, y, vel, width, height, tipo):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 40, 40)
        self.tipo = tipo
    def draw(self, screen):
        self.hitbox = (self.x, self.y, 40, 40)
        self.y +=  self.vel
        screen.blit(self.figurasDraw[self.tipo], (self.x, self.y, 40, 40))     
#-------------------------------------------------------------------------------CLASES DIFICULTAD MEDIA
class player2(object):
    fondoMedio = pygame.image.load(path_imagenes + '\FondoMedio.jpg').convert()
    vida = pygame.image.load(path_imagenes + '\\vida.png').convert_alpha()
    def __init__(self, x, y, width, height, life):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12
        self.hitbox = (self.x, self.y)
        self.score = 0
        self.lost = 0
        self.life = life
    def draw(self, screen):
        screen.blit(self.fondoMedio, (0,0))
        text = font.render('Score: ' + str(self.score), 1, (255,255,255))
        screen.blit(text, (10, 545))
        n = 0
        for l in range(10,1,-1):
            if self.life < l: #####10 de vida y blit a distintas posiciones
                screen.blit(self.vida,(10+n,545))
                n += 50
        self.hitbox = (self.x, self.y)
        if self.score >= 15:
            medioWinn.play()
            medioWin() 
    def hit(self): 
        print('Colision')
        self.life -= 1
        naveColision.play()
        if self.life <= 0:
            naveDestroy.play()
            medioLost.play()
            lostMedio()
class meteoro(object):
    meteorosDraw = [pygame.image.load(path_imagenes + '\meteoroS.png'), pygame.image.load(path_imagenes + '\meteoroM.png'), pygame.image.load(path_imagenes + '\meteoroG.png')]
    meteorosHit = [pygame.image.load(path_imagenes + '\meteoroShit.png'), pygame.image.load(path_imagenes + '\meteoroMhit.png'), pygame.image.load(path_imagenes + '\meteoroGhit.png')]
    def __init__(self, x, y, vel, width, height, radio, num, tipo): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.radio = radio
        self.num = num
        self.life = num//multiplo
        self.hitbox = (self.x, self.y + self.height, self.width, self.height)
        self.tipo = tipo
    def draw(self, screen):
        screen.blit(self.meteorosDraw[self.tipo], (self.x, self.y))
        self.hitbox = (self.x, self.y + self.height, self.width, self.height)
        self.y += + self.vel
        text = font.render(str(self.num), 1, (0,0,0))
        screen.blit(text, (self.x+(self.width-text.get_width())/2, self.y + self.height+(self.height-text.get_height())/2))
    def hit(self):
        print('hit')
        self.life -= 1
        screen.blit(self.meteorosHit[self.tipo], (self.x, self.y)) 
class projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 18
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
#---------------------------------------------------------------------------------- PANTALLAS, JUEGO EN LINEA 292
def main():
    fondo = pygame.image.load(path_imagenes + "\PosibleMenu2.jpg").convert()
    jugar_button = pygame.image.load(path_imagenes + "\Jugar.png").convert_alpha()
    opciones_button = pygame.image.load(path_imagenes + "\Opciones.png").convert_alpha()
    esc_salir = pygame.image.load(path_imagenes + "\Esc1.png").convert_alpha()
    button_1 = pygame.Rect(250, 250, 250, 90)
    button_2 = pygame.Rect(250, 365, 250, 90)
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(fondo, (0, 0))
        if button_1.collidepoint((mx, my)):
            screen.blit(indicador, (245, 270))
            if click:
                juego()
        if button_2.collidepoint((mx, my)):
            screen.blit(indicador, (205, 382))
            if click:
                opciones()
        screen.blit(jugar_button, (250, 250))
        screen.blit(opciones_button, (250, 365))
        screen.blit(esc_salir, (10, 500))
        pygame.display.flip()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:    
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def juego():
    fondo_juego = pygame.image.load(path_imagenes + '\JuegoFondo.jpg').convert()
    sequia = pygame.image.load(path_imagenes + '\sequia.png').convert_alpha()
    invasion = pygame.image.load(path_imagenes + '\invasion.png').convert_alpha()
    esc_volver = pygame.image.load(path_imagenes + "\Esc2.png").convert_alpha()
    button_3 = pygame.Rect(220, 150, 300, 90)
    button_4 = pygame.Rect(170, 300, 400, 150)
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.blit(fondo_juego, (0, 0))
        if button_3.collidepoint((mx, my)):
            screen.blit(indicador, (215, 175))
            if click:
                loreFacil()
        if button_4.collidepoint((mx, my)):
            screen.blit(indicador, (140, 350))
            if click:
                loreMedio()
        screen.blit(sequia, (220, 150))
        screen.blit(invasion, (170, 300))
        screen.blit(esc_volver, (10, 500))
        pygame.display.flip()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:    
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def opciones():
    fondo_juego = pygame.image.load(path_imagenes + '\OpcionesFondo.jpg').convert()
    esc_volver = pygame.image.load(path_imagenes + "\Esc2.png").convert_alpha()
    asdw = pygame.image.load(path_imagenes + "\\asdw.png").convert_alpha()
    flechitas = pygame.image.load(path_imagenes + "\\flechitas.png").convert_alpha()
    button_1 = pygame.Rect(100, 300, 228, 145)
    button_2 = pygame.Rect(400, 300, 228, 145)
    click = False
    running = True
    while running:
        screen.blit(fondo_juego, (0, 0))
        mx, my = pygame.mouse.get_pos()
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 255),(100, 300, 228, 145),2)
            if click:
                global control
                control = 0
                print(control)
        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 255),(400, 300, 228, 145),2)
            if click:
                control = 1
                print(control)
        screen.blit(asdw, (100, 300))
        screen.blit(flechitas, (400, 300))
        screen.blit(esc_volver, (10, 500))
        pygame.display.flip()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:    
                    click = True
        pygame.display.update()
        mainClock.tick(60)
#------------------------------------------------------------------------- DIFICULTAD FACIL        
def d_facil():
    radio = 52.5
    man = player(300, 460, 85, 80)
    cuadrado = figura(random.randint(0,720), 0, 1.2, 40, 40, 0)
    triangulo = figura(random.randint(0,720), 0, .8, 40, 40, 1)
    circulo = figura(random.randint(0,720), 0, 1, 40, 40, 2)
    pentagono = figura(random.randint(0,720), 0, 1.4, 40, 40, 3)
    figuras = [circulo, cuadrado, triangulo, pentagono]
    running = True
    while running:
        man.draw(screen)
        for forma in figuras:
            forma.draw(screen)
        for i in range(0,4):
            if radio >= math.sqrt(pow((man.x + 42.5)-(figuras[i].x + 20),2) + pow((man.y + 40)-(figuras[i].y + 20),2)):
                figuras[i].y = 0
                figuras[i].x = random.randint(0, 720)
                figuras[i].vel += 1/2
                if figuras[i] == figuras[FiguraRan]:
                    man.score += 1
                    correctf.play()
                else:
                    man.lost += 1
                    incorrectf.play()
            if figuras[i].y >= SCREEN_HEIGHT:
                figuras[i].y = 0
                figuras[i].x = random.randint(0, 720)
                figuras[i].vel += 1/2
                if figuras[i] == figuras[FiguraRan]:
                    man.lost += 1
                    incorrectf.play()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        keys = pygame.key.get_pressed() 
        if control == 1:
            if keys[pygame.K_LEFT] and man.x > man.vel:
                man.x -= man.vel
            if keys[pygame.K_RIGHT] and man.x < 760 - man.width - man.vel:
                man.x += man.vel
        if control == 0:
            if keys[pygame.K_a] and man.x > man.vel:
                man.x -= man.vel
            if keys[pygame.K_d] and man.x < 760 - man.width - man.vel:
                man.x += man.vel
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)
def preFacil():
    presioneEspacio = pygame.image.load(path_imagenes + '\ESPACIO.png').convert_alpha()
    running = True
    while running:
        screen.fill((150,200,230))
        screen.blit(presioneEspacio, (70, 400))
        randomw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    loreFacil()
                if event.key == K_SPACE:
                    d_facil()
        pygame.display.update()
        mainClock.tick(60)
def postFacil():
    VolverJugar = pygame.image.load(path_imagenes + '\VolverJugar.png').convert_alpha()
    Felicidades = pygame.image.load(path_imagenes + '\Felicidades.jpg').convert_alpha()
    button_1 = pygame.Rect(170, 350, 400, 90)
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.blit(avance4, (0,0))
        screen.blit(Felicidades, (0, 0))
        if button_1.collidepoint((mx, my)):
            screen.blit(indicador, (158, 380))
            if click:
                preFacil()
        screen.blit(VolverJugar, (170, 350))
        pygame.display.flip()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:    
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def lostFacil():
    lostFacil = pygame.image.load(path_imagenes + '\lostFacil.jpg').convert()
    button_1 = pygame.Rect(190, 370, 400, 90)
    click = False
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.blit(lostFacil, (0, 0))
        if button_1.collidepoint((mx, my)):
            screen.blit(indicador, (180, 390)) 
            if click:
                preFacil()   
        screen.blit(reintentar, (190, 370))
        pygame.display.flip()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:    
                    click = True
        pygame.display.update()
        mainClock.tick(60)  
def loreFacil():
    lore = pygame.image.load(path_imagenes + '\loreFacil.jpg').convert()
    presioneEspacio = pygame.image.load(path_imagenes + '\ESPACIO.png').convert_alpha()
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(lore, (0, 0))
        screen.blit(presioneEspacio, (70, 450))
        pygame.display.flip()    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    juego()
                if event.key == K_SPACE:
                    preFacil()
        pygame.display.update()
        mainClock.tick(60)
def randomw():
    if FiguraRan == 2:
        screen.blit(lados_3, (70, 50))
    if FiguraRan == 1:
        screen.blit(lados_4, (55, 50))
    if FiguraRan == 0:
        screen.blit(lados_0, (40, 50))
    if FiguraRan == 3:
        screen.blit(lados_5, (40, 50))
 #------------------------------------------------------------------------------- INVASION DE MULTIPLOS      
def d_medio():
    naveDina = pygame.image.load(path_imagenes + '\\NaveDina.png').convert_alpha()
    naveNODina = pygame.image.load(path_imagenes + '\\NaveNODina.png').convert_alpha()
    naveDis = pygame.image.load(path_imagenes + '\\NaveDis.png').convert_alpha()
    nave = player2(300, 460, 100, 100, 10)
    meteoroS = meteoro(random.randint(50, 710), -80, 2, 50, 40, 28, random.randint(1,50), 0)
    meteoroM = meteoro(random.randint(0, 660), -180, 2, 100, 90, 53, random.randint(1,50), 1) 
    meteoroG = meteoro(random.randint(0, 560), -280, 2, 170, 140, 78, random.randint(1,50),2)
    meteoros = [meteoroS, meteoroM, meteoroG]
    t = time.time()
    bullets = []
    running = True
    while running:
        nave.draw(screen)
        for meteorito in meteoros:
            meteorito.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for meteorito in meteoros:
        ######################################################VIDA
            if meteorito.num%multiplo == 0:
                if meteorito.life <= 0:
                    meteorito.x = random.randint(meteorito.width/2, 760-meteorito.width)
                    meteorito.y = meteorito.height*-2
                    meteorito.num = random.randint(1, 50)
                    explosion.play()
                    meteorito.life = meteorito.num//multiplo
                    nave.score += 1
                    print(nave.score)
                if meteorito.y > SCREEN_HEIGHT:
                    meteorito.x = random.randint(meteorito.width/2, 760-meteorito.width)  
                    meteorito.y = meteorito.height * -2
                    meteorito.num = random.randint(1,50)
                    meteorito.life = meteorito.num//multiplo
                    nave.hit()
            if meteorito.num%multiplo != 0:
                if meteorito.life <= 0:
                    meteorito.x = random.randint(meteorito.width/2, 760-meteorito.width)
                    meteorito.y = meteorito.height*-2
                    meteorito.num = random.randint(1, 50)
                    explosion.play()
                    meteorito.life = meteorito.num//multiplo
                    nave.hit()
                if meteorito.y > SCREEN_HEIGHT:
                    meteorito.x = random.randint(meteorito.width/2, 760-meteorito.width)  
                    meteorito.y = meteorito.height * -2
                    meteorito.num = random.randint(1,50)
                    meteorito.life = meteorito.num//multiplo
        #----------------------------------------- PROJECTILES EN LA PANTALLA
        for bullet in bullets:
            for meteorito in meteoros:
                if math.sqrt(pow((meteorito.x + (meteorito.width/2))-(bullet.x + bullet.radius),2) + pow((meteorito.y + (meteorito.height*2))-(bullet.y + bullet.radius),2)) < meteorito.radio:
                    meteorito.hit()
                    print('VIDA', meteorito.life)
                    if bullet in bullets:
                        bullets.remove(bullet)
                elif bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                    bullet.y -= bullet.vel
                else:
                    if bullet in bullets:
                        bullets.remove(bullet)
        #Hitbox de la nave
        for meteorito in meteoros:
            if math.sqrt(pow((meteorito.x + (meteorito.width/2))-(nave.x + 50),2) + pow((meteorito.y + (meteorito.height*2))-(nave.y + 50),2)) <= meteorito.radio + 20:
                if time.time() > t + 1:
                    nave.hit()
                    t = time.time()
        keys = pygame.key.get_pressed()
        #------------------------------------------------- PROJECTILES
        if keys[pygame.K_SPACE]:
            #-------------------------------------- NUMERO DE PROJECTILES EN PANTALLA
            if time.time() > t + .1:
                disparo.play()
                #---------------------------CARACTERISTICAS DE LA BALA
                bullets.append(projectile(round(nave.x + nave.width // 2), round(nave.y + nave.height // 2), 8, (255,0,0)))
                screen.blit(naveDis, (nave.x, nave.y))
                t = time.time()
        if control == 1:
            if keys[pygame.K_LEFT] and nave.x > nave.vel:
                nave.x -= nave.vel
                screen.blit(naveDina, (nave.x, nave.y))
            if keys[pygame.K_RIGHT] and nave.x < 760 - nave.width - nave.vel:
                nave.x += nave.vel
                screen.blit(naveDina, (nave.x, nave.y))
            if keys[pygame.K_UP] and nave.y > nave.vel:
                nave.y -= nave.vel
                screen.blit(naveDina, (nave.x, nave.y))
            if keys[pygame.K_DOWN] and nave.y < 600 - nave.height - nave.vel:
                nave.y+= nave.vel
                screen.blit(naveDina, (nave.x, nave.y))
        if control == 0:
            if keys[pygame.K_a] and nave.x > nave.vel:
                nave.x -= nave.vel
                screen.blit(naveDina, (nave.x, nave.y))
            if keys[pygame.K_d] and nave.x < 760 - nave.width - nave.vel:
                nave.x += nave.vel
                screen.blit(naveDina, (nave.x, nave.y))
            if keys[pygame.K_w] and nave.y > nave.vel:
                nave.y -= nave.vel
                screen.blit(naveDina, (nave.x, nave.y))
            if keys[pygame.K_s] and nave.y < 600 - nave.height - nave.vel:
                nave.y += nave.vel
                screen.blit(naveDina, (nave.x, nave.y))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        screen.blit(naveNODina, (nave.x, nave.y))
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)
def preMedio():
    fondoMedio = pygame.image.load(path_imagenes + '\FondoMedio.jpg').convert()
    presioneK = pygame.image.load(path_imagenes + '\presioneK.png').convert_alpha()
    running = True
    while running:
        screen.blit(fondoMedio, (0,0))
        screen.blit(presioneK, (70, 450))
        randomM() 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    loreMedio()
                if event.key == K_k:
                    d_medio()
        pygame.display.update()
        mainClock.tick(60)
def loreMedio():
    loreMedio = pygame.image.load(path_imagenes + '\loreMedio.jpg').convert()
    presioneK = pygame.image.load(path_imagenes + '\presioneK.png').convert_alpha()
    running = True
    while running:
        screen.blit(loreMedio, (0,0))
        screen.blit(presioneK, (70, 450))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    juego()
                if event.key == K_k:
                    preMedio()
        pygame.display.update()
        mainClock.tick(60)
def lostMedio(): 
    lostMedio = pygame.image.load(path_imagenes + '\lostMedio.jpg').convert()
    button_1 = pygame.Rect(190, 370, 400, 90)
    running = True
    click = False
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.blit(lostMedio, (0,0))
        screen.blit(reintentar, (190, 370))
        if button_1.collidepoint((mx, my)):
            screen.blit(indicador, (180, 390)) 
            if click:
                preMedio()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:    
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def medioWin():
    medioWin = pygame.image.load(path_imagenes + '\medioWin.jpg').convert()
    nuevoAtaque = pygame.image.load(path_imagenes + '\\nuevoAtaque.png').convert_alpha()
    button_1 = pygame.Rect(190, 370, 400, 90)
    running = True
    click = False
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.blit(medioWin, (0,0))
        screen.blit(nuevoAtaque, (195, 340))
        if button_1.collidepoint((mx, my)):
            screen.blit(indicador, (180, 390)) 
            if click:
                preMedio()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:    
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def randomM():
    if multiplo == 2:
        screen.blit(multiplo2, (40, 50))
    if multiplo == 3:
        screen.blit(multiplo3, (40, 50))
    if multiplo == 5:
        screen.blit(multiplo5, (40, 50))     
main()