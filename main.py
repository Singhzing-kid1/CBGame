import pygame
import sys

pygame.init()

SCREEN_SIZE = (500, 500)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BIG_FONT = pygame.font.Font('SedgwickAveDisplay-Regular.ttf', 40)
SMALL_FONT = pygame.font.Font('font.ttf', 20)
CLOCK = pygame.time.Clock()
bb1 = BIG_FONT.render('Prologue', True, BLUE)
b1 = bb1.get_rect(topleft=(5, 5))
bb2 = BIG_FONT.render('The Charlottetown Conference', True, BLUE)
b2 = bb2.get_rect(topleft=(5, 5))
bb3 = BIG_FONT.render('The Quebec Conference', True, BLUE)
b3 = bb3.get_rect(topleft=(5, 55))
bb4 = BIG_FONT.render('The London Conference', True, BLUE)
b4 = bb4.get_rect(topleft=(5, 105))
bbl1 = BIG_FONT.render('Prologue', True, BLACK)
bl1 = bb1.get_rect(topleft=(5, 5))
bbl2 = BIG_FONT.render('The Charlottetown Conference', True, BLACK)
bl2 = bb2.get_rect(topleft=(5, 5))
bbl3 = BIG_FONT.render('The Quebec Conference', True, BLACK)
bl3 = bb3.get_rect(topleft=(5, 5))
bbl4 = BIG_FONT.render('The London Conference', True, BLACK)
bl4 = bb4.get_rect(topleft=(5, 5))

contsign = SMALL_FONT.render("Click anywhere to continue", True, BLUE)


p = True
l1 = False
l2 = False
l3 = False
name = ""
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 20)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.returntext = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.returntext = True
                    
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

def levelselect(pl, l, ll, lll, clock, nm):
    screen = pygame.display.set_mode(SCREEN_SIZE)
    mousepos = pygame.mouse.get_pos()
    
    


    while True:
        screen.fill((214, 204, 169))
        if pl == True:
            screen.blit(bb1, b1)

        if pl == False and l == True:
            screen.blit(bb2, b2)
        if ll == True and l == False:
            screen.blit(bbl2, bl2)
            screen.blit(bb3, b3)

        if lll == True and ll == False:
            screen.blit(bbl2, b2)
            screen.blit(bbl3, b3)
            screen.blit(bb4, b4)



        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                if b3.collidepoint(e.pos):
                    name = nm
                    qc(p, l1, l2, l3, BIG_FONT, SMALL_FONT, BLACK, 500, 500, contsign, CLOCK, name)
                    print("youu say ooooooogaaaa booooooga")
                    
                if b1.collidepoint(e.pos):
                    prolg(p, l1, l2, l3, BIG_FONT, SMALL_FONT, BLACK, 500, 950, CLOCK)

                if b2.collidepoint(e.pos):
                    cc(p, l1, l2, l3, BIG_FONT, SMALL_FONT, BLACK, 500, 500, contsign, CLOCK, nm)

        pygame.display.update()
        clock.tick(30)

def prolg(pl, l, ll, lll, fnt1, fnt2, txt_col, screenx, screeny, clock):
    
    
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
                levelselect(p, l1, l2, l3, CLOCK, name)
            
        pygame.display.update()
        clock.tick(30)

def fail():
    print("HAHA YOU FAILED!!")
    pygame.quit()
    sys.exit()

