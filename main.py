'''

 PACMAN GAME 

''' 

from map import layout
import pygame
import math
from load_img import *
from settings import *

pygame.init()

'''
-------- GAME DISPLAY FUNCTIONS --------
'''

def draw_ui():
    
    # SCORE TEXT: Bottom right of window
    score_text = font.render(f'SCORE: {score}', True, '#FFFFE0')
    game_window.blit(score_text, (750, 920))

    # LIFE IMAGES: Bottom left of window
    for i in range(lives):
        game_window.blit(pygame.transform.scale(life_img, (45, 45)), (50 + i * 40, 912))

    if start_timer < 180 and not game_over and not game_won: # 3 second delay before starting game
        start_text = font_small.render('READY?', True, 'yellow') # Displays "READY?" text during those 3 seconds
        game_window.blit(start_text, (390, 505))

    # GAME OVER SCREEN
    if game_over:
        game_window.fill('black')
        gameover_text = font_big.render('GAME OVER!', True, 'yellow')
        game_window.blit(gameover_text, (145, 450))
        restart_text = font_small.render('Press Space to Restart', True, 'yellow')
        game_window.blit(restart_text, (280, 550))

    # VICTORY SCREEN
    if game_won:
        game_window.fill('black')
        win_text = font_big.render('YOU WON!', True, 'yellow')
        game_window.blit(win_text, (190, 400))
        restart_text = font_small.render('Press Space to Restart', True, 'yellow')
        game_window.blit(restart_text, (280, 500))

