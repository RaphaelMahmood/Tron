# Example file showing a circle moving on screen
import pygame
import time
p1 = 0
p2 = 0


# pygame setup
pygame.init()
def On():
    if Bigga._alive == True and Digga._alive == True:
        return True
    else:
        return False
    
text_font = pygame.font.SysFont("comicsansms", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))


def Enemy_projectile(self):
        if self._player == 1:
            return Bigga._projectilesRect
        elif self._player == 2:
            return Digga._projectilesRect
        
class Player:     
    def __init__(self, p, c, l, pos, s, sw, sh):
        self._player = p
        self._colour = c
        self._length = l
        self._position = pos
        self._speed = s
        self._screenWidth = sw
        self._screenHeight = sh
        self._projectiles = []
        self._projectilesRect = []
        self._character = []
        self.up = 0
        self.draw = 1
        self._rect = pygame.Rect(self._position[0], self._position[1], self._length,self._length,)
        self.trail = self.Trail()
        self._alive = True
        self._dir = 'down'
    
    def Trail(self):
        if self._player == 1:
            return "cyan"
        elif self._player == 2:
            return "pink"

    def Draw(self, _screen):
        if self._alive:
            for item in self._projectiles:
                item.Draw(_screen)
            self._rect = pygame.Rect(self._position[0], self._position[1], self._length,self._length,)
            pygame.draw.rect(_screen, self._colour, self._rect)

    def Drawdeath(self):
        if self._alive == False:
            if self._player == 1 and Bigga._alive == True:    
                    draw_text("Player 2 Victory", text_font, 'white', screen.get_width() / 2, screen.get_height() / 2)
                    global p2 
                    p2 += 1
                    if pygame.time.get_ticks() > death + 1000:
                        Reset()
            elif self._player == 2 and Digga._alive == True:      
                    draw_text("PLayer 1 Victory", text_font, 'white', screen.get_width() / 2, screen.get_height() / 2)
                    global p1 
                    p1 += 1
                    if pygame.time.get_ticks() > death + 1000:
                        Reset()
    
    
    def Shoot(self):
        keysreleased = pygame.key.get_just_released()
        if keysreleased[pygame.K_RETURN]:
            spawn_pos = pygame.Vector2(self._position.x + self._length/2, self._position.y + self._length/2)
            self._projectiles.append(Projectile(self._player, "black", 10, spawn_pos, 1, WIDTH, HEIGHT))
            

        if keysreleased[pygame.K_LSHIFT] and self._player == 1 or keysreleased[pygame.K_RSHIFT] and self._player == 2  :
          self.draw +=0

        if self.draw%2 > 0:
            spawn_pos = pygame.Vector2(self._position.x, self._position.y)
            self._projectiles.append(Projectile(self._player, self.trail, self._length, spawn_pos, 1, WIDTH, HEIGHT, pygame.time.get_ticks()))

        for item in self._projectiles:
            item.Destroy()
    def RemoveProjectile(self, objectToRemove):
        self._projectiles.remove(objectToRemove)
    def Move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] and self._player == 1 or keys[pygame.K_UP] and self._player == 2) and self._dir != 'down':
            self._dir = 'up'
        if self._dir == 'up':
            if self._position.y > 0:
                self._position.y -= self._speed
        if (keys[pygame.K_s] and self._player == 1 or keys[pygame.K_DOWN] and self._player == 2) and self._dir != 'up':
            self._dir = 'down'
        if self._dir == 'down':
            if self._position.y < 720 - self._length:
                self._position.y += self._speed
        if (keys[pygame.K_a] and self._player == 1 or keys[pygame.K_LEFT] and self._player == 2) and self._dir != 'right':
            self._dir = 'left'
        if self._dir == 'left':
            if self._position.x > 0:
                self._position.x -= self._speed
        if (keys[pygame.K_d] and self._player == 1 or keys[pygame.K_RIGHT] and self._player == 2) and self._dir != 'left':
            self._dir = 'right'
        if self._dir == 'right':
            if self._position.x < 1280 - self._length:
                self._position.x += self._speed
        keysreleased = pygame.key.get_just_released()
        if keysreleased[pygame.K_SPACE]:
          self.up +=1
        if self.up%2 > 0:
            for item in self._projectiles:
                item.Up()
    def RemoveWall(self):
        self._projectiles.clear()
    

        


        
    


class Projectile:
    def __init__(self, o, c, l, pos, s, sw, sh, time):
        self._owner = o
        self._colour = c
        self._length = l
        self._position = pos
        self._speed = s
        self._screenWidth = sw
        self._screenHeight = sh
        self.n = 0
        self._rect = pygame.Rect(self._position[0], self._position[1], self._length,self._length,)
        self._time = time
        self._activate = time + 5000

    def Draw(self, _screen):
        self._rect = pygame.Rect(self._position[0], self._position[1], self._length,self._length,)
        pygame.draw.rect(_screen, self._colour, self._rect)
    
    def Destroy(self):
        if self._position[1] > 0:
                #self._position[1] -= self._speed
                pass
        else:
            if self._owner == 1:
                Digga.RemoveProjectile(self)
            elif self._owner == 2:
                Bigga.RemoveProjectile(self)

    def Up(self):
        self._position[1] -= self._speed

    def Collide(self, player):
            if self._rect.colliderect(player._rect):
                death = pygame.time.get_ticks()
                player._alive = False
                player.RemoveWall()
                
                
    def Collision(self):
        current = pygame.time.get_ticks()
        if current > self._activate:
            if self._owner == 1:
                self._colour = 'white'
            if self._owner == 2:
                self._colour = 'black'
            self.Collide(Digga)
            self.Collide(Bigga)


        
            
def Reset():
    Digga._position = pygame.Vector2(screen.get_width() / 2 - 200,10)
    Bigga._position = pygame.Vector2(screen.get_width() / 2 + 200,10)
    Digga._alive = True
    Bigga._alive = True
    Bigga.RemoveWall()
    Digga.RemoveWall()
    Bigga._dir = 'down'
    Digga._dir = 'down'
    death = 0
def ResetInput():
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]):
            Reset()

def DrawScore():
    draw_text(f"PLayer 1 Score: {p1}", text_font, 'white', screen.get_width() / 2-600, 80)
    draw_text(f"PLayer 2 Score: {p2}", text_font, 'white', screen.get_width() / 2+200, 80)

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))          
clock = pygame.time.Clock()
running = True
player1_pos = pygame.Vector2(screen.get_width() / 2 - 200,10)
player2_pos = pygame.Vector2(screen.get_width() / 2 + 200,10)
spawn_pos = pygame.Vector2(50,500)

Digga = Player(1, "blue", 40, player1_pos, 1, WIDTH, HEIGHT)
Bigga = Player(2, "red", 40, player2_pos, 1, WIDTH, HEIGHT)



while running:



    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    ResetInput()
    Digga.Move()
    Digga.Shoot()
    Digga.Draw(screen)
    Bigga.Move()
    Bigga.Shoot()
    Bigga.Draw(screen)
    Digga.Drawdeath()
    Bigga.Drawdeath()
    DrawScore()
    
    if On():
        for item in Digga._projectiles:
            if item._rect.colliderect(Digga._rect) or item._rect.colliderect(Bigga._rect):
                death = pygame.time.get_ticks()
            item.Collision()
        for item in Bigga._projectiles:
            if item._rect.colliderect(Digga._rect) or item._rect.colliderect(Bigga._rect):
                death = pygame.time.get_ticks()
            item.Collision()
   

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
clock.tick(300)

pygame.quit()