# AIM: Python program to simulate bouncing ball in Pygame
import pygame 
import sys
# Initialize Pygame 
pygame.init()
# load ball image
ball = pygame.image.load("data/ball.png")
# Set up the display 
width, height = 800, 600
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Bouncing Simulation")
pygame.display.set_icon(ball)

# Ball properties
ball = pygame.transform.scale(ball,(80,80))
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
    if ball_position[0] < 0 or ball_position[0] >width-80:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] < 0 or ball_position[1] >height-80:
        ball_speed[1] = -ball_speed[1]
#Clear the screen
    screen.fill((255, 255, 255))
# Draw the logo
    screen.blit(ball, ball_position)
#Update the display
    pygame.display.flip()
# Add a small delay to control the frame rate 
    pygame.time.delay(30)