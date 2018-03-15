"""
   Name: Sindy Wang
   
   Date: May 20, 2016
   
   Description: This module contains all of the sprite classes need for the
   "Perfect Lawn Simulator" game. It has a Player, Flower, Scorekeeper, Grass 
   and Face class.
   
"""

import pygame, random

class Player(pygame.sprite.Sprite):
    """This class creates the player(mouse)."""
    def __init__(self):
        """This method initiates the player class."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/hand.gif')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
    def update(self):
        """This update method get the mouse's position."""
        self.rect.center = pygame.mouse.get_pos()
        
class Flower(pygame.sprite.Sprite):
    """This class creates the Flower."""
    def __init__(self, screen, seconds):
        """This class initiates the flower class."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/dandelionnotpuff.gif')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()   
        self.__screen = screen
        #these set the time for the flower to do stuff(die, puff, seed)
        self.__dietime = seconds + 6
        self.__pufftime = seconds + 2
        self.__seedtime = seconds + 4
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height()-100)
        
    def puff(self):
        """This method puffs up the flower"""
        self.image = pygame.image.load('sprites/puff.gif')
        self.image = self.image.convert()
        
    def time_to_die(self, seconds):
        """This method returns true if it's time to die."""
        return self.__dietime == seconds

    def time_to_puff(self, seconds):
        """This method returns true when it is time to puff up."""
        return self.__pufftime == seconds
        
    def seed(self):
        """This method leaves the flower with only a stem."""
        self.image = pygame.image.load('sprites/seed.gif')
        self.image = self.image.convert()
        
    def time_to_seed(self, seconds):
        """This method returns true when it is time for the flower to be a stem."""
        return self.__seedtime == seconds    

class ScoreKeeper(pygame.sprite.Sprite):
    """This class creates the scorekeeper for the game."""
    def __init__(self):
        """This method initiates the scorekeeper class."""
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.Font("alterebro-pixel-font.ttf", 30)
        self.__score = 0
        
    def point(self):
        """This method adds 10 points."""
        self.__score += 10
        
    def update(self):
        """This method updates the score board on screen."""
        message = "Score: %d" % self.__score
        self.image = self.__font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (60, 480)
    
class Grass(pygame.sprite.Sprite):
    """This creates the background for the game"""
    def __init__(self,screen):
        """This method initiates the grass class which is also the background class."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('grass.png')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 250)
        
class Face(pygame.sprite.Sprite):
    """This class creates the Face with the emotions."""
    def __init__(self,screen):
        """This method initiates the beginning mood of player, which is happy."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/face1.gif')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (750, 450)
        
    def happy(self):
        """This method is shown when player is doing well."""
        self.image = pygame.image.load('sprites/face1.gif')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (750, 450)
        
    def not_so_good(self):
        """This method is shown when player is doing not so well."""
        self.image = pygame.image.load('sprites/face3.gif')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (750, 450)
        
    def angry(self):
        """This method is shown when player is almost losing or has already lost."""
        self.image = pygame.image.load('sprites/face2.gif')
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (750, 450)
          