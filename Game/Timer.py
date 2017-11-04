"""
 Show how to put a timeer on the screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
font = pygame.font.Font("Comic.ttf", 25)
frame_count = 0
frame_rate = 60
start_time = 90
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    # Set the screen background
    screen.fill(WHITE)
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    # Calculate total seconds
    total_seconds = start_time - (frame_count / frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds / 60
    seconds = total_seconds % 60
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(output_string, True, BLACK)
    screen.blit(text, [10, 280])
    frame_count += 1
    # Limit frames per second
    clock.tick(frame_rate)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()