def cc(pl, l, ll, lll, fnt1, fnt2, txt_col, screenx, screeny, ctc, clock, nm):
    name = nm
    q = ""
    box1 = InputBox(67, 215, 140, 22)
    box2 = InputBox(450, 450, 25, 22)
    screen = pygame.display.set_mode((screenx, screeny))
    title = fnt1.render("John A. Macdonald", True, txt_col)
    t1 = fnt2.render("He told me you would come.", True, txt_col)
    t21 = fnt2.render("The late king(RIP). He told me in a", True, txt_col)
    t22 = fnt2.render("letter.", True, txt_col)
    t31 = fnt2.render("Well... What would you like me to call", True, txt_col) 
    t32 = fnt2.render("you:", True, txt_col)
    tt41 = fnt2.render("We will be meeting with", True, txt_col) 
    tt42 = fnt2.render("George- Etienne Cartier & George", True, txt_col) 
    tt43 = fnt2.render("Brown", True, txt_col)
    tt51 = fnt2.render("Our goal is to convince the maritime", True, txt_col) 
    tt52 = fnt2.render("provinces to join the province of Canada", True, txt_col)
        
    welcome = False
    day14 = False
    day57 = False
    greet = True 

    while True:
        mousepos = pygame.mouse.get_pos()
        tt31 = fnt2.render("Well " + name + ", We are headed to the", True, txt_col)
        tt32 = fnt2.render("Charlottetown Conference.", True, txt_col)
        screen.fill((214, 204, 169))
        screen.blit(title, (5, 5))
        

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            box1.handle_event(e)
            box2.handle_event(e)

        #start name input box + extras    
            if e.type == pygame.MOUSEBUTTONDOWN:
                if day57 == True:
                    p = False
                    l1 = False
                    l2 = True
                    levelselect(p, l1, l2, l3, CLOCK, name)

                if day14 == True and box2.text == "y" or box2.text == "Y":
                    day14 = False
                    day57 = True
                elif day14 == True and box2.text == "n" or box2.text == "N":
                    fail()

                if welcome == True:
                    welcome = False
                    box1.returntext = False
                    day14 = True
        #end name input + extras
        
        if greet == True:
            screen.blit(t1, (5, 55))
            screen.blit(t21, (5, 85))
            screen.blit(t22, (5, 115))
            screen.blit(t31, (5, 145))
            screen.blit(t32, (5, 175))
            box1.update()
            box1.draw(screen)
            

        if welcome == True:
            screen.blit(tt31, (5, 55))
            screen.blit(tt32, (5, 85))
            screen.blit(tt41, (5, 115))
            screen.blit(tt42, (5, 145))
            screen.blit(tt43, (5, 175))
            screen.blit(tt51, (5, 205))
            screen.blit(tt52, (5, 235))
            screen.blit(ctc, (5, 265))
        
        if day14 == True:
            box2.draw(screen)
            
            
            screen.blit(ctc, (5, 335))

        if box1.returntext == True:
            
            name = box1.text
            box1.active = False
            greet = False
            welcome = True
            
        
               
        pygame.display.update()
        clock.tick(30)

def qc(pl, l, ll, lll, fnt1, fnt2, txt_col, screenx, screeny, ctc, clock, nm):
    welcome = True
    week1 = False
    week2 = False
    Q = InputBox(450, 450, 25, 22)
    num = 0
    title = fnt1.render("John A. Macdonald", True, txt_col)
    screen = pygame.display.set_mode((screenx, screeny))
    while True:
        screen.fill((214, 204, 169))
        screen.blit(title, (5, 5))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if week2 == True:
                    p = False
                    l1 = False
                    l2 = False
                    l3 = True
                    name = nm
                    levelselect(p, l1, l2, l3, CLOCK, name)

                if week1 == True and Q.text == "y" or Q.text == "Y":
                    week1 = False
                    week2 = True

                if week1 == True and Q.text == "n" or Q.text == "Y":
                    fail()

                if welcome == True:
                    welcome = False
                    week1 = True

            Q.handle_event(e)
        
        if welcome == True:
            screen.blit(ctc, (5, 55))

        if week1 == True:
            screen.blit(ctc, (100, 100))
            Q.draw(screen)

        if week2 == True:
            screen.blit(ctc, (15, 155))

        pygame.display.update()
        clock.tick(30)

        





levelselect(p, l1, l2, l3, CLOCK, name)