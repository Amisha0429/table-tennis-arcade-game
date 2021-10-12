# PONG / TABLE TENNIS ARCADE GAME
# A graphical two-player Pong game.
# The left player controls the left paddle by pressing and holding down the q key to move the paddle up and the a key to move the paddle down. 
# The right player controls the right paddle by pressing and holding down the p key to move the paddle up and the l key to move the paddle down. 

import pygame

# User-defined functions
def main():
    
    # initialize all pygame modules   
    pygame.init()
    
    # create a pygame display window
    display_window = pygame.display.set_mode((750, 500))
    
    # set the title of the display window
    pygame.display.set_caption('PONG ARCADE GAME')
            
    # Colors represented by the RGB values   
    white = (255, 255, 255) 
    black = (0, 0, 0)
    
    # Function that updates the screen
    def update_screen():
        display_window.fill(black)# Displays a black screen
    
        # Font with which the scores will be shown
        font = pygame.font.SysFont('Arial', 50)
    
        # Player 1 Score
        left_paddle_score = font.render(str(left_paddle.points), False, white)
        left_paddle_rect = left_paddle_score.get_rect()#When you call the get_rect method of a pygame.Surface, Pygame creates a new rect with the size of the image and the x, y coordinates (0, 0)
        left_paddle_rect.center = (50, 50)
        # overlap the surface on the canvas at the rect position
        display_window.blit(left_paddle_score, left_paddle_rect)# blit copies content of one surface to another
    
        # Player 2 Score
        right_paddle_score = font.render(str(right_paddle.points), False, white)
        right_paddle_rect = right_paddle_score.get_rect()
        right_paddle_rect.center = (700, 50)
        # overlap the surface on the canvas at the rect position
        display_window.blit(right_paddle_score, right_paddle_rect)
    
        # Updates all Sprites
        sprites.draw(display_window)
    
        # Draws updates
        pygame.display.update()
        

#User-defined classes        
# Classes for Sprites(object on screen that can move around) 
    class Left_Paddle(pygame.sprite.Sprite):
        # Creates Left_Paddle object
        def __init__(self):
            pygame.sprite.Sprite.__init__(self) #Simple base class for visible game objects.
            self.image = pygame.Surface([10, 75])
            self.image.fill(white)
            self.rect = self.image.get_rect()
            self.points = 0
    
    class Right_Paddle(pygame.sprite.Sprite):
        # Create Right_Paddle object
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([10, 75])
            self.image.fill(white)
            self.rect = self.image.get_rect()
            self.points = 0
    
    class Ball(pygame.sprite.Sprite):
        # Creates Ball object
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([10, 10])
            self.image.fill(white)
            self.rect = self.image.get_rect()
            self.speed = 12.5
            self.displace_x = 1
            self.displace_y = 1
    
    # Making a sprite(movable object on screen)
    left_paddle= Left_Paddle()
    left_paddle.rect.x = 25
    left_paddle.rect.y = 225
    
    right_paddle = Right_Paddle()
    right_paddle.rect.x = 715
    right_paddle.rect.y = 225
    
    paddle_speed = 15
    
    pong = Ball()
    pong.rect.x = 375
    pong.rect.y = 250
    
    # Making a group of Sprites
    sprites = pygame.sprite.Group()#A container class to hold and manage multiple Sprite objects.
    sprites.add(left_paddle, right_paddle, pong)#add the sprite to groups
    
    run = True
    
    while run:
    
        pygame.time.delay(100)
    
        # Stops the event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        # Movement of the paddles
        key = pygame.key.get_pressed()
        if key[pygame.K_q]:
            #left paddle moves up
            left_paddle.rect.y =left_paddle.rect.y+(-paddle_speed)
        if key[pygame.K_a]:
            #left paddle moves down
            left_paddle.rect.y =left_paddle.rect.y+(paddle_speed)
        if key[pygame.K_p]:
            #right paddle moves up
            right_paddle.rect.y =right_paddle.rect.y+(-paddle_speed)
        if key[pygame.K_l]:
            #right paddle moves down
            right_paddle.rect.y =right_paddle.rect.y+(paddle_speed)
    
        # Moves/Displaces the pong ball
        pong.rect.x += pong.speed * pong.displace_x
        pong.rect.y += pong.speed * pong.displace_y
    
        # Pong bounces off the wall or paddle
        if pong.rect.y > 490: #bounce up
            pong.displace_y = -1
    
        if pong.rect.y < 1:# bounce down
            pong.displace_y = 1
    
        if pong.rect.x > 740: # bounce left
            pong.rect.x, pong.rect.y = 375, 250
            pong.displace_x = -1
            left_paddle.points += 1
    
        if pong.rect.x < 1: # bounce right
            pong.rect.x, pong.rect.y = 375, 250
            pong.displace_x = 1
            right_paddle.points += 1
    
        if left_paddle.rect.colliderect(pong.rect): # bounce right
            pong.displace_x = 1
    
        if right_paddle.rect.colliderect(pong.rect): # bounce left
            pong.displace_x = -1
    
        # update_screen() is called 
        update_screen()
    
    pygame.quit()

main()
