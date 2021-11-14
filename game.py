import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 500,300
pygame.display.set_caption("TAP TAP FAST")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
start_pos_red = 0
start_pos_blue = WIDTH//2
red_rect = pygame.Rect(0, 0, WIDTH//2, HEIGHT)
blue_rect= pygame.Rect(WIDTH//2, 0, WIDTH//2, HEIGHT)
game = False
whowin = "no one"
mainscreen = True
def display_text(pos_x, pos_y, text, font, size, color):
    _text = pygame.font.Font(font, size)
    text_surf = _text.render(text, True, color)
    text_rect = text_surf.get_rect(center= (pos_x, pos_y))
    screen.blit(text_surf, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game==False:
            if event.key == pygame.K_SPACE:
                game = True
                red_rect.width = WIDTH//2
                blue_rect.width = WIDTH//2
                red_rect.left = 0
                blue_rect.left = WIDTH//2
    if game:
        screen.fill((91,91,91))
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            red_rect.width+=5 #increasing red 
            blue_rect.left+=5 #decreasing blue
        if key[pygame.K_UP]:
            blue_rect.width+=5 #increasing blue
            blue_rect.left -=5 # decreasing blue position 
            red_rect.left-=5 # decreasing red
        if red_rect.right >= WIDTH:
            game=False
            mainscreen = False
            whowin = "RED"
        if blue_rect.left<=0:
            game=False
            mainscreen = False
            whowin = "BLUE"
            red_rect.x = 0
            blue_rect.x = WIDTH//2
        pygame.draw.rect(screen, (255,0,0), red_rect)
        pygame.draw.rect(screen, (0,0,255), blue_rect)
        display_text(100,60, "RED", "fonts\\font.ttf", 30, (0,0,0))
        display_text(400,60, "BLUE", "fonts\\font.ttf", 30, (0,0,0))
    else:
        screen.fill((51,51,51))
        if mainscreen:
            display_text(WIDTH//2, 80, "TAP TAP FAST", "fonts\\font.ttf", 45, (255,255,255))
            display_text(WIDTH//2, HEIGHT//2, "PRESS SPACE KEY TO START", "fonts\\font.ttf", 40, (255,255,255))
        else:
            display_text(WIDTH//2, 100, "GAME OVER", "fonts\\font.ttf", 40, (255,255,255))
            display_text(WIDTH//2, HEIGHT//2, f"{whowin}  Win", "fonts\\font.ttf", 50, (255,255,255))
            display_text(WIDTH//2, HEIGHT//2+50, "PRESS SPACE TO RESTART", "fonts\\font.ttf", 40, (255,255,255))
    pygame.display.update()
    clock.tick(60)