def draw_map():
    tiles_y = ((HEIGHT - 50) // 32)
    # 50 -> is space reserved for update_score at the bottom
    # 32 -> is the number of tiles going vertically

    tiles_x = (WIDTH // 30)
    # 30 -> is the number of tiles going horizontally

    for row in range(len(map)): # Go through every row
        for col in range(len(map[row])): # Go through every column in row

            # No need to define # because it's just hollow

            if map[row][col] == ' ': # The little dots
                pygame.draw.circle(game_window, '#FFFFE0', 
                                   (col * tiles_x + (0.5 * tiles_x), # x coordinate
                                    row * tiles_y + (0.5 * tiles_y)), # y coordinate
                                    4) # radius (size of dot)
                
                                    # col * tiles_x puts little dots in every column in the rows (each tile)
                                    # + (0.5 * tiles_y) centers it in each tile

            if map[row][col] == 'o' and not blink: # The big dots (power ups)
                pygame.draw.circle(game_window, '#FFFFE0', (col * tiles_x + (0.5 * tiles_x), # x coordinate
                                                          row * tiles_y + (0.5 * tiles_y)), # y coordinate
                                                          10) # radius (size of dot)
            
            if map[row][col] == '|': # Borders: Vertical line going down the center of each tile
                pygame.draw.line(game_window, 'blue', (col * tiles_x + (0.5 * tiles_x), # x coord (start)
                                                      row * tiles_y), # y coord (start)
                                                      (col * tiles_x + (0.5 * tiles_x), # x coord (end)
                                                       row * tiles_y + tiles_y), # y coord (end)
                                                       3) # Line thickness
            
            if map[row][col] == '=': # Borders: Horizontal line going through the center of each tile
                pygame.draw.line(game_window, 'blue', (col * tiles_x, # x coord (start)
                                                      row * tiles_y + (0.5 * tiles_y)), # y coord (start)
                                                      (col * tiles_x + tiles_x, # x coord (end)
                                                       row * tiles_y + (0.5 * tiles_y)), # y coord (end)
                                                       3) # Line thickness
            
            if map[row][col] == '2': # Borders: Top right corner piece
                pygame.draw.arc(game_window, 'blue', [(col * tiles_x - (tiles_x * 0.4)) - 2, 
                                                     # x coord (start) of rectangle (top left corner)
                                                     # uses - to shift rectangle to the left 
                # Arc is drawn inside a rectangle
                                                     (row * tiles_y + (0.5 * tiles_y)), 
                                                     # y coord (start) of rectangle (top left corner)
                                                     # used + to shift rectangle downwards

                                                     tiles_x, # Width of rectangle
                                                     tiles_y], # Height of rectangle

                                                     0, # Start angle
                                                     math.pi / 2, # End angle
                                                     3) # Line thickness
            
            if map[row][col] == '1': # Borders: Top left corner piece
                pygame.draw.arc(game_window, 'blue', [(col * tiles_x + (tiles_x * 0.5)), 
                                                     # x coord (start) of rectangle (top left corner)
                                                     # uses + to shift rectangle to the right 
                # Arc is drawn inside a rectangle
                                                     (row * tiles_y + (0.5 * tiles_y)), 
                                                     # y coord (start) of rectangle (top left corner)
                                                     # used + to shift rectangle downwards 
                                                     
                                                     tiles_x, # Width of rectangle
                                                     tiles_y], # Height of rectangle

                                                     # Rectangle is drawn, moving on to arc

                                                     math.pi / 2, # Start angle
                                                     math.pi, # End angle
                                                     3) # Line thickness
            
            if map[row][col] == '3': # Borders: Bottom left corner piece
                pygame.draw.arc(game_window, 'blue', [(col * tiles_x + (tiles_x * 0.5)), 
                                                     # x coord (start) of rectangle (top left corner)
                                                     # used + to shift rectangle to the right 

                                                     (row * tiles_y - (0.4 * tiles_y)), 
                                                     # y coord (start) of rectangle (top left corner)
                                                     # used - to shift rectangle upwards

                                                     # Rectangle is drawn, moving on to arc

                                                     tiles_x, # Width of rectangle
                                                     tiles_y], # Height of rectangle

                                                     math.pi, # Start angle
                                                     3 * math.pi / 2, # End angle
                                                     3) # Line thickness
            
            if map[row][col] == '4':  # Borders: Bottom right corner piece
                pygame.draw.arc(game_window, 'blue', [(col * tiles_x - (tiles_x * 0.4)) - 2, 
                                                     # x coord (start) of rectangle (top left corner)
                                                     # used - to shift rectangle to the left 

                                                     (row * tiles_y - (0.4 * tiles_y)), 
                                                     # y coord (start) of rectangle (top left corner)
                                                     # used - to shift rectangle upwards

                                                     # Rectangle is drawn, moving on to arc

                                                     tiles_x, # Width of rectangle
                                                     tiles_y], # Height of rectangle

                                                     3 * math.pi / 2, # Start angle
                                                     2 * math.pi, # End angle
                                                     3) # Line thickness
            
            if map[row][col] == '-': # Ghost gate
                pygame.draw.line(game_window, '#FFFFE0', (col * tiles_x, # x coord (start)
                                                        row * tiles_y + (0.5 * tiles_y)), # y coord (start)
                                                        (col * tiles_x + tiles_x, # x coord (end)
                                                         row * tiles_y + (0.5 * tiles_y)), # y coord (end)
                                                         3) # Line thickness

'''
-------- PACMAN CONTROL FUNCTIONS -------
'''

def draw_pacman():
    
    # FACING RIGHT
    if direction == 0:
        game_window.blit(pacman_imgs[cycle // 8], (pacman_x, pacman_y)) # cycle used to control which frame of the animation is displayed

    # FACING LEFT
    elif direction == 1:  # Flips the image to the left
        game_window.blit(pygame.transform.flip(pacman_imgs[cycle // 8],
                                               True, # Flips in the x direction
                                               False), # Flips in the y direction
                                               (pacman_x, pacman_y)) # Pacman position
    
    # FACING UP
    elif direction == 2:
        game_window.blit(pygame.transform.rotate(pacman_imgs[cycle // 8], 
                                                 90), # Rotates 90 degrees to the left
                                                 (pacman_x, pacman_y)) # Pacman position
    
    # FACING DOWN
    elif direction == 3:
        game_window.blit(pygame.transform.rotate(pacman_imgs[cycle // 8], 
                                                 -90), # Rotates 90 degrees to the right
                                                 (pacman_x, pacman_y)) # Pacman position

def pacman_collisions(update_score, power, power_count, kill_ghosts):

    tiles_y = ((HEIGHT - 50) // 32)
    # 50 -> is space reserved for update_score at the bottom
    # 32 -> is the number of tiles going vertically

    tiles_x = (WIDTH // 30)
    # 30 -> is the number of tiles going horizontally

    if 0 < pacman_x < 870: # Checks when player is within the bounds of the map

        if map[center_actor_y // tiles_y][center_actor_x // tiles_x] == ' ': # Checks if the center is 1 on the map (meaning the pellet is eaten)
            map[center_actor_y // tiles_y][center_actor_x // tiles_x] = '#'  # Clears the dot (pellet) after it's eaten
            update_score += 10 # Adds 10 points after eating pellet

        if map[center_actor_y // tiles_y][center_actor_x // tiles_x] == 'o': # Checks if the center is 2 on the map (meaning the power-up is eaten)
            map[center_actor_y // tiles_y][center_actor_x // tiles_x] = '#'  # Clears the power-up after it's eaten
            update_score += 30 # Adds 30 points after power-up

            power = True # Gives you power after eating power-up
            power_count = 0 # Resets power-up counter after each power-up eaten

            # Default ghosts killed after eaten with power-up
            kill_ghosts = [False, False, False, False]
            
    return update_score, power, power_count, kill_ghosts

def pacman_position(pacmanx, pacmany):
    turns = [False, # Right
             False, # Left
             False, # Up
             False] # Down
            # Turns allowed

    tiles_y = ((HEIGHT - 50) // 32)
    # 50 -> is space reserved for update_score at the bottom
    # 32 -> is the number of tiles going vertically

    tiles_x = ((WIDTH // 30))
    # 30 -> is the number of tiles going horizontally

    safety_margin = 15
    # Assures movement is smooth (won't collide with empty space near borders)

    if pacmanx // 30 < 29: # Ensures Pacman stays in horizontal boundaries of the map by checking columns

        # Able to turn in the opposite direction
        if direction == 0:
            if map[pacmany // tiles_y][(pacmanx - safety_margin) // tiles_x] in [' ', 'o', '#']:
                turns[1] = True

        if direction == 1:
            if map[pacmany // tiles_y][(pacmanx + safety_margin) // tiles_x] in [' ', 'o', '#']:
                turns[0] = True

        if direction == 2:
            if map[(pacmany + safety_margin) // tiles_y][pacmanx // tiles_x] in [' ', 'o', '#']:
                turns[3] = True

        if direction == 3:
            if map[(pacmany - safety_margin) // tiles_y][pacmanx // tiles_x] in [' ', 'o', '#']:
                turns[2] = True

        # Able to turn up or down based on active direction
        if direction == 2 or direction == 3:
            if 12 <= pacmanx % tiles_x <= 18:
            # If the remainder is between 12 and 18 -> Roughly in the mid point of the tile
            # To make sure you can only turn when Pacman is in the center, to avoid going through walls

                if map[(pacmany + safety_margin) // tiles_y][pacmanx // tiles_x] in [' ', 'o', '#']:
                    turns[3] = True

                if map[(pacmany - safety_margin) // tiles_y][pacmanx // tiles_x] in [' ', 'o', '#']:
                    turns[2] = True

            if 12 <= pacmany % tiles_y <= 18:
                if map[pacmany // tiles_y][(pacmanx - tiles_x) // tiles_x] in [' ', 'o', '#']:
                    turns[1] = True
                if map[pacmany // tiles_y][(pacmanx + tiles_x) // tiles_x] in [' ', 'o', '#']:
                    turns[0] = True
        if direction == 0 or direction == 1:
            if 12 <= pacmanx % tiles_x <= 18:
                if map[(pacmany + tiles_y) // tiles_y][pacmanx // tiles_x] in [' ', 'o', '#']:
                    turns[3] = True
                if map[(pacmany - tiles_y) // tiles_y][pacmanx // tiles_x] in [' ', 'o', '#']:
                    turns[2] = True
            if 12 <= pacmany % tiles_y <= 18:
                if map[pacmany // tiles_y][(pacmanx - safety_margin) // tiles_x] in [' ', 'o', '#']:
                    turns[1] = True
                if map[pacmany // tiles_y][(pacmanx + safety_margin) // tiles_x] in [' ', 'o', '#']:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True

    return turns

def move_pacman(pacman_move_x, pacman_move_y):
    
    if direction == 0 and valid_turns[0]: # Moves Pacman to the left
        pacman_move_x += player_speed

    elif direction == 1 and valid_turns[1]: # Moves Pacman to the right
        pacman_move_x -= player_speed

    if direction == 2 and valid_turns[2]: # Moves Pacman up
        pacman_move_y -= player_speed

    elif direction == 3 and valid_turns[3]: # Moves Pacman down
        pacman_move_y += player_speed

    return pacman_move_x, pacman_move_y

'''
---- GHOST CONTROL FUNCTIONS & CLASS ----
'''

class Ghost:
    def __init__(self, ghostx, ghosty, target, speed, img, path, dead, at_spawn, id):
        
        # x and y coords of ghost (and determining the center of the ghost)
        self.ghost_x = ghostx
        self.ghost_y = ghosty
        self.center_actor_x = self.ghost_x + 22
        self.center_actor_y = self.ghost_y + 22

        # determines where the ghost goes
        self.target = target
        self.direction = path

        # speed of ghost movement
        self.speed = speed

        # ghost images
        self.img = img

        # when ghost is killed
        self.dead = dead

        # when ghost is at their spawn (in the middle box)
        self.in_spawn = at_spawn

        # to identify each individual ghost
        self.id = id

        # checking ghost position on board
        self.turns, self.in_spawn = self.pacman_collisions()

        # outline of ghost hit-box
        self.rect = self.draw()

    def draw(self): # Displaying different ghosts

        # NORMAL GHOST
        if (not powerup and not self.dead) or (killed_ghosts[self.id] and powerup and not self.dead):
            # if there's no power-up and the ghost isn't dead or ghost already killed during power-up, and isn't dead
            game_window.blit(self.img, (self.ghost_x, self.ghost_y))

        # VULNERABLE GHOST
        elif powerup and not self.dead and not killed_ghosts[self.id]: # power-up is active but ghost isn't dead
            game_window.blit(vulnerable_img, (self.ghost_x, self.ghost_y))

        # KILLED GHOST
        else:
            game_window.blit(dead_img, (self.ghost_x, self.ghost_y)) # otherwise, ghost is dead

        # Ghost Hit-box
        ghost_rect = pygame.rect.Rect((self.center_actor_x - 19, # x coord (start)
                                       self.center_actor_y - 19), # y coord (start)
                                       (40, 40)) # width and height
        return ghost_rect

    def pacman_collisions(self):
        
        tiles_y = ((HEIGHT - 50) // 32)
        # 50 -> is space reserved for update_score at the bottom
        # 32 -> is the number of tiles going vertically

        tiles_x = (WIDTH // 30)
        # 30 -> is the number of tiles going horizontally
        
        safety_margin = 15

        self.turns = [False, False, False, False]

        if 0 < self.center_actor_x // 30 < 29: # If within an occupiable tile

            # Ghosts can pass through 9 (their gate)

            # Going up (out of the gate)
            if map[(self.center_actor_y - safety_margin) // tiles_y][self.center_actor_x // tiles_x] == '-':
                self.turns[2] = True

            # Turn to left direction
            if map[self.center_actor_y // tiles_y][(self.center_actor_x - safety_margin) // tiles_x] in [' ', 'o', '#'] \
                    or (map[self.center_actor_y // tiles_y][(self.center_actor_x - safety_margin) // tiles_x] == '-' and (
                    self.in_spawn or self.dead)):
                self.turns[1] = True

            # Turn to right direction
            if map[self.center_actor_y // tiles_y][(self.center_actor_x + safety_margin) // tiles_x] in [' ', 'o', '#'] \
                    or (map[self.center_actor_y // tiles_y][(self.center_actor_x + safety_margin) // tiles_x] == '-' and (
                    self.in_spawn or self.dead)):
                self.turns[0] = True

            # Turn to down direction
            if map[(self.center_actor_y + safety_margin) // tiles_y][self.center_actor_x // tiles_x] in [' ', 'o', '#'] \
                    or (map[(self.center_actor_y + safety_margin) // tiles_y][self.center_actor_x // tiles_x] == '-' and (
                    self.in_spawn or self.dead)):
                self.turns[3] = True

            # Turn to up direction
            if map[(self.center_actor_y - safety_margin) // tiles_y][self.center_actor_x // tiles_x] in [' ', 'o', '#'] \
                    or (map[(self.center_actor_y - safety_margin) // tiles_y][self.center_actor_x // tiles_x] == '-' and (
                    self.in_spawn or self.dead)):
                self.turns[2] = True

            # Able to turn up or down based on active direction
            if self.direction == 2 or self.direction == 3:
                if 12 <= self.center_actor_x % tiles_x <= 18:

                    # Can turn down
                    if map[(self.center_actor_y + safety_margin) // tiles_y][self.center_actor_x // tiles_x] in [' ', 'o', '#'] \
                            or (map[(self.center_actor_y + safety_margin) // tiles_y][self.center_actor_x // tiles_x] == '-' and (
                            self.in_spawn or self.dead)):
                        self.turns[3] = True

                    # Can turn up
                    if map[(self.center_actor_y - safety_margin) // tiles_y][self.center_actor_x // tiles_x] in [' ', 'o', '#'] \
                            or (map[(self.center_actor_y - safety_margin) // tiles_y][self.center_actor_x // tiles_x] == '-' and (
                            self.in_spawn or self.dead)):
                        self.turns[2] = True

                if 12 <= self.center_actor_y % tiles_y <= 18:

                    # Can turn left
                    if map[self.center_actor_y // tiles_y][(self.center_actor_x - tiles_x) // tiles_x] in [' ', 'o', '#'] \
                            or (map[self.center_actor_y // tiles_y][(self.center_actor_x - tiles_x) // tiles_x] == '-' and (
                            self.in_spawn or self.dead)):
                        self.turns[1] = True

                    # Can turn right
                    if map[self.center_actor_y // tiles_y][(self.center_actor_x + tiles_x) // tiles_x] in [' ', 'o', '#'] \
                            or (map[self.center_actor_y // tiles_y][(self.center_actor_x + tiles_x) // tiles_x] == '-' and (
                            self.in_spawn or self.dead)):
                        self.turns[0] = True

            # Able to turn right or left based on active direction
            if self.direction == 0 or self.direction == 1:
                if 12 <= self.center_actor_x % tiles_x <= 18:

                    # Can turn down
                    if map[(self.center_actor_y + safety_margin) // tiles_y][self.center_actor_x // tiles_x] in [' ', 'o', '#'] \
                            or (map[(self.center_actor_y + safety_margin) // tiles_y][self.center_actor_x // tiles_x] == '-' and (
                            self.in_spawn or self.dead)):
                        self.turns[3] = True

                    # Can turn up
                    if map[(self.center_actor_y - safety_margin) // tiles_y][self.center_actor_x // tiles_x] in [' ', 'o', '#'] \
                            or (map[(self.center_actor_y - safety_margin) // tiles_y][self.center_actor_x // tiles_x] == '-' and (
                            self.in_spawn or self.dead)):
                        self.turns[2] = True

                if 12 <= self.center_actor_y % tiles_y <= 18:

                    # Can turn left
                    if map[self.center_actor_y // tiles_y][(self.center_actor_x - safety_margin) // tiles_x] in [' ', 'o', '#'] \
                            or (map[self.center_actor_y // tiles_y][(self.center_actor_x - safety_margin) // tiles_x] == '-' and (
                            self.in_spawn or self.dead)):
                        self.turns[1] = True

                    # Can turn right
                    if map[self.center_actor_y // tiles_y][(self.center_actor_x + safety_margin) // tiles_x] in [' ', 'o', '#'] \
                            or (map[self.center_actor_y // tiles_y][(self.center_actor_x + safety_margin) // tiles_x] == '-' and (
                            self.in_spawn or self.dead)):
                        self.turns[0] = True
        
        # Still able to go left and right if out of bounds (travel across screen)
        else:
            self.turns[0] = True
            self.turns[1] = True

        # Checks whether ghost is at spawn
        if 350 < self.ghost_x < 550 and 370 < self.ghost_y < 480: # x and y coords of box
            self.in_spawn = True
        else:
            self.in_spawn = False

        return self.turns, self.in_spawn

    # MOVEMENT PATTERN: ORANGE GHOST
    def move_orange_ghost(self):

        # Behavior: Aggressively pursues the player but prioritizes horizontal movement, turning up/down only upon collision or when advantageous.
        # Tendency: Moves left/right unless blocked, switching directions unpredictably.

        # MOVING RIGHT
        if self.direction == 0:
            if self.target[0] > self.ghost_x and self.turns[0]: 
                self.ghost_x += self.speed + 1  # Slightly increase speed for horizontal pursuit
            # Move right if target is farther right and ghost can continue right

            else:
                # Collision or turn required while moving right
                if not self.turns[0]: 
                    if self.target[1] > self.ghost_y and self.turns[3]:
                        self.direction = 3
                        self.ghost_y += self.speed
                    # Turn down if target is below and path is clear

                    elif self.target[1] < self.ghost_y and self.turns[2]:
                        self.direction = 2
                        self.ghost_y -= self.speed
                    # Turn up if target is above and path is clear

                    elif self.target[0] < self.ghost_x and self.turns[1]:
                        self.direction = 1
                        self.ghost_x -= self.speed - 1
                    # Turn left if target is to the left and path is clear

                    elif self.turns[3]:
                        self.direction = 3
                        self.ghost_y += self.speed
                    # No direct path, fallback to moving down

                    elif self.turns[2]:
                        self.direction = 2
                        self.ghost_y -= self.speed
                    # Fallback to moving up

                    elif self.turns[1]:
                        self.direction = 1
                        self.ghost_x -= self.speed - 1
                    # Fallback to moving left

                elif self.turns[0]:

                    # Check for vertical movement options if still able to move right
                    if self.target[1] > self.ghost_y and self.turns[3]:
                        self.direction = 3
                        self.ghost_y += self.speed
                    # Move down if target is below

                    elif self.target[1] < self.ghost_y and self.turns[2]:
                        self.direction = 2
                        self.ghost_y -= self.speed
                    # Move up if target is above

                    else:
                        self.ghost_x += self.speed + 1
                    # Continue moving right

        # MOVING LEFT
        elif self.direction == 1:
            if self.target[1] > self.ghost_y and self.turns[3]:
                self.direction = 3
            # Turn down if target is below

            elif self.target[0] < self.ghost_x and self.turns[1]:
                self.ghost_x -= self.speed + 1  # Prioritize horizontal movement
            # Continue left if target is left and path is clear

            elif not self.turns[1]:

                # Handle collision or turns while moving left
                if self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                # Turn down if target is below

                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                # Turn up if target is above

                elif self.target[0] > self.ghost_x and self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed - 1
                # Turn right if target is to the right

                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                # Fallback to moving down

                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                # Fallback to moving up

                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed - 1
                # Fallback to moving right

            elif self.turns[1]:

                # Check for vertical movement options if still able to move left
                if self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed

                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed

                else:
                    self.ghost_x -= self.speed + 1
                    # Continue moving left

        # MOVING UPWARDS
        elif self.direction == 2:
            if self.target[0] < self.ghost_x and self.turns[1]:
                self.direction = 1
                self.ghost_x -= self.speed
            # Turn left if target is to the left

            elif self.target[1] < self.ghost_y and self.turns[2]:
                self.ghost_y -= self.speed + 1
            # Continue moving up if target is above

            elif not self.turns[2]:

                # Handle collision or turns while moving up
                if self.target[0] > self.ghost_x and self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                # Turn right if target is to the right

                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed - 1
                # Turn left if target is to the left

                elif self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                # Turn down if target is below

                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed - 1
                # Fallback to moving left

                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                # Fallback to moving down

                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                # Fallback to moving right

            elif self.turns[2]:
                self.ghost_y -= self.speed + 1
            # Continue moving up

        # MOVING DOWNWARDS
        elif self.direction == 3:
            if self.target[1] > self.ghost_y and self.turns[3]:
                self.ghost_y += self.speed + 1
            # Continue moving down if target is below

            elif not self.turns[3]:

                # Handle collision or turns while moving down
                if self.target[0] > self.ghost_x and self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                # Turn right if target is to the right

                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                # Turn left if target is to the left

                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed - 1
                # Turn up if target is above

                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed - 1
                # Fallback to moving up

                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                # Fallback to moving left

                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                # Fallback to moving right

            elif self.turns[3]:
                self.ghost_y += self.speed + 1
            # Continue moving down

        # Ghost moves closer to you after exiting and entering screen through portal
        if self.ghost_x < -30:
            self.ghost_x = 900
        elif self.ghost_x > 900:
            self.ghost_x -= 30

        return self.ghost_x, self.ghost_y, self.direction

    # MOVEMENT PATTERN: RED GHOST
    def move_red_ghost(self):

    # Behavior: Directly chases the player with minimal deviation, always moving in the most direct path.
    # Tendency: Moves aggressively towards the target, prioritizing both vertical and horizontal alignment simultaneously.

    # Red ghost aggressively chases the player
        if self.direction == 0:  # Moving right
            if self.target[0] > self.ghost_x and self.turns[0]:  # Check if player is to the right
                self.ghost_x += self.speed
            elif self.target[1] > self.ghost_y and self.turns[3]:  # Check if player is below
                self.direction = 3
                self.ghost_y += self.speed
            elif self.target[1] < self.ghost_y and self.turns[2]:  # Check if player is above
                self.direction = 2
                self.ghost_y -= self.speed
            elif self.target[0] < self.ghost_x and self.turns[1]:  # Check if player is to the left
                self.direction = 1
                self.ghost_x -= self.speed
        elif self.direction == 1:  # Moving left
            if self.target[0] < self.ghost_x and self.turns[1]:  # Check if player is to the left
                self.ghost_x -= self.speed
            elif self.target[1] > self.ghost_y and self.turns[3]:  # Check if player is below
                self.direction = 3
                self.ghost_y += self.speed
            elif self.target[1] < self.ghost_y and self.turns[2]:  # Check if player is above
                self.direction = 2
                self.ghost_y -= self.speed
            elif self.target[0] > self.ghost_x and self.turns[0]:  # Check if player is to the right
                self.direction = 0
                self.ghost_x += self.speed
        elif self.direction == 2:  # Moving up
            if self.target[1] < self.ghost_y and self.turns[2]:  # Check if player is above
                self.ghost_y -= self.speed
            elif self.target[0] > self.ghost_x and self.turns[0]:  # Check if player is to the right
                self.direction = 0
                self.ghost_x += self.speed
            elif self.target[0] < self.ghost_x and self.turns[1]:  # Check if player is to the left
                self.direction = 1
                self.ghost_x -= self.speed
            elif self.target[1] > self.ghost_y and self.turns[3]:  # Check if player is below
                self.direction = 3
                self.ghost_y += self.speed
        elif self.direction == 3:  # Moving down
            if self.target[1] > self.ghost_y and self.turns[3]:  # Check if player is below
                self.ghost_y += self.speed
            elif self.target[0] > self.ghost_x and self.turns[0]:  # Check if player is to the right
                self.direction = 0
                self.ghost_x += self.speed
            elif self.target[0] < self.ghost_x and self.turns[1]:  # Check if player is to the left
                self.direction = 1
                self.ghost_x -= self.speed
            elif self.target[1] < self.ghost_y and self.turns[2]:  # Check if player is above
                self.direction = 2
                self.ghost_y -= self.speed

        # Wrap around when ghost goes off screen
        if self.ghost_x < -30:
            self.ghost_x = 900
        elif self.ghost_x > 900:
            self.ghost_x = -30

        return self.ghost_x, self.ghost_y, self.direction

    # MOVEMENT PATTERN: CYAN GHOST
    def move_cyan_ghost(self):

        # Behavior: Pursues the player but emphasizes vertical movement to align with the player and then moves horizontally.
        # Tendency: Prefers up/down movement unless blocked, only moving horizontally when necessary.
     
        if self.direction == 0:
            if self.target[0] > self.ghost_x and self.turns[0]:
                self.ghost_x += self.speed
            elif not self.turns[0]:
                if self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
            elif self.turns[0]:
                if self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                if self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                else:
                    self.ghost_x += self.speed
        elif self.direction == 1:
            if self.target[1] > self.ghost_y and self.turns[3]:
                self.direction = 3
            elif self.target[0] < self.ghost_x and self.turns[1]:
                self.ghost_x -= self.speed
            elif not self.turns[1]:
                if self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.target[0] > self.ghost_x and self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
            elif self.turns[1]:
                if self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                if self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                else:
                    self.ghost_x -= self.speed
        elif self.direction == 2:
            if self.target[1] < self.ghost_y and self.turns[2]:
                self.direction = 2
                self.ghost_y -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.ghost_x and self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
            elif self.turns[2]:
                self.ghost_y -= self.speed
        elif self.direction == 3:
            if self.target[1] > self.ghost_y and self.turns[3]:
                self.ghost_y += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.ghost_x and self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
            elif self.turns[3]:
                self.ghost_y += self.speed
        if self.ghost_x < -30:
            self.ghost_x = 900
        elif self.ghost_x > 900:
            self.ghost_x - 30
        return self.ghost_x, self.ghost_y, self.direction

    # MOVEMENT PATTERN: PINK GHOST
    def move_pink_ghost(self):

        # Behavior: Avoids direct confrontation with the player by moving away if too close, but otherwise roams the maze semi-randomly.
        # Tendency: Wanders around unless the player is nearby, in which case it moves to maintain a safe distance.

        # Define a distance threshold for avoiding confrontation
        avoidance_distance = 8

        # Calculate the distance to the target (player)
        distance_to_target = ((self.target[0] - self.ghost_x) ** 2 + (self.target[1] - self.ghost_y) ** 2) ** 0.5

        if distance_to_target < avoidance_distance:
            # Move away from the player if too close
            if self.ghost_x < self.target[0]:
                if self.turns[1]:  # Can turn left
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[2]:  # Can turn down
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[3]:  # Can turn up
                    self.direction = 3
                    self.ghost_y += self.speed
            else:
                if self.turns[0]:  # Can turn right
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.turns[2]:  # Can turn down
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[3]:  # Can turn up
                    self.direction = 3
                    self.ghost_y += self.speed
        else:
            # Roam semi-randomly
            if self.direction == 0:
                if self.turns[0]:
                    self.ghost_x += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
            elif self.direction == 1:
                if self.turns[1]:
                    self.ghost_x -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
            elif self.direction == 2:
                if self.turns[2]:
                    self.ghost_y -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
            elif self.direction == 3:
                if self.turns[3]:
                    self.ghost_y += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed

        # Wrap around the screen
        if self.ghost_x < -30:
            self.ghost_x = 900
        elif self.ghost_x > 900:
            self.ghost_x = -30

        return self.ghost_x, self.ghost_y, self.direction

def get_targets(red_x, red_y, cyan_x, cyan_y, pink_x, pink_y, orange_x, orange_y):
    # CHECK PLAYER POSITION WHEN POWER-UP
    if pacman_x < 450: # If player is on the left half of the screen, scatter to opposite side
        scatter_x = 900
    else:
        scatter_x = 0

    if pacman_y < 450: # If player is on the right half of the screen, scatter to opposite side
        scatter_y = 900
    else:
        scatter_y = 0
    return_target = (380, 400) # Spawn point for ghosts

    if powerup:
        
        # If red ghost not dead, scatter
        if not red_ghost.dead and not killed_ghosts[0]:
            reds_target = (scatter_x, scatter_y)

        # If red ghost not dead but in spawn point, get out of box
        elif not red_ghost.dead and killed_ghosts[0]:
            if 340 < red_x < 560 and 340 < red_y < 500:
                reds_target = (400, 100)

            # If not dead and no power-up, chase pacman
            else:
                reds_target = (pacman_x, pacman_y)

        # If red ghost dead, go back to spawn
        else:
            reds_target = return_target

        if not cyan_ghost.dead and not killed_ghosts[1]:
            cyans_target = (scatter_x, pacman_y)

        elif not cyan_ghost.dead and killed_ghosts[1]:
            if 340 < cyan_x < 560 and 340 < cyan_y < 500:
                cyans_target = (400, 100)

            else:
                cyans_target = (pacman_x, pacman_y)
                
        else:
            cyans_target = return_target

        if not pink_ghost.dead:
            pinks_target = (pacman_x, scatter_y)

        elif not pink_ghost.dead and killed_ghosts[2]:
            if 340 < pink_x < 560 and 340 < pink_y < 500:
                pinks_target = (400, 100)

            else:
                pinks_target = (pacman_x, pacman_y)

        else:
            pinks_target = return_target

        if not orange_ghost.dead and not killed_ghosts[3]:
            oranges_target = (450, 450)

        elif not orange_ghost.dead and killed_ghosts[3]:
            if 340 < orange_x < 560 and 340 < orange_y < 500:
                oranges_target = (400, 100)

            else:
                oranges_target = (pacman_x, pacman_y)

        else:
            oranges_target = return_target

    else:
        if not red_ghost.dead:
            if 340 < red_x < 560 and 340 < red_y < 500:
                reds_target = (400, 100)

            else:
                reds_target = (pacman_x, pacman_y)

        else:
            reds_target = return_target

        if not cyan_ghost.dead:
            if 340 < cyan_x < 560 and 340 < cyan_y < 500:
                cyans_target = (400, 100)

            else:
                cyans_target = (pacman_x, pacman_y)

        else:
            cyans_target = return_target

        if not pink_ghost.dead:
            if 340 < pink_x < 560 and 340 < pink_y < 500:
                pinks_target = (400, 100)

            else:
                pinks_target = (pacman_x, pacman_y)

        else:
            pinks_target = return_target
            
        if not orange_ghost.dead:
            if 340 < orange_x < 560 and 340 < orange_y < 500:
                oranges_target = (400, 100)

            else:
                oranges_target = (pacman_x, pacman_y)
                
        else:
            oranges_target = return_target

    return [reds_target, cyans_target, pinks_target, oranges_target]


'''
------------ RUNNING THE GAME ------------
'''

# BACKGROUND MUSIC
pygame.mixer.music.load('audio/pacman_theme.wav')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

run = True
while run:

    # Framerate and blinking cycle of power-ups
    timer.tick(fps)
    if cycle < 31:
        cycle += 1
        if cycle > 3:
            blink = False
    else:
        cycle = 0
        blink = True

    if powerup and power_cycle < 600: # If power-up is active for 10 seconds (at 60 fps)
        power_cycle += 1 # Goes through 1 power cycle

    elif powerup and power_cycle >= 600: # If power-up is active for more than 10 seconds (at 60 fps)
        power_cycle = 0 # Ends power cycle
        powerup = False # Ends power-up
        killed_ghosts = [False, False, False, False] # Reset ghosts killed (can only die during power-up)

    if start_timer < 180 and not game_over and not game_won: # 3 second delay before starting game
        moving = False # Can't move during this period
        start_timer += 1
    else:
        moving = True

    # BACKGROUND
    game_window.fill('black')

    # DISPLAYS MAP
    draw_map()

    # Center of Pacman
    center_actor_x = pacman_x + 23
    center_actor_y = pacman_y + 24

    # Ghost Speeds
    if powerup:
        ghost_speeds = [1, 1, 1, 1] # Slower while power-up
    else:
        ghost_speeds = [2, 2, 2, 2] # Normal without power-up

    if killed_ghosts[0]:
        ghost_speeds[0] = 2

    if killed_ghosts[1]:
        ghost_speeds[1] = 2

    if killed_ghosts[2]:
        ghost_speeds[2] = 2

    if killed_ghosts[3]:
        ghost_speeds[3] = 2

    if red_ghost_dead:
        ghost_speeds[0] = 3

    if cyan_ghost_dead:
        ghost_speeds[1] = 3

    if pink_ghost_dead:
        ghost_speeds[2] = 3
        
    if orange_ghost_dead:
        ghost_speeds[3] = 3


    # WINNING CONDITIONS
    game_won = True
    for i in range(len(map)):
        if ' ' in map[i] or 'o' in map[i]:
            game_won = False

    player_circle = pygame.draw.circle(game_window, 'black', (center_actor_x, center_actor_y), 20, 2)

    # DISPLAYS PACMAN
    draw_pacman()

    # GHOST ATTRIBUTES
    red_ghost = Ghost(red_ghost_x, red_ghost_y, targets[0], ghost_speeds[0], red_ghost_img, red_ghost_direction, red_ghost_dead, red_ghost_at_spawn, 0)
    cyan_ghost = Ghost(cyan_ghost_x, cyan_ghost_y, targets[1], ghost_speeds[1], cyan_ghost_img, cyan_ghost_direction, cyan_ghost_dead, cyan_ghost_at_spawn, 1)
    pink_ghost = Ghost(pink_ghost_x, pink_ghost_y, targets[2], ghost_speeds[2], pink_ghost_img, pink_ghost_direction, pink_ghost_dead, pink_ghost_at_spawn, 2)
    orange_ghost = Ghost(orange_ghost_x, orange_ghost_y, targets[3], ghost_speeds[3], orange_ghost_img, orange_ghost_direction, orange_ghost_dead, orange_ghost_at_spawn, 3)
    
    # DISPLAYS GAME UI
    draw_ui()

    # EACH GHOSTS' TARGETS
    targets = get_targets(red_ghost_x, red_ghost_y, cyan_ghost_x, cyan_ghost_y, pink_ghost_x, pink_ghost_y, orange_ghost_x, orange_ghost_y)

    # MOVES GHOSTS IF PACMAN IS MOVING
    valid_turns = pacman_position(center_actor_x, center_actor_y)
    if moving:
        pacman_x, pacman_y = move_pacman(pacman_x, pacman_y)

        # MOVES GHOSTS
        if not red_ghost_dead and not red_ghost.in_spawn:                                           
            red_ghost_x, red_ghost_y, red_ghost_direction = red_ghost.move_red_ghost()
        else:
            red_ghost_x, red_ghost_y, red_ghost_direction = red_ghost.move_orange_ghost()
        if not pink_ghost_dead and not pink_ghost.in_spawn:
            pink_ghost_x, pink_ghost_y, pink_ghost_direction = pink_ghost.move_pink_ghost()
        else:
            pink_ghost_x, pink_ghost_y, pink_ghost_direction = pink_ghost.move_orange_ghost()
        if not cyan_ghost_dead and not cyan_ghost.in_spawn:
            cyan_ghost_x, cyan_ghost_y, cyan_ghost_direction = cyan_ghost.move_cyan_ghost()
        else:
            cyan_ghost_x, cyan_ghost_y, cyan_ghost_direction = cyan_ghost.move_orange_ghost()
        orange_ghost_x, orange_ghost_y, orange_ghost_direction = orange_ghost.move_orange_ghost()

    # PACMAN COLLISIONS
    score, powerup, power_cycle, killed_ghosts = pacman_collisions(score, powerup, power_cycle, killed_ghosts) 

    if not powerup:
        if (player_circle.colliderect(red_ghost.rect) and not red_ghost.dead) or \
                (player_circle.colliderect(cyan_ghost.rect) and not cyan_ghost.dead) or \
                (player_circle.colliderect(pink_ghost.rect) and not pink_ghost.dead) or \
                (player_circle.colliderect(orange_ghost.rect) and not orange_ghost.dead):
            
            if lives > 0:
                lives -= 1
                start_timer = 0 
                powerup = False
                power_cycle = 0
                pacman_x = 430
                pacman_y = 660
                direction = 0
                direction_cmd = 0
                red_ghost_x = 430
                red_ghost_y = 325
                red_ghost_direction = 0
                cyan_ghost_x = 380
                cyan_ghost_y = 410
                cyan_ghost_direction = 2
                pink_ghost_x = 430
                pink_ghost_y = 410
                pink_ghost_direction = 2
                orange_ghost_x = 480
                orange_ghost_y = 410
                orange_ghost_direction = 2
                killed_ghosts = [False, False, False, False]
                red_ghost_dead = False
                cyan_ghost_dead = False
                orange_ghost_dead = False
                pink_ghost_dead = False
            else:
                game_over = True
                moving = False
                start_timer = 0
    if powerup and player_circle.colliderect(red_ghost.rect) and killed_ghosts[0] and not red_ghost.dead:
        if lives > 0:
            powerup = False
            power_cycle = 0
            lives -= 1
            start_timer = 0
            pacman_x = 430
            pacman_y = 660
            direction = 0
            direction_cmd = 0
            red_ghost_x = 430
            red_ghost_y = 410
            red_ghost_direction = 0
            cyan_ghost_x = 380
            cyan_ghost_y = 410
            cyan_ghost_direction = 2
            pink_ghost_x = 430
            pink_ghost_y = 410
            pink_ghost_direction = 2
            orange_ghost_x = 480
            orange_ghost_y = 410
            orange_ghost_direction = 2
            killed_ghosts = [False, False, False, False]
            red_ghost_dead = False
            cyan_ghost_dead = False
            orange_ghost_dead = False
            pink_ghost_dead = False
        else:
            game_over = True
            moving = False
            start_timer = 0
    if powerup and player_circle.colliderect(cyan_ghost.rect) and killed_ghosts[1] and not cyan_ghost.dead:
        if lives > 0:
            powerup = False
            power_cycle = 0
            lives -= 1
            start_timer = 0
            pacman_x = 430
            pacman_y = 660
            direction = 0
            direction_cmd = 0
            red_ghost_x = 430
            red_ghost_y = 325
            red_ghost_direction = 0
            cyan_ghost_x = 380
            cyan_ghost_y = 410
            cyan_ghost_direction = 2
            pink_ghost_x = 430
            pink_ghost_y = 410
            pink_ghost_direction = 2
            orange_ghost_x = 480
            orange_ghost_y = 410
            orange_ghost_direction = 2
            killed_ghosts = [False, False, False, False]
            red_ghost_dead = False
            cyan_ghost_dead = False
            orange_ghost_dead = False
            pink_ghost_dead = False
        else:
            game_over = True
            moving = False
            start_timer = 0
    if powerup and player_circle.colliderect(pink_ghost.rect) and killed_ghosts[2] and not pink_ghost.dead:
        if lives > 0:
            powerup = False
            power_cycle = 0
            lives -= 1
            start_timer = 0
            pacman_x = 430
            pacman_y = 660
            direction = 0
            direction_cmd = 0
            red_ghost_x = 430
            red_ghost_y = 325
            red_ghost_direction = 0
            cyan_ghost_x = 380
            cyan_ghost_y = 410
            cyan_ghost_direction = 2
            pink_ghost_x = 430
            pink_ghost_y = 410
            pink_ghost_direction = 2
            orange_ghost_x = 480
            orange_ghost_y = 410
            orange_ghost_direction = 2
            killed_ghosts = [False, False, False, False]
            red_ghost_dead = False
            cyan_ghost_dead = False
            orange_ghost_dead = False
            pink_ghost_dead = False
        else:
            game_over = True
            moving = False
            start_timer = 0
    if powerup and player_circle.colliderect(orange_ghost.rect) and killed_ghosts[3] and not orange_ghost.dead:
        if lives > 0:
            powerup = False
            power_cycle = 0
            lives -= 1
            start_timer = 0
            pacman_x = 430
            pacman_y = 660
            direction = 0
            direction_cmd = 0
            red_ghost_x = 430
            red_ghost_y = 325
            red_ghost_direction = 0
            cyan_ghost_x = 380
            cyan_ghost_y = 410
            cyan_ghost_direction = 2
            pink_ghost_x = 430
            pink_ghost_y = 410
            pink_ghost_direction = 2
            orange_ghost_x = 430 # x coord updated cause orange keeps getting stuck
            orange_ghost_y = 410 # y coord updated cause orange keeps getting stuck
            orange_ghost_direction = 2
            killed_ghosts = [False, False, False, False]
            red_ghost_dead = False
            cyan_ghost_dead = False
            orange_ghost_dead = False
            pink_ghost_dead = False
        else:
            game_over = True
            moving = False
            start_timer = 0
    if powerup and player_circle.colliderect(red_ghost.rect) and not red_ghost.dead and not killed_ghosts[0]:
        red_ghost_dead = True
        killed_ghosts[0] = True
        score += (2 ** killed_ghosts.count(True)) * 100
    if powerup and player_circle.colliderect(cyan_ghost.rect) and not cyan_ghost.dead and not killed_ghosts[1]:
        cyan_ghost_dead = True
        killed_ghosts[1] = True
        score += (2 ** killed_ghosts.count(True)) * 100
    if powerup and player_circle.colliderect(pink_ghost.rect) and not pink_ghost.dead and not killed_ghosts[2]:
        pink_ghost_dead = True
        killed_ghosts[2] = True
        score += (2 ** killed_ghosts.count(True)) * 100
    if powerup and player_circle.colliderect(orange_ghost.rect) and not orange_ghost.dead and not killed_ghosts[3]:
        orange_ghost_dead = True
        killed_ghosts[3] = True
        score += (2 ** killed_ghosts.count(True)) * 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Arrow Right or 'D'
                direction_cmd = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: # Arrow Left or 'A'
                direction_cmd = 1
            if event.key == pygame.K_UP or event.key == pygame.K_w: # Arrow Up or 'W'
                direction_cmd = 2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: # Arrow Down or 'S'
                direction_cmd = 3
            if event.key == pygame.K_SPACE and (game_over or game_won): # Space bar to restart game
                powerup = False
                power_cycle = 0
                lives -= 1
                start_timer = 0
                pacman_x = 430
                pacman_y = 660
                direction = 0
                direction_cmd = 0
                red_ghost_x = 430
                red_ghost_y = 325
                red_ghost_direction = 0
                cyan_ghost_x = 380
                cyan_ghost_y = 410
                cyan_ghost_direction = 2
                pink_ghost_x = 430
                pink_ghost_y = 410
                pink_ghost_direction = 2
                orange_ghost_x = 480
                orange_ghost_y = 410
                orange_ghost_direction = 2
                killed_ghosts = [False, False, False, False]
                red_ghost_dead = False
                cyan_ghost_dead = False
                orange_ghost_dead = False
                pink_ghost_dead = False
                score = 0
                lives = 3
                map = layout
                game_over = False
                game_won = False

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction_cmd == 0: # Arrow Right or 'D'
                direction_cmd = direction
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction_cmd == 1: # Arrow Left or 'A'
                direction_cmd = direction
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction_cmd == 2: # Arrow Up or 'W'
                direction_cmd = direction
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction_cmd == 3: # Arrow Down or 'S'
                direction_cmd = direction

    if direction_cmd == 0 and valid_turns[0]:
        direction = 0
    if direction_cmd == 1 and valid_turns[1]:
        direction = 1
    if direction_cmd == 2 and valid_turns[2]:
        direction = 2
    if direction_cmd == 3 and valid_turns[3]:
        direction = 3

    if pacman_x > 900: # If Pacman has exceeded screen
        pacman_x = -47
    elif pacman_x < -50:
        pacman_x = 897

    # Respawn if ghosts make it back to spawn
    if red_ghost.in_spawn and red_ghost_dead:
        red_ghost_dead = False
    if cyan_ghost.in_spawn and cyan_ghost_dead:
        cyan_ghost_dead = False
    if pink_ghost.in_spawn and pink_ghost_dead:
        pink_ghost_dead = False
    if orange_ghost.in_spawn and orange_ghost_dead:
        orange_ghost_dead = False

    pygame.display.flip() # Updates game window display

pygame.mixer.music.stop()
pygame.quit()
