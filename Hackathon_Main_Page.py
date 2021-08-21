import pygame

pygame.init()

Font2 = pygame.font.Font('Fonts\\Lilly\\Lilly__.ttf',25)

Bg = pygame.image.load().convert_alpha()

Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)


if __name__ == __main__:
    ''

Width = 960
Height = 540

screen = Load_Screen(Width,Height)

def Load_Screen(Width,Height): #Loading the window

    screen = pygame.display.set_mode((Width,Height))
    return screen

def Positions(Width):
    Sep = 20

    Pos1 = (Width/2,Height/2)
    Pos2 = (Width/2+ Sep ,Height/2 + Sep)
    Pos3 = (Width/2+ Sep*2 ,Height/2 + Sep*2)
    Pos4 = (Width/2+ Sep*3 ,Height/2 + Sep*3)
    Pos5 = (Width/2+ Sep*4 ,Height/2 + Sep*4)


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

def M_Fn(Txt_rect):
        
        if Tile_Rect.collidepoint(Mouse_Pos):
            if Click:
                    Tile_Click = 1
                    
            else:
                Tile_Click = 0
                  
        else:
            Tile_Click = 0

        return Tile_Click

def Mouse(Txt1_rect, Txt2_rect, Txt3_rect):

    Mouse_Pos = pygame.mouse.get_pos()
    Click = pygame.mouse.get_pressed()[0]

    screen.blit(Bg,(0,0))

    Click1 = M_Fn(Txt1_rect)
    Click2 = M_Fn(Txt2_rect)
    Click3 = M_Fn(Txt3_rect)

    return Click1, Click2, Click3

def Display_imgs(Txt1_img,Txt1_rect, Txt2_img,Txt2_rect, Txt3_img,Txt3_rect):

    screen.blit(Bg,(0,0))
    screen.blit(Txt1_img, Txt1_rect)
    screen.blit(Txt2_img, Txt2_rect)
    screen.blit(Txt3_img, Txt3_rect)
