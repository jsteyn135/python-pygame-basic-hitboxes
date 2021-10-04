import pygame
import time

from modules import playerChar as pc
from modules import collide_block as cb

def main():

    pygame.init()
    screen = (800,600)
    game_window = pygame.display.set_mode(screen)
    game_window.fill((38,237,229))
    pygame.display.flip()
    
    
    game_clock = pygame.time.Clock()
    
    # hard coded blocks/terrain
    collide_block0 = cb.collide_block(pygame,72,420)
    collide_block = cb.collide_block(pygame,200,420)
    collide_block3 = cb.collide_block(pygame,264,420)
    collide_block5 = cb.collide_block(pygame,328,420)
    collide_block6 = cb.collide_block(pygame,392,420)
    collide_block7 = cb.collide_block(pygame,456,420)
    collide_block8 = cb.collide_block(pygame,520,420)
    collide_block9 =  cb.collide_block(pygame,136,420)
    collide_block10 = cb.collide_block(pygame,456,356)
    collide_block11 = cb.collide_block(pygame,456,292)
    collide_block12 = cb.collide_block(pygame,456,228)
    collide_block13 = cb.collide_block(pygame,200,282)
    collide_block14 = cb.collide_block(pygame,264,282)

    block_list = []
    block_list.append(collide_block)
    block_list.append(collide_block3)
    block_list.append(collide_block5)
    block_list.append(collide_block6)
    block_list.append(collide_block7)
    block_list.append(collide_block8)
    block_list.append(collide_block9)
    block_list.append(collide_block10)
    block_list.append(collide_block11)
    block_list.append(collide_block12)
    block_list.append(collide_block13)
    block_list.append(collide_block14)
    block_list.append(collide_block0)
    
    player = pc.playerChar(pygame,200,270)

    game_window.fill((10,100,40))

    grounded = False
    can_jump = [0]
    touching_top_block = [0]
    projectiles = []
    while(True):
        
        game_clock.tick(120)
        game_window.fill((3,245,229))
        
        player.y += 1
        player.hitbox.y +=1

        for i in block_list:
            game_window.blit(i.img,(i.x,i.y))
        
        
        player.player_move(can_jump)
        touching_top_block[0] = 0
        for i in block_list:
            if(player.hitbox.colliderect(i.up)):
                can_jump[0] =  1

                player.y -=1
                player.hitbox.y -=1
                
                touching_top_block[0] = 1
                
            if(player.hitbox.colliderect(i.left)):
                player.velocity_x -= 1
                player.velocity_y = 0
                
                continue
            if(player.hitbox.colliderect(i.right)):
                player.velocity_x += 1
                player.velocity_y = 0
                
                continue
            if(player.hitbox.colliderect(i.down)):
                player.velocity_y +=2
                continue
        if(touching_top_block[0] == 0):
            can_jump[0] = 0

        
        game_window.blit(player.img,(player.x,player.y)) 
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break


main()












