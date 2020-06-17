import pygame
import sys

pygame.init()

SCREEN_SIZE = (500, 500)
BLACK = (0, 0, 0)
BIG_FONT = pygame.font.Font('SedgwickAveDisplay-Regular.ttf', 40)
SMALL_FONT = pygame.font.Font('SedgwickAve-Regular.ttf', 30)
bb1 = BIG_FONT.render('Prologue', True, BLACK)
b1 = bb1.get_rect(topleft=(5, 5))
bb2 = BIG_FONT.render('Charlottetown Conference', True, BLACK)
b2 = bb2.get_rect(topleft=(5, 5))
bb3 = BIG_FONT.render('The Quebec Conference', True, BLACK)
b3 = bb3.get_rect(topleft=(5, 5))
bb4 = BIG_FONT.render('The London Conference', True, BLACK)
b4 = bb4.get_rect(topleft=(5, 5))
contsign = SMALL_FONT.render('Click to Continue', True, BLACK)
p = True
prit = False
l1 = False
l2 = False
l3 = False

def levelselect(pl, l, ll, lll):
    screen = pygame.display.set_mode(SCREEN_SIZE)
    mousepos = pygame.mouse.get_pos()
    


    while True:
        screen.fill((214, 204, 169))
        if pl == True:
            screen.blit(bb1, b1)

        if pl == False and l == True:
            screen.blit(bb2, b2)
        if ll == True:
            pass



        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(e.pos):
                    prolg(p, l1, l2, l3, BIG_FONT, SMALL_FONT, BLACK, 500, 950)

                if b2.collidepoint(e.pos):
                    cc(p, l1, l2, l3, BIG_FONT, SMALL_FONT, BLACK, 500, 500)


            





        pygame.display.update()

def prolg(pl, l, ll, lll, fnt1, fnt2, txt_col, screenx, screeny):
    
    
    title = fnt1.render('The King of Britain', True, txt_col)
    tt11 = fnt2.render("I'm glad to say I have won the seven", True, txt_col)
    tt12 = fnt2.render("years war!", True, txt_col)
    tt21 = fnt2.render("It was long and hard, but I did. I'm in", True, txt_col) 
    tt22 = fnt2.render("debt now and I’m taxing my british", True, txt_col)
    tt23 = fnt2.render("colonies in north america.", True, txt_col)
    tt31 = fnt2.render("After the seven years war, I put some", True, txt_col)
    tt32 = fnt2.render("acts and proclamations in place.", True, txt_col)
    tt41 = fnt2.render("First the ‘Royal Proclamation’. I gave", True, txt_col)
    tt42 = fnt2.render("the First Nations all the land west of", True, txt_col)
    tt43 = fnt2.render("Quebec's border.", True, txt_col)
    tt51 = fnt2.render("Then later, when the french got", True, txt_col)
    tt52 = fnt2.render("grumpy (at me), they started saying", True, txt_col)
    tt53 = fnt2.render("things like: non non roi George", True, txt_col)
    tt54 = fnt2.render("troisième", True, txt_col)
    tt61 = fnt2.render("So I enacted the Quebec Act, which", True, txt_col) 
    tt62 = fnt2.render("gave the french their culture and", True, txt_col)
    tt63 = fnt2.render("language back. Then they were happy", True, txt_col)
    tt64 = fnt2.render("and started saying things like: oui oui", True, txt_col) 
    tt65 = fnt2.render("roi George troisième.", True, txt_col)
    tt71 = fnt2.render("Now I'm going to hand it off to John A.", True, txt_col) 
    tt72 = fnt2.render("Macdonald to tell you about the making", True, txt_col) 
    tt73 = fnt2.render("of Canada.", True, txt_col)
    screen = pygame.display.set_mode((screenx, screeny))


    while True:
        screen.fill((214, 204, 169))
        screen.blit(title, (5, 5))

      
        
        screen.blit(tt11, (5, 55))
        screen.blit(tt12, (5, 95))

        screen.blit(tt21, (5, 135))
        screen.blit(tt22, (5, 175))
        screen.blit(tt23, (5, 215))

        screen.blit(tt31, (5, 255))
        screen.blit(tt32, (5, 295))

        screen.blit(tt41, (5, 335))
        screen.blit(tt42, (5, 375))
        screen.blit(tt43, (5, 415))

        screen.blit(tt51, (5, 455))
        screen.blit(tt52, (5, 495))
        screen.blit(tt53, (5, 535))
        screen.blit(tt54, (5, 575))
        
        screen.blit(tt61, (5, 615))
        screen.blit(tt62, (5, 655))
        screen.blit(tt63, (5, 695))
        screen.blit(tt64, (5, 735))
        screen.blit(tt65, (5, 775))
        
        screen.blit(tt71, (5, 815))
        screen.blit(tt72, (5, 855))
        screen.blit(tt73, (5, 895))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                p = False
                l1 = True
                levelselect(p, l1, l2, l3)
            
                    
            
                
            
            
            
            
            



        pygame.display.update()


def cc(pl, l, ll, lll, fnt1, fnt2, txt_col, screenx, screeny):
    screen = pygame.display.set_mode((screenx, screeny))
    title = fnt1.render("John A. Macdonald", True, txt_col)
    t1 = fnt2.render("He told me you would come.", True, txt_col)
    t21 = fnt2.render("The late king(RIP). He told me in a", True, txt_col)
    t22 = fnt2.render("letter.", True, txt_col)
    t31 = fnt2.render("Well... What would you like me to call", True, txt_col) 
    t32 = fnt2.render("you:", True, txt_col)
    font = pygame.font.Font(None, 30)
    name = ""
    text = ""
    input_box = pygame.Rect(67, 226, 140, 32)

    prit = False
    
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    greet = True
    active = False
    nameshow = False 


    while True:
        mousepos = pygame.mouse.get_pos()
        screen.fill((214, 204, 169))
        screen.blit(title, (5, 5))
        name = ""

        if greet == True:
            screen.blit(t1, (5, 55))
            screen.blit(t21, (5, 95))
            screen.blit(t22, (5, 135))
            screen.blit(t31, (5, 175))
            screen.blit(t32, (5, 215))
        if prit == True:
            print(name)

        

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(e.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if e.type == pygame.KEYDOWN:
                if active:
                    if e.key == pygame.K_RETURN:

                        nameshow = True
                        
                        
                    elif e.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += e.unicode

        if nameshow == True:
            
            name = text
            
               
            

        txt_surface = font.render(text, True, txt_col)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pygame.draw.rect(screen, color, input_box, 2)
        
        pygame.display.update()



levelselect(p, l1, l2, l3)

























