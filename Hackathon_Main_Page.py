import pygame
import sys

pygame.init()

Width = 960
Height = 540

def Load_Screen(Width,Height): #Loading the window

    screen = pygame.display.set_mode((Width,Height))
    return screen

screen = Load_Screen(Width,Height)

Font2 = pygame.font.Font('Assets\\Lilly\\Lilly__.ttf',25)

Bg = pygame.transform.scale(pygame.image.load('Assets\\Bg1.jpg').convert_alpha(),(Width,Height))

Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

def Positions():
    Sep = 50

    W = Width/10
    H = 2*Height/3

    Pos1 = (W ,H)
    Pos2 = (W ,H + Sep)
    Pos3 = (W ,H + Sep*2)
    Pos4 = (W ,H + Sep*3)
    Pos5 = (W ,H + Sep*4)


    Txt1 = 'I have academic issues'
    Txt1_img = Font2.render(Txt1, True , Black).convert_alpha()
    Txt1_rect = Txt1_rect = Txt1_img.get_rect(midleft = Pos1)

    Txt2 = 'I have family issues'
    Txt2_img = Font2.render(Txt2, True , Black).convert_alpha()
    Txt2_rect = Txt2_rect = Txt2_img.get_rect(midleft = Pos2)

    Txt3 = 'I have psycological issues'
    Txt3_img = Font2.render(Txt3, True , Black).convert_alpha()
    Txt3_rect = Txt3_rect = Txt3_img.get_rect(midleft = Pos3)

    return Txt1,Txt1_img,Txt1_rect, Txt2,Txt2_img,Txt2_rect, Txt3,Txt3_img,Txt3_rect

def M_Fn(Txt_rect,Mouse_Pos,Click):
        
        if Txt_rect.collidepoint(Mouse_Pos):
            if Click:
                    Txt_Click = 1
                    
            else:
                Txt_Click = 0
                  
        else:
            Txt_Click = 0

        return Txt_Click

def Mouse(Txt1_rect, Txt2_rect, Txt3_rect):

    Mouse_Pos = pygame.mouse.get_pos()
    Click = pygame.mouse.get_pressed()[0]

    Click1 = M_Fn(Txt1_rect,Mouse_Pos,Click)
    Click2 = M_Fn(Txt2_rect,Mouse_Pos,Click)
    Click3 = M_Fn(Txt3_rect,Mouse_Pos,Click)

    return Click1, Click2, Click3

def Display_imgs(Txt1_img,Txt1_rect, Txt2_img,Txt2_rect, Txt3_img,Txt3_rect):

    screen.blit(Bg,(0,0))
    screen.blit(Txt1_img, Txt1_rect)
    screen.blit(Txt2_img, Txt2_rect)
    screen.blit(Txt3_img, Txt3_rect)

def Check1(Click1,Txt1, Click2,Txt2, Click3,Txt3):

    if Click1:
        return Txt1
        
    elif Click2:
        return Txt2

    elif Click3:
        return Txt3

    else:
        return 'No Value returned'

def Close_Window(Q):
    pygame.quit()
    if Q == 'Quit':
        sys.exit() #Safely exits the code

def Main():

    Txt1,Txt1_img,Txt1_rect, Txt2,Txt2_img,Txt2_rect, Txt3,Txt3_img,Txt3_rect = Positions()

    while True:
        for event in pygame.event.get(): # Handling user input
            
            if event.type == pygame.QUIT: # Handling User input to quit game
                Close_Window('Quit')

        Display_imgs(Txt1_img, Txt1_rect, Txt2_img, Txt2_rect, Txt3_img, Txt3_rect)

        Click1, Click2, Click3 = Mouse(Txt1_rect, Txt2_rect, Txt3_rect)

        Check_Str = Check1(Click1, Txt1, Click2, Txt2, Click3, Txt3)

        pygame.display.update() # refreshes the contents of the screen

        pygame.time.Clock().tick(60)

        if Check_Str != 'No Value returned':
            Pass_on_message = Check_Str
            Close_Window('')
            return Pass_on_message


if __name__ == '__main__':
    print(Main())