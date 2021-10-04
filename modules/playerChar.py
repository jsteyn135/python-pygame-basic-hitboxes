import pygame

class playerChar():


    def __init__(self,pygameObj,x=0,y=0):
        self.x = x
        self.y = y
        self.pygame = pygameObj
        self.image_path = R"imgs\tiles\rabbit.gif"
        self.img = self.pygame.image.load(self.image_path)
        self.hitbox = self.img.get_rect()
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        # 32 wide x 55 high        

        self.velocity_x = 0
        self.velocity_y = 0


    def player_move(self,can_jump):
                
        if(abs(self.velocity_x) > 3):# this number here (3) prevents the player from going infinite speeds
            if(self.velocity_x>0):#if its positive
                self.velocity_x -=1
            elif(self.velocity_x<0):#if its negative
                self.velocity_x +=1

        if(self.velocity_x != 0):# this is like the friction
            if(self.velocity_x>0):#if its positive
                self.velocity_x -= 0.0625
            elif(self.velocity_x<0):#if its negative
                self.velocity_x += 0.0625
                

       
        if(can_jump[0]==1):
            self.velocity_y = 0# floating into the ground issue solved with this
            self.velocity_y -= 0.5  
        else:
            self.velocity_y+=0.125

        keyboard_input = pygame.key.get_pressed()# move left or right
        if(keyboard_input[pygame.K_d]):
            self.velocity_x+=0.25  #0.25
            
        if(keyboard_input[pygame.K_a]):
            self.velocity_x-=0.25

        if(keyboard_input[pygame.K_SPACE]):# jump
            if(can_jump[0]==1):
                self.velocity_y -=6
                can_jump[0] =0
            else:
                pass
        
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y
        
        self.hitbox.x = self.x
        self.hitbox.y = self.y
