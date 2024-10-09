import time
import pygame
import random
import asyncio
from pygame import mixer

async def main():
    """
    Constantes globales
    """
    #--------------------------------------------GLOBALS-----------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------
    # Colors
    BLACK = (0, 0, 0) 
    WHITE = (255, 255, 255) 
    BLUE = (0, 0, 255)
    GREEN = (0,80,0)
    RED =(255,80,0)
    LIGTH_BLUE=(0,100,190)
    
    # Screen size
    SCREEN_WIDTH  = 1000
    SCREEN_HEIGHT = 900


    #--------------------------------------------GLOBALS--------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------


    #--------------------------------------------FUNCTIONS--START---------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------
    def printCompleteMissions(screen,contMission):#---ONLY PRINT
        pygame.font.init()
        mission2=("MISSIONS COMPLETE: "+str(contMission)+"")
        font=pygame.font.SysFont('', 25)
        mission2Text=font.render(mission2,True,(255,0,0))
        mission2Rect=mission2Text.get_rect()
        mission2Rect.center=(880,100)
        screen.blit(mission2Text,mission2Rect)

    def printMission(screen,nMission):#---ONLY PRINT
        pygame.font.init()
        mission=("MISSION : GET "+str(nMission)+" Pts")
        font=pygame.font.SysFont('', 25)
        missionText=font.render(mission,True,(255,0,255))
        missionRect=missionText.get_rect()
        missionRect.center=(880,200)
        screen.blit(missionText,missionRect)

    def printGravedad(screen,cont):#---ONLY PRINT
        pygame.font.init()
        gravity=("GRAVITY : [ +"+str(cont)+" ]")
        font=pygame.font.SysFont('', 33)
        gravityText=font.render(gravity,True,(255,0,255))
        gravityRect=gravityText.get_rect()
        gravityRect.center=(100,500)
        screen.blit(gravityText,gravityRect)

    def printLevel(screen):#---ONLY PRINT
        pygame.font.init()
        Level=("LEVEL : [ 1 ]")
        font=pygame.font.SysFont('', 40)
        LevelText=font.render(Level,True,(255,255,255))
        LevelRect=LevelText.get_rect()
        LevelRect.center=(100,400)
        screen.blit(LevelText,LevelRect)

    def printControls0(screen):#---ONLY PRINT
        pygame.font.init()
        control0=("BASIC CONTROLS:")
        font=pygame.font.SysFont('', 30)
        control0Text=font.render(control0,True,(255,0,0))
        control0Rect=control0Text.get_rect()
        control0Rect.center=(880,570)
        screen.blit(control0Text,control0Rect)

    def printControls1(screen):#---ONLY PRINT
        pygame.font.init()
        control1=("[SPACE]-[ENTER] = STICKS")
        font=pygame.font.SysFont('', 27)
        control1Text=font.render(control1,True,(255,255,255))
        control1Rect=control1Text.get_rect()
        control1Rect.center=(880,610)
        screen.blit(control1Text,control1Rect)

    def printControls2(screen):#---ONLY PRINT
        pygame.font.init()
        control2=("[4] - LAUNCH THE BALL")
        font=pygame.font.SysFont('', 27)
        control2Text=font.render(control2,True,(255,255,255))
        control2Rect=control2Text.get_rect()
        control2Rect.center=(880,640)
        screen.blit(control2Text,control2Rect)

    def printLife(screen,lifes):#---ONLY PRINT
        pygame.font.init()
        Life="LIFES: "+str(lifes)
        font=pygame.font.SysFont('', 40)
        LifeText=font.render(Life,True,(255,255,255))
        LifeRect=LifeText.get_rect()
        LifeRect.center=(850,400)
        screen.blit(LifeText,LifeRect)

    def printScore(screen,points):#---ONLY PRINT
        pygame.font.init()
        Score="SCORE: "+str(points)
        font=pygame.font.SysFont('', 40)
        ScoreText=font.render(Score,True,(255,255,255))
        ScoreRect=ScoreText.get_rect()
        ScoreRect.center=(880,475)
        screen.blit(ScoreText,ScoreRect)

    def ballWallImpactSound():#---ONLY SOUND
        #ballWall=mixer.Sound('sources/ballBloque1.mp3')
        #ballWall.play()
        #ballWall.set_volume(0.7)
        pass
    def makeBall(spriteBalls, x, y):
        
        # Create a sprite
        ball = pygame.sprite.Sprite()
        
        # Set an image surface , dimensions
        ball.image = pygame.Surface([15, 15])
        

        ball.image.fill(RED)
        
        # Get and set the coords position
        ball.rect = ball.image.get_rect()
        ball.rect.x = x
        ball.rect.y = y

        # Speeds
        ball.speed_x =0
        ball.speed_y =0

        #Set the img
        ball.image = pygame.image.load("images/ballP.png").convert_alpha()
        
        #Add to the sprite group
        spriteBalls.add(ball)
        
        return ball

    def makeBall2(spriteBalls, x, y):
        
        # Create a sprite
        ball2 = pygame.sprite.Sprite()
        
        # Set an image surface , dimensions
        ball2.image = pygame.Surface([15, 15])

        ball2.image.fill(RED)
        
        # Get and set the coords position
        ball2.rect = ball.image.get_rect()
        ball2.rect.x = x
        ball2.rect.y = y

        # Speeds
        ball2.speed_x =4
        ball2.speed_y =8
        ball2.image = pygame.image.load("images/ballP.png").convert_alpha()
        #Add to the sprite group
        spriteBalls.add(ball2)
        
        return ball2

    def makeBall3(spriteBalls, x, y):
        
        # Create a sprite
        ball3 = pygame.sprite.Sprite()
        
        # Set an image surface , dimensions
        ball3.image = pygame.Surface([15, 15])
        

        ball3.image.fill(RED)
        
        # Get and set the coords position
        ball3.rect = ball.image.get_rect()
        ball3.rect.x = x
        ball3.rect.y = y

        # Speeds
        ball3.speed_x =-4
        ball3.speed_y =8
        ball3.image = pygame.image.load("images/ballP.png").convert_alpha()
        #Add to the sprite group
        spriteBalls.add(ball3)
        
        return ball3


    def updateball(moveLeftTunnel,moveLeftTunnel2,moveLeftTunnel3,moveRigthTunnel,moveRigthTunnel2,moveRigthTunnel3,extraLife_bumper_X,lifes,ball,ball2,ball3,external_wall_Btunnel,internal_wallBtunnel,extraLife_bumper,Walls,WallslateralStick_wall,topWall,whiteBumpers,LeftStick,RigthStick,paloExterior,red_closer,points,cont):

        #BALLS GRAVITY , ONLY APPLY WHEN THE BALLS STAY OUT OF THE LAUNCHER.
        if ball.rect.right<740:
            calculateGravity(ball)
        if ball2.rect.right<740:
            calculateGravity2(ball2)
        if ball3.rect.right<740:
            calculateGravity3(ball3)
        
        #Hot-FIXS
        ball.image = pygame.image.load("images/ballP.png").convert_alpha()#Reimplementation of the image of the ball, for possible visual errors

        #BALL SPEEDS
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
        
        ball2.rect.x +=ball2.speed_x
        ball2.rect.y +=ball2.speed_y

        ball3.rect.x +=ball3.speed_x
        ball3.rect.y +=ball3.speed_y

        #LATERAL NORMAL WALLS
        impacts_list_normal_wall = pygame.sprite.spritecollide(ball,Walls, False)
        impacts_list_normal_wall2 = pygame.sprite.spritecollide(ball2,Walls, False)
        impacts_list_normal_wall3 = pygame.sprite.spritecollide(ball3,Walls, False)

        #LATERAL STICK WALLS
        impacts_list_lateralStick_wall = pygame.sprite.spritecollide(ball,WallslateralStick_wall, False)
        impacts_list_lateralStick_wall2 = pygame.sprite.spritecollide(ball2,WallslateralStick_wall, False)
        impacts_list_lateralStick_wall3 = pygame.sprite.spritecollide(ball3,WallslateralStick_wall, False)

        #TOP WALL
        impacts_list_topWall = pygame.sprite.spritecollide(ball, topWall, False)
        impacts_list_topWall2 = pygame.sprite.spritecollide(ball2, topWall, False)
        impacts_list_topWall3 = pygame.sprite.spritecollide(ball3, topWall, False)

        #WHITE BUMPERS
        impacts_list_whiteBumpers = pygame.sprite.spritecollide(ball,whiteBumpers,False)
        impacts_list_whiteBumpers2 = pygame.sprite.spritecollide(ball2,whiteBumpers,False)
        impacts_list_whiteBumpers3 = pygame.sprite.spritecollide(ball3,whiteBumpers,False)
        
        #LEFT STICK
        impacts_list_left_Stick = pygame.sprite.spritecollide(ball,LeftStick,False)
        impacts_list_left_Stick2 = pygame.sprite.spritecollide(ball2,LeftStick,False)
        impacts_list_left_Stick3 = pygame.sprite.spritecollide(ball3,LeftStick,False)

        #RIGTH STICK
        impacts_list_rigth_Stick = pygame.sprite.spritecollide(ball,RigthStick,False)
        impacts_list_rigth_Stick2 = pygame.sprite.spritecollide(ball2,RigthStick,False)
        impacts_list_rigth_Stick3 = pygame.sprite.spritecollide(ball3,RigthStick,False)

        #EXTERNAL WALLS (GREEN WALLS) , EXTERNAL EXTRUCTURE
        impacts_list_external_wall = pygame.sprite.spritecollide(ball,paloExterior,False)

        #RED CLOSER (LAUNCHER)
        impacts_list_red_closer = pygame.sprite.spritecollide(ball,red_closer,False)

        #EXTRA LIFE BUMPER
        impacts_list_extraLife_bumper = pygame.sprite.spritecollide(ball,extraLife_bumper, False)
        impacts_list_extraLife_bumper2 = pygame.sprite.spritecollide(ball2,extraLife_bumper, False)
        impacts_list_extraLife_bumper3 = pygame.sprite.spritecollide(ball3,extraLife_bumper, False)

        #INTERNAL WALL (BIG TUNNEL)
        impacts_list_internal_wallBtunnel = pygame.sprite.spritecollide(ball,internal_wallBtunnel, False)
        impacts_list_internal_wallBtunnel2 = pygame.sprite.spritecollide(ball2,internal_wallBtunnel, False)
        impacts_list_internal_wallBtunnel3 = pygame.sprite.spritecollide(ball3,internal_wallBtunnel, False)

        #EXTERNAL WALLS (BIG TUNNEL)
        impacts_list_external_wall_Btunnel = pygame.sprite.spritecollide(ball,external_wall_Btunnel, False)
        impacts_list_external_wall_Btunnel2 = pygame.sprite.spritecollide(ball2,external_wall_Btunnel, False)
        impacts_list_external_wall_Btunnel3 = pygame.sprite.spritecollide(ball3,external_wall_Btunnel, False)
        
        #IMPORTANT---------ON EVERY IMPACT , THE MOVERIGTH OR MOVELEFT FOR THE BIG TUNNEL IS RESET TO TRUE VALUE!!!! , EXCEPT EXTERNAL BIG TUNNEL WALLS , LACUNHER AND EXTERNAL BOARD WALLS.

        keyPressed = pygame.key.get_pressed()

        #EXTERNAL WALLS (BIG TUNNEL)
        for Wall in impacts_list_external_wall_Btunnel:
            ball.speed_y*=-1

        for Wall in impacts_list_external_wall_Btunnel2:
            ball2.speed_y*=-1

        for Wall in impacts_list_external_wall_Btunnel3:
            ball3.speed_y*=-1

        #INTERNAL WALL (BIG TUNNEL)
        for Wall in impacts_list_internal_wallBtunnel:
            ball.speed_y=0
            ball.rect.y=385
            ball.rect.bottom=Wall.rect.top+7

            
        
        for Wall in impacts_list_internal_wallBtunnel2:
            ball2.speed_y=0
            ball2.rect.y=385
            ball2.rect.bottom=Wall.rect.top+7



        for Wall in impacts_list_internal_wallBtunnel3:
            ball3.speed_y=0
            ball3.rect.y=385
            ball3.rect.bottom=Wall.rect.top+7


        #EXTRA LIFE BUMPER
        for Wall in impacts_list_extraLife_bumper:
            print("ball1 - bumper lifes up")
            lifesUpSound()
            lifes+=1
            if lifes>=5:
                lifes=5
            extraLife_bumper_X=9999
            ball.speed_x*=-1
            moveLeftTunnel=True
            moveRigthTunnel=True


        for Wall in impacts_list_extraLife_bumper2:
            print("ball2 - bumper lifes up")
            lifesUpSound()
            lifes+=1
            extraLife_bumper_X=9999
            ball2.speed_x*=-1
            moveLeftTunnel2=True
            moveRigthTunnel2=True

        for Wall in impacts_list_extraLife_bumper3:
            print("ball3 - bumper lifes up")
            lifesUpSound()
            lifes+=1
            extraLife_bumper_X=9999
            ball3.speed_x*=-1
            moveLeftTunnel3=True
            moveRigthTunnel3=True

        #LATERAL STICK WALLS
        for Wall in impacts_list_lateralStick_wall:
            print("LATERAL STICK WALL")
            ballWallImpactSound()
            ball.rect.bottom= Wall.rect.top+5
            ball.speed_y*=-1
            moveLeftTunnel=True
            moveRigthTunnel=True

        for Wall in impacts_list_lateralStick_wall2:
            print("LATERAL STICK WALL")
            ballWallImpactSound()
            ball2.rect.bottom= Wall.rect.top+5
            ball2.speed_y*=-1
            moveLeftTunnel2=True
            moveRigthTunnel2=True

        for Wall in impacts_list_lateralStick_wall3:
            print("LATERAL STICK WALL")
            ballWallImpactSound()
            ball3.rect.bottom= Wall.rect.top+5
            ball3.speed_y*=-1
            moveLeftTunnel3=True
            moveRigthTunnel3=True

        #RED CLOSER (LAUNCHER)
        for Wall in impacts_list_red_closer:
            if ball.rect.right<700:
                ball.speed_x=-ball.speed_x
                print("RED CLOSER APPEARS")
                
        #EXTERNAL WALLS (GREEN WALLS) , EXTERNAL EXTRUCTURE
        for Wall in impacts_list_external_wall:
            ball.rect.bottom = Wall.rect.top
        
        #WHEN ANY BALL IMPACT WITH AN STICK 
        # -> IF THE STISCK IS UP , THE BALL Y SET ON NEGATIVE + CONT(GRAVITY)
        # -> IF THE STICK IS DOWN , THE BALL ROLLS OVER THE STICK , (THE REAL HITBOX IS AN SQUARE OR RECTANGLE , NOT A DIAGONAL HITBOX)
        #RIGTH STICK BALL1
        for Wall in impacts_list_rigth_Stick:
            moveLeftTunnel=True
            moveRigthTunnel=True
            if keyPressed[pygame.K_RETURN]:
                ball.rect.bottom = Wall.rect.top
                ball.speed_y=-26+-cont
                if ball.speed_x <0:
                    ball.speed_x=-10+-cont
                else:
                    ball.speed_x=10+cont
            else:
                ball.rect.bottom=Wall.rect.top

        #LEFT STICK BALL1
        for Wall in impacts_list_left_Stick:
            moveLeftTunnel=True
            moveRigthTunnel=True

            if keyPressed[pygame.K_SPACE]:
                ball.rect.bottom = Wall.rect.top
                ball.speed_y=-26+-cont
                if ball.speed_x <0:
                    ball.speed_x=-10+-cont
                else:
                    ball.speed_x=10+cont
            else:
                ball.rect.bottom=Wall.rect.top

        #RIGTH STICK BALL2
        for Wall in impacts_list_rigth_Stick2:
            moveLeftTunnel2=True
            moveRigthTunnel2=True
            
            if keyPressed[pygame.K_RETURN]:
                ball2.rect.bottom = Wall.rect.top
                ball2.speed_y=-26+-cont
                if ball2.speed_x <0:
                    ball2.speed_x=-10+-cont
                else:
                    ball2.speed_x=10+cont
            else:
                ball2.rect.bottom=Wall.rect.top
        
        #LEFT STICK BALL2
        for Wall in impacts_list_left_Stick2:
            moveLeftTunnel2=True
            moveRigthTunnel2=True

            if keyPressed[pygame.K_SPACE]:
                ball2.rect.bottom = Wall.rect.top
                ball2.speed_y=-26+-cont
                if ball2.speed_x <0:
                    ball2.speed_x=-10+-cont
                else:
                    ball2.speed_x=10+cont
            else:
                ball2.rect.bottom=Wall.rect.top
        
        #RIGTH STICK BALL3
        for Wall in impacts_list_rigth_Stick3:
            moveLeftTunnel3=True
            moveRigthTunnel3=True
            
            if keyPressed[pygame.K_RETURN]:
                ball3.rect.bottom = Wall.rect.top
                ball3.speed_y=-26+-cont
                if ball3.speed_x <0:
                    ball3.speed_x=-10+-cont
                else:
                    ball3.speed_x=10+cont
            else:
                ball3.rect.bottom=Wall.rect.top
        
        #LEFT STICK BALL3
        for Wall in impacts_list_left_Stick3:
            moveLeftTunnel3=True
            moveRigthTunnel3=True

            if keyPressed[pygame.K_SPACE]:
                ball3.rect.bottom = Wall.rect.top
                ball3.speed_y=-26+-cont
                if ball3.speed_x <0:
                    ball3.speed_x=-10+-cont
                else:
                    ball3.speed_x=10+cont
            else:
                ball3.rect.bottom=Wall.rect.top

        #WHITE BUMPERS
        #THE WITHE BUMPERS USE randomNumer FOR CHANGE THE X OR NOT CHANGE IT ,THIS GIVE MORE POSSIBILITIES FOR THE BALL.
        #THE WHITE BUMPERS USE X1.025 SPEED MULTIPLIER.
        randomNumber=random.randint(1,2)#RAMDOM DIRECTION TO IMPACT
        #BALL 1 IMPACTS
        for Wall in impacts_list_whiteBumpers:
            moveLeftTunnel=True
            moveRigthTunnel=True
            ballWallImpactSound()#SOUND
            
            ball.speed_y*=(-1.025)#-------------------------
            ball.speed_x*=(-1.025)

            if randomNumber==1:
                ball.speed_x*=-1.025#-------------------------
            else:
                ball.speed_x*=1.025

            points+=25

        #BALL 2 IMPACTS
        for Wall in impacts_list_whiteBumpers2:
            moveLeftTunnel2=True
            moveRigthTunnel2=True
            ballWallImpactSound()
            
            ball2.speed_y*=(-1.025)#-------------------------
            ball2.speed_x*=(-1.025)

            if randomNumber==1:
                ball2.speed_x*=-1.025#-------------------------
            else:
                ball2.speed_x*=1.025

            points+=25

        #BALL 3 IMPACTS
        for Wall in impacts_list_whiteBumpers3:
            moveLeftTunnel3=True
            moveRigthTunnel3=True
            ballWallImpactSound()
            
            ball3.speed_y*=(-1.025)#-------------------------
            ball3.speed_x*=(-1.025)

            if randomNumber==1:
                ball3.speed_x*=-1.025#-------------------------
            else:
                ball3.speed_x*=1.025

            points+=25
            
        
        #TOP WALL
        # IMPACTS ONLY FOR SOUND AND RESETS         
        for Wall in impacts_list_topWall:
            print("ball1 TOP WALL")
            ballWallImpactSound()
            moveLeftTunnel=True
            moveRigthTunnel=True

        for Wall in impacts_list_topWall2:
            print("ball2 TOP WALL")
            ballWallImpactSound()
            moveLeftTunnel2=True
            moveRigthTunnel2=True

        for Wall in impacts_list_topWall3:
            print("ball3 TOP WALL")
            ballWallImpactSound()
            moveLeftTunnel3=True
            moveRigthTunnel3=True

        #LATERAL NORMAL WALLS
        #IMPACTS ONLY FOR SOUND AND RESETS
        for Wall in impacts_list_normal_wall:
            ballWallImpactSound()
            moveLeftTunnel=True
            moveRigthTunnel=True
                

        for Wall in impacts_list_normal_wall2:
            ballWallImpactSound()
            moveLeftTunnel2=True
            moveRigthTunnel2=True

        for Wall in impacts_list_normal_wall3:
            ballWallImpactSound()
            moveLeftTunnel3=True
            moveRigthTunnel3=True

        return points,lifes,extraLife_bumper_X,moveLeftTunnel,moveLeftTunnel2,moveLeftTunnel3,moveRigthTunnel,moveRigthTunnel2,moveRigthTunnel3
        
    def calculateGravity(ball):
        #BALL 1 GRAVITY
        ball.speed_y +=0.20
        
    def calculateGravity2(ball2):
        #BALL 2 GRAVITY
        ball2.speed_y +=0.20

    def calculateGravity3(ball3):
        #BALL 3 GRAVITY
        ball3.speed_y +=0.20

    def makeWall(x , y, width, height):
        #Create a sprite
        Wall = pygame.sprite.Sprite()
        
        # Set an image surface , dimensions
        Wall.image = pygame.Surface([width,height])
    
        Wall.image.fill(BLUE)
        
        # Get and set the coords position
        Wall.rect = Wall.image.get_rect()
        Wall.rect.y = y
        Wall.rect.x = x
        
        return Wall

    def makeInternalBigTunnel(x , y, width, height):
        #Create a sprite
        Wall = pygame.sprite.Sprite()
        
        #Set an image surface , dimensions.
        Wall.image = pygame.Surface([width,height])
    
        Wall.image.fill(RED)
        
        # Get and set the coords position
        Wall.rect = Wall.image.get_rect()
        Wall.rect.y = y
        Wall.rect.x = x
        Wall.image.set_colorkey(RED)
        return Wall

    def makeExternalWallBTunnel(x , y, width, height):
        #Create a sprite
        Wall = pygame.sprite.Sprite()
        
        #Set an image surface , dimensions.
        Wall.image = pygame.Surface([width,height])
    
        Wall.image.fill(GREEN)
        
        # Get and set the coords position
        Wall.rect = Wall.image.get_rect()
        Wall.rect.y = y
        Wall.rect.x = x
        Wall.image.set_colorkey(GREEN)
        
        return Wall

    def makeLateralStickWall(x , y, width, height):
        #Create a sprite
        Wall = pygame.sprite.Sprite()
        
        #Set an image surface , dimensions.
        Wall.image = pygame.Surface([width,height])
    
        Wall.image.fill(LIGTH_BLUE)
        
        # Get and set the coords position
        Wall.rect = Wall.image.get_rect()
        Wall.rect.y = y
        Wall.rect.x = x
        
        return Wall

    def makeLeftStick(x , y, width, height):
        #Create a sprite
        Wall_stick = pygame.sprite.Sprite()
        
        #Set an image surface , dimensions.
        Wall_stick.image = pygame.Surface([width,height])
    
        Wall_stick.image.fill(BLUE)
        
        # Get and set the coords position
        Wall_stick.rect = Wall_stick.image.get_rect()
        Wall_stick.rect.y = y
        Wall_stick.rect.x = x

        return Wall_stick

    def makeRigthStick(x , y, width, height):
        #Create a sprite
        Wall_stick = pygame.sprite.Sprite()
        
        #Set an image surface , dimensions.
        Wall_stick.image = pygame.Surface([width,height])
    
        Wall_stick.image.fill(BLUE)
        
        # Get and set the coords position
        Wall_stick.rect = Wall_stick.image.get_rect()
        Wall_stick.rect.y = y
        Wall_stick.rect.x = x

    
        return Wall_stick

    def makeExternalWall(x , y, width, height):
        #Create a sprite
        Wall = pygame.sprite.Sprite()
        
        #Set an image surface , dimensions.
        Wall.image = pygame.Surface([width,height])
    
        Wall.image.fill(GREEN)
        
        # Get and set the coords position
        Wall.rect = Wall.image.get_rect()
        Wall.rect.y = y
        Wall.rect.x = x

        return Wall

    def makeRedCloser(x , y, width, height):
        #Create a sprite
        Wall = pygame.sprite.Sprite()
        
        #Set an image surface , dimensions.
        Wall.image = pygame.Surface([width,height])
    
        Wall.image.fill(RED)
        
        # Get and set the coords position
        Wall.rect = Wall.image.get_rect()
        Wall.rect.y = y
        Wall.rect.x = x

        return Wall
    def makeBumper(x , y, width, height):
        #Create a sprite
        Wall = pygame.sprite.Sprite()
        
        #Set an image surface , dimensions.
        Wall.image = pygame.Surface([width,height])
    
        Wall.image.fill(WHITE)
        
        # Get and set the coords position
        Wall.rect = Wall.image.get_rect()
        Wall.rect.y = y
        Wall.rect.x = x

        Wall.image= pygame.image.load("images/bumperP.png").convert_alpha()
        return Wall

    def makeNormalWalls(spriteWalls):
        #Making the walls (x,y,width,height)

        #Wall 1
        Wall1 = makeWall(200,0,10,SCREEN_HEIGHT)

        spriteWalls.add(Wall1)
        

        #Wall 4
        Wall4 = makeWall(700,40,10,SCREEN_HEIGHT)
        spriteWalls.add(Wall4)

        return spriteWalls

    def makeLateralStickWalls(spriteLateral_StickWalls):
        #Making the walls (x,y,width,height)
        #THE LATERAL STICK WALLS--------------

        #Wall21
        Wall21 = makeLateralStickWall(255,725,10,40)
        spriteLateral_StickWalls.add(Wall21)

        #Wall22
        Wall22 = makeLateralStickWall(255,755,55,10)
        spriteLateral_StickWalls.add(Wall22)

        #Wall23
        Wall23 = makeLateralStickWall(657,725,10,40)
        spriteLateral_StickWalls.add(Wall23)

        #Wall24
        Wall24 = makeLateralStickWall(602,755,55,10)
        spriteLateral_StickWalls.add(Wall24)

        return spriteLateral_StickWalls 

    def makeTopWalls(sprite_topWalls):
        #Making the walls (x,y,width,height)
        #TOP WALLS
        #Wall 2
        Wall2 = makeWall(200,0,500,10)
        sprite_topWalls.add(Wall2)

        #Wall 11
        Wall11 = makeWall(600,0,500,10)
        sprite_topWalls.add(Wall11)

        

        return sprite_topWalls

    def makeBumpers(sprite_white_bumpers):
        #Making the walls (x,y,width,height)
        #MAKE THE BUMPERS

        #BUMPERS
        bumper1 = makeBumper(250,150,35,35)
        sprite_white_bumpers.add(bumper1)

        bumper2 = makeBumper(625,150,35,35)
        sprite_white_bumpers.add(bumper2)

        bumper3 = makeBumper(435,225,35,35)
        sprite_white_bumpers.add(bumper3)

        bumper4 = makeBumper(435,500,35,35)
        sprite_white_bumpers.add(bumper4)

        bumper4 = makeBumper(440,850,15,15)#----BOTTOM--IS MORE SMALL
        sprite_white_bumpers.add(bumper4)

        bumper6 = makeBumper(215,680,50,20)#--LEFT SIDE BUMPER
        sprite_white_bumpers.add(bumper6)

        Bumper7 = makeBumper(660,680,50,20)#--RIGTH SIDE BUMPER
        sprite_white_bumpers.add(Bumper7)

        return sprite_white_bumpers

    def makeExternalWalls(spriteexternal_wallerior):
        #Making the walls (x,y,width,height)

        #Wall 12
        Wall12 = makeExternalWall(740,30,500,10)
        spriteexternal_wallerior.add(Wall12)

        #Wall 17
        Wall17 = makeExternalWall(740,40,10,SCREEN_HEIGHT)
        spriteexternal_wallerior.add(Wall17)

        #Wall 18
        Wall18 = makeExternalWall(740,520,500,10)
        spriteexternal_wallerior.add(Wall18)

        #Wall 19
        Wall19 = makeExternalWall(710,720,40,10)
        spriteexternal_wallerior.add(Wall19)

        return spriteexternal_wallerior

    def makeRedClosers(sprite_redCloser):
        #Making the walls (x,y,width,height)
        #MAKE THE MINI WALL OF THE RED CLOSER
        #Wall 25
        Wall25 = makeRedCloser(700,0,11,SCREEN_HEIGHT)
        sprite_redCloser.add(Wall25)


        return sprite_redCloser

    def flipSound(vol):
        #THE FLIP SOUND , FOR THE STICKS
        #flip_sound=mixer.Sound('sources/pinballFlip.mp3')
        #flip_sound.play(0)
        #flip_sound.set_volume(vol)
        pass

    def startSound():
        #THE START SOUND
        #start=mixer.Sound('sources/start.mp3')
        #start.play(0)
        pass

    def manageEvents(ball, isRunning,moveHack):
        #MANAGE THE EVENTS ON THE GAME (NOT ALL)
        
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                
                isRunning = False
            
            elif evento.type == pygame.KEYDOWN:
                #STICKS SOUND PLAY--------------
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE :
                    flipSound(1)
                    print("ENTER OR SPACE")

                #START SOUND PLAY---------------(WHEN THE PRINCIPAL BALL IS OUT OF THE LAUNCHER)
                if ball.rect.x>710 and ball.rect.y>700:
                    if evento.key == pygame.K_4:
                        startSound()
                        ball.speed_y=-40

                #MOVEHACK AND STICK (flip) SOUNDS
                if evento.key == pygame.K_LEFT and moveHack:
                    ball.speed_x=-12
                elif evento.key == pygame.K_RIGHT and moveHack:
                    ball.speed_x=12
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and ball.speed_x <0 and moveHack:
                    ball.speed_x = 0
                elif evento.key == pygame.K_RIGHT and ball.speed_x >0 and moveHack:
                    ball.speed_x = 0
                if evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE :
                    flipSound(0.5)
        
        return isRunning

    def LeftStick(screen,spriteLeftStick):
        #MAKE THE LEFT STICK
        image1 = makeLeftStick(310,750,120,20)
        # Define surface
        image1.image = pygame.Surface((120,20))  
        # SET COLOR FOR COLORKEY
        image1.image.set_colorkey(BLACK)  
        # FILL SURFACE WITH A COLOR 
        image1.image.fill(RED)
        
        keyPressed = pygame.key.get_pressed()  


        # MAKE AN IMAGE COPY
        image = image1.image.copy() 
        # COLORKEY FOR COPY
        image.set_colorkey(BLACK)  
        # GETTING RECT FOR IMAGE AND POSITION
        rect = image.get_rect()  
        rect.center = (310,750)

        if keyPressed[pygame.K_SPACE]:
            #ROTATE TO +0
            new_image = pygame.transform.rotate(image1.image,0)
        else:
            #ROTATE TO -25
            new_image = pygame.transform.rotate(image1.image,-25)

        #RECT FOR NEW IMAGE
        rect = new_image.get_rect()
        rect.left=310
        rect.top=750

        if keyPressed[pygame.K_SPACE]:
            #ROTATE TO +0
            new_image= pygame.image.load("images/flipperIzquieredaUp3.png").convert_alpha()
        else:
            #ROTATE TO -25
            new_image= pygame.image.load("images/flipperIzquieredaDown3.png").convert_alpha()
        spriteLeftStick.add(image1)

        screen.blit(new_image,rect)

        return spriteLeftStick
        
    def RigthStick(screen,spriteRigthStick):
        #MAKE THE RIGTH STICK
        image1 = makeRigthStick(482,750,110,20)
        # Define surface
        image1.image = pygame.Surface((120,20))  
        # SET COLOR FOR COLORKEY
        image1.image.set_colorkey(BLACK)  
        # FILL SURFACE WITH A COLOR 
        image1.image.fill(RED)
        
        keyPressed = pygame.key.get_pressed()  


        # Creamos una copia de la otra superficie para rotarla
        image = image1.image.copy() 
        # COLORKEY FOR COPY
        image.set_colorkey(BLACK)  
        # GETTING RECT FOR IMAGE AND POSITION
        rect = image.get_rect()  
        rect.center = (482,750)

        if keyPressed[pygame.K_RETURN]:
            #ROTATE TO +0
            new_image = pygame.transform.rotate(image1.image,0)
        else:
            #ROTATE TO +25
            new_image = pygame.transform.rotate(image1.image,+25)

        #RECT FOR NEW IMAGE
        rect = new_image.get_rect()
        rect.left=482
        rect.top=750

        if keyPressed[pygame.K_RETURN]:
            #ROTATE TO +0
            new_image= pygame.image.load("images/flipperDerechaUp3.png").convert_alpha()
        else:
            #ROTATE TO -25
            new_image= pygame.image.load("images/flipperDerechaDown3.png").convert_alpha()

        spriteRigthStick.add(image1)
        
        screen.blit(new_image,rect)
        
        return spriteRigthStick

    def makeExtraLifeBumper(sprite_extraLife_bumper, x, y):
        #MAKE THE LIFE UP BUMPER
        # Create a sprite
        extraLife_bumper = pygame.sprite.Sprite()
        
        # Set an image surface , dimensions
        extraLife_bumper.image = pygame.Surface([35, 35])
        

        extraLife_bumper.image.fill(RED)
        
        # Get and set the coords position
        extraLife_bumper.rect = extraLife_bumper.image.get_rect()
        extraLife_bumper.rect.x = x
        extraLife_bumper.rect.y = y


        extraLife_bumper.image = pygame.image.load("images/bumperPAparece.png").convert_alpha()
        #Add to the sprite group
        extraLife_bumper.add(sprite_extraLife_bumper)
        
        return extraLife_bumper

    def makeTopPipe(sprite_top_pipe, x, y):
        #MAKE THE TOP PIPE (RED)
        # Create a sprite
        topPipe = pygame.sprite.Sprite()
        
        # Set an image surface , dimensions
        topPipe.image = pygame.Surface([35, 25])
        

        topPipe.image.fill(RED)
        
        # Get and set the coords position
        topPipe.rect = topPipe.image.get_rect()
        topPipe.rect.x = x
        topPipe.rect.y = y


        topPipe.image = pygame.image.load("images/tunnelJoin.png").convert_alpha()
        #Add to the sprite group
        topPipe.add(sprite_top_pipe)
        
        return topPipe

    def makeBottomPipe(sprite_bottom_pipe, x, y):
        #MAKE THE BOTTOM PIPE (YELLOW)
        # Create a sprite
        bottomPipe = pygame.sprite.Sprite()
        
        # Set an image surface , dimensions
        bottomPipe.image = pygame.Surface([35, 25])
        

        bottomPipe.image.fill(RED)
        
        # Get and set the coords position
        bottomPipe.rect = topPipe.image.get_rect()
        bottomPipe.rect.x = x
        bottomPipe.rect.y = y


        bottomPipe.image = pygame.image.load("images/tunnelOut.png").convert_alpha()
        #Add to the sprite group
        bottomPipe.add(sprite_bottom_pipe)
        
        return bottomPipe

    def makeInternalWallBigTunnel(sprite_internalWall_Btunnel):
        #Making the walls (x,y,width,height)
        #MAKE THE INTERNAL WALL FOR THE BIG TUNNEL
        #Wall 26
        Wall26 = makeInternalBigTunnel(360,400,200,10)
        sprite_internalWall_Btunnel.add(Wall26)


        return sprite_internalWall_Btunnel


    #EXTERNAL WALLS (BIG TUNNEL)
    def makeExternalWallsBigTunnel(sprite_externalWall_Btunnel):
        #Making the walls (x,y,width,height)
        #MAKE THE EXTERNAL WALLS FOR THE BIG TUNNEL
        #Wall 26
        Wall28 = makeExternalWallBTunnel(380,380,160,10)
        sprite_externalWall_Btunnel.add(Wall28)

        Wall29 = makeExternalWallBTunnel(380,420,160,10)
        sprite_externalWall_Btunnel.add(Wall29)


        return sprite_externalWall_Btunnel
        
    def ballSpeedLimits():
        #THIS IS FOR FIX POSSIBLE EXTREME SPEEDS
        #SPEED LIMITS-------------
        if ball.speed_x>=20:#BALLS X LIMITS POSITIVE
            ball.speed_x=20
        if ball2.speed_x>=20:
            ball2.speed_x=20
        if ball3.speed_x>=20:
            ball3.speed_x=20
        
        if ball.speed_x<=-20:#BALLS X LIMITS NEGATIVE
            ball.speed_x=-20
        if ball2.speed_x<=-20:
            ball2.speed_x=-20
        if ball3.speed_x<=-20:
            ball3.speed_x=-20

        if ball.speed_y>40:#BALLS Y LIMITS POSITIVE
            ball.speed_y=40
        if ball2.speed_y>40:
            ball2.speed_y=40
        if ball3.speed_y>40:
            ball3.speed_y=40

        if ball.speed_y<-40:#BALLS Y LIMITS POSITIVE
            ball.speed_y=-40
        if ball2.speed_y<-40:
            ball2.speed_y=-40
        if ball3.speed_y<-40:
            ball3.speed_y=-40
        #SPEED LIMITS-------------

    def ballsJoinBigTunnel(moveLeftTunnel,moveLeftTunnel2,moveLeftTunnel3,moveRigthTunnel,moveRigthTunnel2,moveRigthTunnel3):
        #WHEN THE BALLS JOIN ON THE BIG TUNNEL , THEY USE BOOLEAN VARIABLES TO SELECT THE DIRECTION OF THE BALL, 2 BOOLEANS FOR EACH BALL (moveLeftTunnel,moveRigthTunnel)
        #ball1 , JOIN ON BIG TUNNEL-------------------------------------------------------------------------------
        if (ball.rect.x>=345 and ball.rect.x<=386 and ball.rect.y>=380 and ball.rect.y<=410 and moveRigthTunnel):
            print("CHANGE DIRECTIONN---------------------------------------------------------1")
            ball.speed_x=6
            
        if ball.speed_x>0:
            moveLeftTunnel=False
        else:
            moveLeftTunnel=True

        if (ball.rect.x>=534 and ball.rect.x<=560 and ball.rect.y>=380 and ball.rect.y<=410 and moveLeftTunnel):
            print("CHANGE DIRECTIONN---------------------------------------------------------1")
            ball.speed_x=-6
            moveRigthTunnel=False
        
        if ball.speed_x<0:
            moveRigthTunnel=False
        else:
            moveRigthTunnel=True

        #ball2 , JOIN ON BIG TUNNEL-------------------------------------------------------------------------------
        if (ball2.rect.x>=345 and ball2.rect.x<=386 and ball2.rect.y>=380 and ball2.rect.y<=410 and moveRigthTunnel2):
            print("CHANGE DIRECTIONN---------------------------------------------------------2")
            ball2.speed_x=6
            
        if ball2.speed_x>0:
            moveLeftTunnel2=False
        else:
            moveLeftTunnel2=True

        if (ball2.rect.x>=534 and ball2.rect.x<=560 and ball2.rect.y>=380 and ball2.rect.y<=410 and moveLeftTunnel2):
            print("CHANGE DIRECTIONN---------------------------------------------------------2")
            ball2.speed_x=-6
            moveRigthTunnel2=False
        
        if ball2.speed_x<0:
            moveRigthTunnel2=False
        else:
            moveRigthTunnel2=True

        #ball3 , JOIN ON BIG TUNNEL-------------------------------------------------------------------------------
        if (ball3.rect.x>=345 and ball3.rect.x<=386 and ball3.rect.y>=380 and ball3.rect.y<=410 and moveRigthTunnel3):
            print("CHANGE DIRECTIONN---------------------------------------------------------3")
            ball3.speed_x=6
            
        if ball3.speed_x>0:
            moveLeftTunnel3=False
        else:
            moveLeftTunnel3=True

        if (ball3.rect.x>=534 and ball3.rect.x<=560 and ball3.rect.y>=380 and ball3.rect.y<=410 and moveLeftTunnel3):
            print("CHANGE DIRECTIONN---------------------------------------------------------3")
            ball3.speed_x=-6
            moveRigthTunnel3=False
        
        if ball3.speed_x<0:
            moveRigthTunnel3=False
        else:
            moveRigthTunnel3=True
    
        return moveLeftTunnel,moveLeftTunnel2,moveLeftTunnel3,moveRigthTunnel,moveRigthTunnel2,moveRigthTunnel3

    def incrementGrav(points,old_points,cont):
        #INCREMENT GRAVITY EVERY X750 POINTS , LIMIT ON +6 FOR BE PLAYEABLE , COMPARE THE OLD POINTS WITH ACUTAL POINTS FOR FIX ERRORS.
        if points%750==0 and points>0 and not(old_points==points):
            old_points=points
            cont+=1
            print(cont)
            if cont > 6:
                cont=6
            if ball.rect.x<700:
                ball.speed_y +=cont
                ball2.speed_y +=cont
                ball3.speed_y +=cont

                ball.speed_x +=cont
                ball2.speed_x +=cont
                ball3.speed_x +=cont

        return points,old_points,cont

    def gravityReset(lifes,points,cont):
        #RESET GRAVITY WHEN POINTS ARE 0 OR LIFES ARE < 0 (-1)
        if points==0 or lifes<0:
            cont=0
        return cont
        
    def securityTopBarriers():
        #THE SECURITY LIMITIS FOR THE BALLS ,SO THE BALLS DO NOT LEAVE THE BOARD
        #(--------------THIS IS FOR THE TOP WALL---------------)
        if ball.rect.top<10:
            ball.rect.y=11
            ball.speed_y*=-1

        if ball2.rect.top<10:
            ball2.rect.y=11
            ball2.speed_y*=-1

        if ball3.rect.top<10:
            ball3.rect.y=11
            ball3.speed_y*=-1

    def ballsJoinSmallTunnelSound():
        #SOUND FOR THE SAMLL TUNNEL
        #ballTunnel=mixer.Sound('sources/tunnelJoin.mp3')
        #ballTunnel.play()       
        #ballTunnel.set_volume(2)
        pass
    def ballsJoinSmallTunnel():
        #IF THE BALLS JOIN ON THE SMALL TUNNEL (RED) , HAS BEEN TELEPORT TO THE YELLOW TUNNEL.
        #------ONLY 1 DIRECTION RED--> YELLOW , NO YELLOW --> RED-----------
        if ball.rect.x>=420 and ball.rect.x<=465 and ball.rect.y <=35:
            print("BALL 1 JOIN")
            ballsJoinSmallTunnelSound()

            ball.rect.x=220
            ball.rect.y=500


        if ball2.rect.x>=420 and ball2.rect.x<=465 and ball2.rect.y <=35:
            print("BALL 2 JOIN")
            ballsJoinSmallTunnelSound()
            
            ball2.rect.x=220
            ball2.rect.y=500

        if ball3.rect.x>=420 and ball3.rect.x<=465 and ball3.rect.y <=35:
            print("BALL 3 JOIN")
            ballsJoinSmallTunnelSound()
            
            ball3.rect.x=220
            ball3.rect.y=500

    def ballsAppearsSound():
        #BALLS APPEARS SOUND
        #ballsAparecen=mixer.Sound('sources/ballsAparecen.mp3')
        #ballsAparecen.play()       
        #ballsAparecen.set_volume(2)
        pass
    def ballsAppears(old_points2):
        #BALL 2 AND BALL 3 APPEARS EVERY X500 POINTS , ONLY IF YOU ARE PLAYING WITH THE PRINCIPAL BALL.
        #COMPARE THE OLD POINTS WITH ACUTAL POINTS FOR FIX ERRORS.
        #BALL 2 AND 3 STAY OUT OF THE SCREEN HEIGHT , FOR THIS USE > SCREEN_HEIGHT , AND TELEPORT IT TO THE ACTUAL COORDS.
        if points%500==0 and points>0 and not(old_points2==points) and ball2.rect.y>SCREEN_HEIGHT and ball3.rect.y>SCREEN_HEIGHT:
            old_points2=points
            ball2.rect.x=350
            ball2.rect.y=100
            ball2.speed_y=-4#SPEED Y
            ball2.speed_x=12#SPEED X

            ball3.rect.x=560
            ball3.rect.y=100
            ball3.speed_y=-4#SPEED Y
            ball3.speed_x=-12#SPEED X
            ballsAppearsSound()
        return old_points2

    def initialSound(startGame):
        #THE INITIAL SOUND WHEN THE PARTY STARTS , USE A BOOLEAN FOR IT (startGame)
        if startGame:
            #inicioP=mixer.Sound('sources/PartidaInicio.mp3')
            #inicioP.play(0)
            startGame=False
        return startGame

    def activateCloser(close):
        #ACTIVATE THE CLOSER WHEN PRINCIPAL BALL GO OUT OT THEM
        if ball.rect.right<705:
            close=True
        return close

    def closedSound():
        #cerRED=mixer.Sound('sources/cierre.mp3')
        #cerRED.play(1)       
        #cerRED.set_volume(4)
        pass
    def forcedImpacts(close,closed):
        #IF close its true , set forced collision to the red closer , for fix possible errors.
        if close:
            #BALL 1 FORCED IMPACTS
            if ball.rect.right>710:
                print("FORCE IMPACT")
                ball.rect.x=690
                ball.speed_x*=-1
            if ball.rect.x<200:
                ball.rect.x=210
                ball.speed_x*=-1
            if ball.rect.x>700:
                ball.rect.x=700
                ball.speed_x*=-1
            sprite_redCloser.draw(screen)

            if closed:#closed is for the close sound.
                closed=False
                closedSound()
        #BALL 2 FORCED IMPACTS
        if ball2.rect.right>710:
            print("FORCE IMPACT")
            ball2.rect.x=690
            ball2.speed_x*=-1
        if ball2.rect.x<200:
            ball2.rect.x=210
            ball2.speed_x*=-1
        if ball2.rect.x>700:
            ball2.rect.x=700
            ball2.speed_x*=-1

        #BALL 3 FORCED IMPACTS
        if ball3.rect.right>710:
            print("FORCE IMPACT")
            ball3.rect.x=690
            ball3.speed_x*=-1
        if ball3.rect.x<200:
            ball3.rect.x=210
            ball3.speed_x*=-1
        if ball3.rect.x>700:
            ball3.rect.x=700
            ball3.speed_x*=-1
        return closed

    def pushOutBall():
        #PULL PRINCIPAL BALL OUT OF THE LAUNCHER
        if ball.rect.x>700 and ball.rect.y<=11:
            ball.speed_y=-1
            randomA = random.randint(14,16)
            ball.speed_x=-randomA

    def noBallOutLauncher():
        #IF THE PRINCIPAL (MAIN) BALL DONT LEAVE THE LAUNCHER , THE Y SPEED IS 0
        if ball.rect.x>700 and ball.rect.y>=720:
            ball.rect.y=720
            ball.speed_y=0

    def printSpriteGroups(spriteBalls,sprite_white_bumpers,spriteWalls,spriteexternal_wallerior,sprite_topWalls,spriteLateral_StickWalls,sprite_top_pipe,sprite_bottom_pipe,sprite_internalWall_Btunnel,sprite_externalWall_Btunnel):
        #DRAW THE SPRITE GROUPS
        spriteBalls.draw(screen)
        sprite_white_bumpers.draw(screen)
        spriteWalls.draw(screen)
        spriteexternal_wallerior.draw(screen)
        sprite_topWalls.draw(screen)
        spriteLateral_StickWalls.draw(screen)
        sprite_top_pipe.draw(screen)
        sprite_bottom_pipe.draw(screen)
        sprite_internalWall_Btunnel.draw(screen)
        sprite_externalWall_Btunnel.draw(screen)

    def printCristalBigTunnel():
        #PRINT THE BIG TUNNEL IMAGE ON THE BOARD
        bigTunnel=pygame.image.load("images/tuboGrandeC.png").convert_alpha()
        screen.blit(bigTunnel,(365,383))

    def lifesLimiter(lifes):
        #LIFE LIMITS
        if lifes>=5:
            lifes=5
        return lifes

    def extraLifeBumperFunction(points,old_points3,activeCont,extraLife_bumper_X,secondsCont,sprite_extraLife_bumper,extraLife_bumper):

        #EVERY X1000 POINTS , APPEARS THE LIFE UP BUMPER , COMPARE THE OLD POINTS WITH ACUTAL POINTS FOR FIX ERRORS.
        #THAT USE activeCont FOR COUNT THE TIME , WHEN IT START TO COUNT , PUT THE EXTRA LIFE BUMPER ON THE REAL POSITION .
        if (points%1000==0 and not(points==0) and not(old_points3==points)):
            activeCont=True
            old_points3=points
        if secondsCont==0:#RESET BUMPER LIFE UP COORDS
            extraLife_bumper_X=435

        if(activeCont):
            secondsCont+=1
            extraLife_bumper.rect.x=extraLife_bumper_X#SETTING THE COORDS ON THE TIME
            sprite_extraLife_bumper.draw(screen)#DRAW THE LIFE UP BUMPER

            if(secondsCont==300):#WHEN GOT 300 , CHANGE COORDS TO 99999.
                extraLife_bumper.rect.x=99999
                activeCont=False#RESET
                secondsCont=0#RESET

        return points,old_points3,activeCont,extraLife_bumper_X,secondsCont,sprite_extraLife_bumper,extraLife_bumper

    def ballFallSouns():
        #LOSE BALLS SOUND
        #ballCae=mixer.Sound('sources/ballFall.mp3')
        #ballCae.play()       
        #ballCae.set_volume(0.6)
        pass

    def noBallsResetGame(lifes,closed,startGame,close,points,contMissions,nMission):
        #RESET THE GAME , WHEN YOU DONT HAV ANY BALL ON THE GAME , OR LOSE ALL LIFES.
        if ball.rect.y >= SCREEN_HEIGHT and ball2.rect.y >= SCREEN_HEIGHT and ball3.rect.y >= SCREEN_HEIGHT:
            ball.speed_x=0
            ball.speed_y=0
            ball.rect.x=720
            ball.rect.y=20

            ball2.rect.x=999999
            ball2.rect.y=999999

            ball3.rect.y=999999
            ball3.rect.y=999999

            ball2.speed_x=0
            ball2.speed_y=0

            ball3.speed_x=0
            ball3.speed_y=0
            
            lifes-=1
            print("Ball FALL")
            ballFallSouns()
            closed=True#CLOSED TRUE FOR OPEN AGAIN THE RED CLOSER
            
            time.sleep(1)#SLEEP 1 SECOND

            if lifes <0:#LIFES OUT
                lifes=5
                points=0
                startGame=True#RESET
                closed=True#RESET
                contMissions=0
                nMission=random.randint(points,points+2000)
            close=False#RESET

        return lifes,closed,startGame,close,points,contMissions,nMission


    def diagonalLines():
        #DRAW THE DIAGONAL LINES NEAR TO STICKS
        pygame.draw.line(screen, (BLUE), (250,700), (315, 755))
        pygame.draw.line(screen, (BLUE), (660, 700), (595,755))

    def lifesUpSound():
        #SOUND FOR THE EXTRA LIFE BUMPER IMPACT , OR LIFE UP
        #lifesUp=mixer.Sound('sources/lifeUp.mp3')
        #lifesUp.play(2)       
        #lifesUp.set_volume(2)
        pass

    def mainTheme():
        #THE MAIN THEME
        mixer.music.load('sources/pinball.mp3')
        mixer.music.play(-1)#MUSIC ON LOOP (-1)
        pygame.mixer.music.set_volume(0.4)

    def moveHacks(moveHack):
        #MOVE HACKS , ENABLE MOVE THE PRINCIPAL BALL (ONLY THE PRINCIPAL) TO RIGTH OR LEFT
        keyPressed = pygame.key.get_pressed()  

        if keyPressed[pygame.K_d]:
            if keyPressed[pygame.K_e]:
                moveHack=True
        return moveHack

    def fullLifes(lifes):
        #FULL LIFES HACKS , GIVE YOU THE MAX AOUNT POSSIBLE OF LIFES
        keyPressed = pygame.key.get_pressed()  

        if keyPressed[pygame.K_f]:
            if keyPressed[pygame.K_u]:
                lifes=5
        return lifes

    def missions(nMission,points,contMission):
        #IF THE ACTUAL POINTS IS > OR EUQUALS TO nMission , USE randomPoint , FOR GET EXTRA POINTS!
        if(nMission<=points):
            contMission+=1#+1 MISSION COMPLETES FOR PRINT
            nMission=random.randint(points,points+2000)#THE NEXT RANDOM MISSION
            randomPoint=random.randint(1,3)
            #POSSIBLE EXTRA POINTS WHEN COMPLETE IT
            if(randomPoint==1):
                points+=25
            elif(randomPoint==2):
                points+=50
            elif(randomPoint==2):
                points+=100
        return nMission,points,contMission
    #--------------------------------------------FUNCTIONS--END------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------


    #--------------------------------------------PYGAME-START-------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------
    # INIT PYGAME
    pygame.init()

    # MAKING 1000x900 Screen
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    
    # Set the window title
    pygame.display.set_caption('PINBALL - 1 DAM - DAVID MF')

    #SPRITE LISTS
    spriteBalls = pygame.sprite.Group()
    spriteWalls = pygame.sprite.Group()
    sprite_topWalls= pygame.sprite.Group()
    sprite_white_bumpers = pygame.sprite.Group()
    spriteLeftStick = pygame.sprite.Group()
    spriteRigthStick = pygame.sprite.Group()
    spriteexternal_wallerior = pygame.sprite.Group()
    sprite_redCloser = pygame.sprite.Group()
    spriteLateral_StickWalls = pygame.sprite.Group()
    sprite_extraLife_bumper = pygame.sprite.Group()
    sprite_top_pipe = pygame.sprite.Group()
    sprite_bottom_pipe = pygame.sprite.Group()
    sprite_internalWall_Btunnel = pygame.sprite.Group()
    sprite_externalWall_Btunnel = pygame.sprite.Group()

    #COUNTS---------------------------------
    cont=0#GRVITY COUNT
    old_points=0#FOR INCREMENT GRAVITY ON X750 POINTS
    old_points2=0#FOR BALLS APPEARS ON X500 POINTS
    old_points3=0#FOR BUMPER LIFE UP ON X1000 POINTS
    #COUNTS---------------------------------
    #POINTS AND LIFES
    points=0
    lifes=3

    #HACKS-VAIRABLES
    moveHack=False

    #MISSIONS
    nMission= random.randint(100,1000)
    contMission=0
    #LOAD THE MAIN THEME
    mainTheme()



    #MAKING WALLS , BUMPERS , STICKS FOR SPRITE GROUPS
    spriteWalls = makeNormalWalls(spriteWalls)
    spriteexternal_wallerior = makeExternalWalls(spriteexternal_wallerior)
    sprite_topWalls = makeTopWalls(sprite_topWalls)
    sprite_redCloser = makeRedClosers(sprite_redCloser)
    spriteLateral_StickWalls = makeLateralStickWalls(spriteLateral_StickWalls)
    sprite_white_bumpers = makeBumpers(sprite_white_bumpers)
    sprite_internalWall_Btunnel = makeInternalWallBigTunnel(sprite_internalWall_Btunnel)
    sprite_externalWall_Btunnel = makeExternalWallsBigTunnel(sprite_externalWall_Btunnel)

    #BACKGROUND IMAGE
    bg_img = pygame.image.load('images/base6.png').convert_alpha()
    bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH,SCREEN_HEIGHT))

    #CLOSERS
    close = False#red closer
    closed=True#force impacts

    #START GAME, BOOLEAN
    startGame=True

    #BUMPER LIFE UP X
    extraLife_bumper_X=435


    #BOOLEANS FOR THE HIT WALLS ON THE BIG TUNNEL , FOR DECIDE THE MOVEMENT OF THE BALL WHEN IT JOIN. 2 FOR EACH BALL.
    moveRigthTunnel=True
    moveLeftTunnel=True

    moveRigthTunnel2=True
    moveLeftTunnel2=True

    moveRigthTunnel3=True
    moveLeftTunnel3=True


    # MAKING THE BALLS
    ball = makeBall(spriteBalls, 720, 20)
    ball2 = makeBall2(spriteBalls, 400, 999999)
    ball3 = makeBall3(spriteBalls,500,999999)

    #MAKING BUMPER LIFE UP
    extraLife_bumper = makeExtraLifeBumper(sprite_extraLife_bumper,99999,340)

    #MAKING TOP AND BOTTOM PIPE
    topPipe = makeTopPipe(sprite_top_pipe,435,10)
    bottomPipe = makeBottomPipe(sprite_bottom_pipe,210,500)

    #SET THE CURRENT FPS LIMITS
    fps = pygame.time.Clock()

    #INITIAL STATE FOR BUMPER LIFE UP CONTS
    activeCont=False
    secondsCont=0

    #RUNNING TRUE , THE GAME BOOLEAN
    isRunning = True


    while isRunning:

        #SPEED LIMITS-------------
        ballSpeedLimits()
        #SPEED LIMITS-------------

        #HACKS
        moveHack=moveHacks(moveHack)
        lifes=fullLifes(lifes)
        #SCREEN FILLS , AND BACKGROUND POSITION
        screen.fill(BLACK)
        screen.blit(bg_img,(0,0))

        #EXTRA LIFE BUMPER (BUMPER LIFE UP) APPEARS
        points,old_points3,activeCont,extraLife_bumper_X,secondsCont,sprite_extraLife_bumper,extraLife_bumper=extraLifeBumperFunction(points,old_points3,activeCont,extraLife_bumper_X,secondsCont,sprite_extraLife_bumper,extraLife_bumper)
        
        #LIFES LIMITS
        lifes=lifesLimiter(lifes)
        
        #MANAGE EVENTS
        isRunning = manageEvents(ball, isRunning,moveHack)

        #INC GRAVITY X750
        points,old_points,cont=incrementGrav(points,old_points,cont)
    
        #BALLS JOIN ON THE BIG TUNNEL
        moveLeftTunnel,moveLeftTunnel2,moveLeftTunnel3,moveRigthTunnel,moveRigthTunnel2,moveRigthTunnel3=ballsJoinBigTunnel(moveLeftTunnel,moveLeftTunnel2,moveLeftTunnel3,moveRigthTunnel,moveRigthTunnel2,moveRigthTunnel3)

        #UPDATE BALL/S
        points,lifes,extraLife_bumper_X,moveLeftTunnel,moveLeftTunnel2,moveLeftTunnel3,moveRigthTunnel,moveRigthTunnel2,moveRigthTunnel3=updateball(moveLeftTunnel,moveLeftTunnel2,moveLeftTunnel3,moveRigthTunnel,moveRigthTunnel2,moveRigthTunnel3,extraLife_bumper_X,lifes,ball,ball2,ball3,sprite_externalWall_Btunnel,sprite_internalWall_Btunnel,sprite_extraLife_bumper,spriteWalls,spriteLateral_StickWalls,sprite_topWalls,sprite_white_bumpers,spriteLeftStick,spriteRigthStick,spriteexternal_wallerior,sprite_redCloser,points,cont)

        #RESET GRAVITY WHEN POINTS ITS 0 OR LIFES < 0
        cont=gravityReset(lifes,points,cont)

        #FOR PREVENTS ERRORS WHIT BALLS OUT OF THE TOP WALL
        securityTopBarriers()
        
        #BALLS 1 2 3 JOIN ON THE SMALL TUNNEL/S
        ballsJoinSmallTunnel()
    
        #BALLS 2 AND 3 APPEARS X500 POINTS
        old_points2=ballsAppears(old_points2)

        #IF START GAME IS TRUE , PLAY THE INITIAL SOUND
        startGame=initialSound(startGame)

        #ACTIVATE LACUNCHER CLOSER
        close=activateCloser(close)
        
        #FORCED IMPACTS , FOR PREVENTS ERRORS
        closed=forcedImpacts(close,closed)
    
        #PULL OUT OF LAUNCHER la ball principal
        pushOutBall()

        #FOR PREVENTS THE FALL OF THE MAIN BALL ON THE LAUNCHER
        noBallOutLauncher()

        #STICKS DRAWS
        spriteLeftStick=LeftStick(screen,spriteLeftStick)
        spriteRigthStick=RigthStick(screen,spriteRigthStick)

        #PRINT OF DIAGONAL LINES NEAR TO STICKS
        diagonalLines()
        
        #PRINT SPRITE GROUPS
        printSpriteGroups(spriteBalls,sprite_white_bumpers,spriteWalls,spriteexternal_wallerior,sprite_topWalls,spriteLateral_StickWalls,sprite_top_pipe,sprite_bottom_pipe,sprite_internalWall_Btunnel,sprite_externalWall_Btunnel)

        #MISSIONS FUNCTION
        nMission,points,contMission=missions(nMission,points,contMission)

        #TEXT PRINTS
        printScore(screen,points)
        printLife(screen,lifes)
        printLevel(screen)
        printControls0(screen)
        printGravedad(screen,cont)
        printControls1(screen)
        printControls2(screen)
        printMission(screen,nMission)
        printCompleteMissions(screen,contMission)


        #IF ALL THE BALLS FALL , RESET THE GAME
        lifes,closed,startGame,close,points,contMission,nMission=noBallsResetGame(lifes,closed,startGame,close,points,contMission,nMission)

        #THE NEXT TWO LINES , DRAW A BLUE AREA ON THE HITBOX AREA FOR THE BIG TUNNEL , FOR TESTING
        #pygame.draw.rect(screen, BLUE,(534,400,26,10))
        #pygame.draw.rect(screen, BLUE,(360,400,26,10))

        #BIG TUNNEL PRINT
        printCristalBigTunnel()
        
        #pygame.time.delay(5)
        #UPDATE THE SCREEN
        pygame.display.flip()
        
        #THE FPS LIMITS
        #fps.tick(60)
                    

    #--------------------------------------------PYGAME-END----------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------
        await asyncio.sleep(0)
        
asyncio.run(main())
