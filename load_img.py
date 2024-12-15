'''

MANAGING IMAGES

'''

import pygame

pygame.init()

pacman_imgs = [] # To hold the loaded images

# PACMAN IMAGES
for i in range(1, 5): # Goes through images 1-4
    pacman_imgs.append(pygame.transform.scale(pygame.image.load(f'images/pacman_imgs/{i}.png'), # Loads images
                                              (45, # Width
                                               45))) # Height
    # Loads the images and then scales them accordingly

# GHOST IMAGES
red_ghost_img = pygame.transform.scale(pygame.image.load(f'images/ghost_images/red.png'), (45, 45))
pink_ghost_img = pygame.transform.scale(pygame.image.load(f'images/ghost_images/pink.png'), (45, 45))
cyan_ghost_img = pygame.transform.scale(pygame.image.load(f'images/ghost_images/cyan.png'), (45, 45))
orange_ghost_img = pygame.transform.scale(pygame.image.load(f'images/ghost_images/orange.png'), (45, 45))


# GHOST VULNERABLE TO PLAYER
vulnerable_img = pygame.transform.scale(pygame.image.load(f'images/ghost_images/vulnerable.png'), (45, 45))

# GHOST RUNNING BACK TO SPAWN
dead_img = pygame.transform.scale(pygame.image.load(f'images/ghost_images/dead.png'), (45, 45))

# LIFE IMAGES
life_img = pygame.transform.scale(pygame.image.load(f'images/lives.png'), (45, 45))
