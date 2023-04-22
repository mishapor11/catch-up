from pygame import *

window = display.set_mode((1280, 800))
display.set_caption('Догонялки')  

background = transform.scale(
    image.load('background.png'),
    (1280,800)
) 

sprite1 = transform.scale(image.load('sprite1.png'), (100,100))
sprite2 = transform.scale(image.load('sprite2.png'), (100,100))

x1 = 90
y1 = 240
x2 = 340
y2 = 240


clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_UP] and y1 > 0:
        y1 -= 20

    
    if keys_pressed[K_DOWN] and y1 < 700:
        y1 += 20

    if keys_pressed[K_RIGHT] and x1 < 1180:
        x1 += 20    


    if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= 20

    if keys_pressed[K_w] and y2 > 0:
        y2 -= 20

    
    if keys_pressed[K_s] and y2 < 700:
        y2 += 20

    if keys_pressed[K_d] and x2 < 1180:
        x2 += 20    


    if keys_pressed[K_a] and x2 > 0:
        x2 -= 20


    clock.tick(FPS)

    display.update()

