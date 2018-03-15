"""
   Name: Sindy Wang

   Date: May 20, 2016
   
   Description: (Perfect Lawn Simulator) - Objective of this game is to get rid of
   dandelions before they take over your lawn. The only control in this game is
   the mouse and whenever player clicks the flower, they are able to pluck it out.
   If player takes too long, the spread of the flowers will be greater.
   
"""
#IMPORT AND INITIALIZE
import pygame, gameSprites
pygame.init()
pygame.mixer.init() 
screen = pygame.display.set_mode((800, 500))

def menu():
    """This is the intro screen for players to see before starting the game."""
    #DISPLAY
    pygame.display.set_caption("Perfect Lawn Simulator")
    #ENTITIES
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))      
    grass = gameSprites.Grass(screen)
    player = gameSprites.Player()
    intro_image = pygame.image.load("introscreen.png")
    #background music
    pygame.mixer.music.load("backgroundmusic.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1) 
    
    menuSprites = pygame.sprite.OrderedUpdates(grass, player)
    
    #ACTION
    #ASSIGN 
    menuGoing = True
    clock = pygame.time.Clock()
    #LOOP
    while menuGoing:
        #TIME
        clock.tick(60)
        #EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuGoing = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menuGoing = False
        #REFRESH            
        menuSprites.clear(screen, background)
        menuSprites.update()
        menuSprites.draw(screen)  
        screen.blit(intro_image,(-5,-125)) 
        pygame.display.flip() 
        
    pygame.quit()
    
def main():
    """This is main game logic."""
    #DISPLAY
    pygame.display.set_caption("Perfect Lawn Simulator")
    #ENTITIES
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))      
    
    seconds = 0
    #sprites
    player = gameSprites.Player()
    flower = gameSprites.Flower(screen,seconds)
    scorekeeper = gameSprites.ScoreKeeper()
    grass = gameSprites.Grass(screen)
    face = gameSprites.Face(screen)

    #loading gameover sign
    gameover = pygame.image.load("gameoversign.gif")
    gameover = gameover.convert()
    
    #background music
    pygame.mixer.music.load("backgroundmusic.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1) 
    
    #loading sound effect
    pull_sound = pygame.mixer.Sound("ripping-grass.wav")
    pull_sound.set_volume(0.2)
    
    #creating the starting 10 flowers 
    flowers = []
    for i in range(10):
        flowers.append(gameSprites.Flower(screen,seconds))
        
    flowerGroup = pygame.sprite.Group(flowers)
    allSprites = pygame.sprite.OrderedUpdates(grass,flowerGroup,player,scorekeeper,face)
    
    #ACTION
    #ASSIGN    
    clock = pygame.time.Clock()
    keepGoing = True
    pygame.mouse.set_visible(False)
    time = 0
    flowers_hit_list = []
    #LOOP
    while keepGoing:
        #TIME
        clock.tick(30)
        time += 1
        seconds = time / 30
        #EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #collision detection for when player clicks more than 1 flower
                flowers_hit = pygame.sprite.spritecollide(player,flowerGroup,False)
                if flowers_hit:
                    pull_sound.play()
                    flowers_hit_list.append(flowers_hit)
                    flowers_hit_number = len(flowers_hit_list)                     
                for hits in range(len(flowers_hit)):
                    scorekeeper.point()
                for hit in flowers_hit:
                    hit.kill()                   
        #every second, a flower grows
        if (seconds >= 0) and (seconds <= 15):
            if (time % 30 == 0):
                flower = gameSprites.Flower(screen, seconds)
                flowerGroup.add(flower)
                allSprites = pygame.sprite.OrderedUpdates\
                    (grass,flowerGroup,player,scorekeeper,face)
        #every half a second, a flower grows
        if (seconds > 15 ) and (seconds <= 30):
            if (time % 15 == 0):
                flower = gameSprites.Flower(screen, seconds)
                flowerGroup.add(flower)
                allSprites = pygame.sprite.OrderedUpdates\
                    (grass,flowerGroup,player,scorekeeper,face)
        #every 1/6 of a second, a flower grows (beast mode)
        if (seconds > 30 ): 
            if (time % 5 == 0):
                flower = gameSprites.Flower(screen, seconds)
                flowerGroup.add(flower)
                allSprites = pygame.sprite.OrderedUpdates\
                    (grass,flowerGroup,player,scorekeeper,face)
                
        for plant in flowerGroup:
            if plant.time_to_puff(seconds):
                plant.puff()
            elif plant.time_to_seed(seconds):
                plant.seed()
            elif plant.time_to_die(seconds):
                #when player fails to pull flower that has been on screen for too long
                #that flower dies, and 2 more flowers pop up
                for j in range(2):
                    newflower = gameSprites.Flower(screen, seconds)
                    flowerGroup.add(newflower)
                    allSprites = pygame.sprite.OrderedUpdates\
                        (grass,flowerGroup,player,scorekeeper,face)
                    plant.kill()
       
            # checking amount of flowers on screen so the face class can change
            if (len(flowerGroup) >= 0) and (len(flowerGroup) <= 20):
                face.happy()
            if (len(flowerGroup) > 20)  and (len(flowerGroup) <= 35):
                face.not_so_good()
            if (len(flowerGroup) > 35):
                face.angry()
            #when there are 60 flowers on screen, game is over
            if len(flowerGroup) == 50:
                keepGoing = False
        #REFRESH   
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip() 
        
    pygame.mixer.music.fadeout(3000)
    screen.blit(gameover, (300, 200))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
                    
menu()