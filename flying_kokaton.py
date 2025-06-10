import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    koukaton3_img = pg.image.load("fig/3.png")
    koukaton3_img = pg.transform.flip(koukaton3_img, True, False)
    koukaton3_rct = koukaton3_img.get_rect()
    koukaton3_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        
        key_lst = pg.key.get_pressed()

        x = -2
        y = 0

        if key_lst[pg.K_UP]:
            x = 0
            y = -2  
              
        if key_lst[pg.K_DOWN]:
            x = 0
            y = +2
            
        if key_lst[pg.K_LEFT]:
            x = -2
            y = 0
            
        if key_lst[pg.K_RIGHT]:
            x = +5
            y = 0
            
        
        koukaton3_rct.move_ip(x, y)
        

        

        x = tmr
        x = tmr%3200
        
        screen.blit(bg_img, [-x, 0])  # 1枚目
        screen.blit(bg_img2, [-x+1600, 0])  # 2枚目
        screen.blit(bg_img, [-x+3200, 0])  # 3枚目

        

        screen.blit(koukaton3_img, koukaton3_rct)
        #koukaton3_rct = koukaton3_img.get_rect()
        #koukaton3_rct.center = 300, 200
        

        pg.display.update()
        
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()