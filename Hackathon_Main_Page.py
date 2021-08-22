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

White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

Input_txt = '' 

def Positions():
    Sep = 50

    W = Width/10
    H = 2*Height/3

    W2 = 4*Width/5
    H2 = Width/25

    Pos1 = (W ,H)
    Pos2 = (W ,H + Sep)
    Pos3 = (W ,H + Sep*2)


    Pos_in_1 = (W2 ,H2)
    Pos_in_2 = (W2 ,H2 + Sep)


    Txt1 = 'I have academic issues'
    Txt1_img = Font2.render(Txt1, True , Black).convert_alpha()
    Txt1_rect = Txt1_rect = Txt1_img.get_rect(midleft = Pos1)

    Txt2 = 'I have family issues'
    Txt2_img = Font2.render(Txt2, True , Black).convert_alpha()
    Txt2_rect = Txt2_rect = Txt2_img.get_rect(midleft = Pos2)

    Txt3 = 'I have psycological issues'
    Txt3_img = Font2.render(Txt3, True , Black).convert_alpha()
    Txt3_rect = Txt3_rect = Txt3_img.get_rect(midleft = Pos3)

    Txt_in_1 = 'Enter your passcode:'
    Txt_in_1_img = Font2.render(Txt_in_1, True , Black).convert_alpha()
    Txt_in_1_rect = Txt_in_1_img.get_rect(center = Pos_in_1)

    return Txt1,Txt1_img,Txt1_rect, Txt2,Txt2_img,Txt2_rect, Txt3,Txt3_img,Txt3_rect ,Txt_in_1,Txt_in_1_img,Txt_in_1_rect, Pos_in_2

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

def Display_imgs(Txt1_img,Txt1_rect, Txt2_img,Txt2_rect, Txt3_img,Txt3_rect, Txt_in_1_img, Txt_in_1_rect, Input_txt ,Pos_in_2):

    screen.blit(Bg,(0,0))
    screen.blit(Txt1_img, Txt1_rect)
    screen.blit(Txt2_img, Txt2_rect)
    screen.blit(Txt3_img, Txt3_rect)
    screen.blit(Txt_in_1_img, Txt_in_1_rect)

    #Input Text Preview

    Txt_in_2_img = Font2.render(Input_txt, True , Black).convert_alpha()
    Txt_in_2_rect = Txt_in_2_img.get_rect(center = Pos_in_2)
    screen.blit(Txt_in_2_img, Txt_in_2_rect)

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

    Input_txt = 'Lol'

    Txt1,Txt1_img,Txt1_rect, Txt2,Txt2_img,Txt2_rect, Txt3,Txt3_img,Txt3_rect ,Txt_in_1,Txt_in_1_img,Txt_in_1_rect, Pos_in_2 = Positions()

    while True:

        for event in pygame.event.get(): # Handling user input
            
            if event.type == pygame.QUIT: # Handling User input to quit game
                Close_Window('Quit')

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:

                    Input_txt = Input_txt[0:len(Input_txt)-1]

                elif event.key in (pygame.K_KP_ENTER , pygame.K_RETURN):
                    pass

                else:
                    Input_txt += event.unicode

        Display_imgs(Txt1_img, Txt1_rect, Txt2_img, Txt2_rect, Txt3_img, Txt3_rect, Txt_in_1_img, Txt_in_1_rect, Input_txt ,Pos_in_2)

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
