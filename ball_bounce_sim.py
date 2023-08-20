# AIM: Python program to simulate bouncing ball in Pygame
import pygame 
import sys
# Initialize Pygame 
pygame.init()
# Set up the display 
width, height = 800, 600
screen=pygame.display.set_mode((width, height))

#Ball properties
ball_radius=30
ball_color = (255,0,0)
ball_speed= [5, 5] # [x-speed, y-speed]
ball_position= [width // 2, height // 2]
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# Update ball position
    ball_position[0] += ball_speed[0] 
    ball_position[1] += ball_speed[1]
# Check for collision with walls
    if ball_position[0] < 0 or ball_position[0] >width:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] < 0 or ball_position[1] >height:
        ball_speed[1] = -ball_speed[1]
#Clear the screen
    screen.fill((255, 255, 255))
# Draw the logo
    pygame.draw.circle(screen,ball_color,ball_position,ball_radius)
#Update the display
    pygame.display.flip()
# Add a small delay to control the frame rate 
    pygame.time.delay(30)