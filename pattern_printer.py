import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Tree")

# Colors
background_color = (0, 0, 0)
tree_color = (0, 255, 0)

# Function to draw a fractal tree
def draw_tree(x, y, branch_length, angle, depth):
    if depth > 0:
        # Calculate the endpoint of the branch
        x2 = x + int(math.cos(math.radians(angle)) * branch_length)
        y2 = y - int(math.sin(math.radians(angle)) * branch_length)

        # Draw the branch
        pygame.draw.line(screen, tree_color, (x, y), (x2, y2), 2)

        # Recursive calls for right and left branches
        draw_tree(x2, y2, branch_length * 0.7, angle - 20, depth - 1)
        draw_tree(x2, y2, branch_length * 0.7, angle + 20, depth - 1)

# Main drawing loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(background_color)

    # Draw the fractal tree
    draw_tree(width // 2, height - 50, 100, -90, 9)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
