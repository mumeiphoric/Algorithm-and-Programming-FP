'''

DEFAULT SETTINGS

'''

import pygame
from map import layout

pygame.init()

pygame.display.set_caption('PACMAN')

# GAME WINDOW SIZE
WIDTH = 900
HEIGHT = 950
game_window = pygame.display.set_mode([WIDTH, HEIGHT])

# REGULATING FRAMERATE
timer = pygame.time.Clock()
fps = 60

# FONT SETTINGS
font = pygame.font.Font(f'fonts/Minecraft.ttf', 20)
font_small = pygame.font.Font(f'fonts/Minecraft.ttf', 30) 
font_big = pygame.font.Font(f'fonts/Minecraft.ttf', 100)  

# MAP
map = layout

# INITIAL PACMAN POSITION
pacman_x = 430 # x coords on map
pacman_y = 660 # y coords on map
direction = 0 # initially facing right

# INITIAL GHOSTS POSITIONS
red_ghost_x = 430 # x coords on map
red_ghost_y = 325 # y coords on map
red_ghost_direction = 0 # initially facing right

cyan_ghost_x = 380 # x coords on map
cyan_ghost_y = 410 # y coords on map
cyan_ghost_direction = 2 # initially facing up

pink_ghost_x = 430 # x coords on map
pink_ghost_y = 410 # y coords on map
pink_ghost_direction = 2 # initially facing up

orange_ghost_x = 480 # x coords on map
orange_ghost_y = 410 # y coords on map
orange_ghost_direction = 2 # initially facing up

# POWER-UP BLINKS
cycle = 0 # reset animation
blink = False # power ups don't blink initially

# PACMAN MOVEMENT
valid_turns = [False, # Right
               False, # Left
               False, # Up
               False] # Down

direction_cmd = 0 # direction initially facing right (holds down player direction)
player_speed = 2

# INITIAL SCORE SETTING
score = 0

# INITIAL POWER-UP SETTINGS
powerup = False
power_cycle = 0 

# INITIAL GHOST SETTINGS
killed_ghosts = [False, False, False, False] # No ghosts killed initially
targets = [(pacman_x, pacman_y), (pacman_x, pacman_y), (pacman_x, pacman_y), (pacman_x, pacman_y)] # Each ghosts' initial targets (pacman)

red_ghost_dead = False
cyan_ghost_dead = False
orange_ghost_dead = False
pink_ghost_dead = False

red_ghost_at_spawn = False
cyan_ghost_at_spawn = False
orange_ghost_at_spawn = False
pink_ghost_at_spawn = False

moving = False
ghost_speeds = [2, 2, 2, 2]

# START COUNTDOWN
start_timer = 0

#INITIAL LIVES
lives = 3

# GAME OVER
game_over = False
game_won = False
