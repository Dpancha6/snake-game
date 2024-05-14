import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)  
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (40, 40, 40)  # Dark gray background

# Set up the snake
SNAKE_SIZE = 20
snake_position = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
snake_direction = RIGHT = (SNAKE_SIZE, 0)

# Set up the food and power-up
food_position = [random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                 random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
power_up_position = None

# Set up the game loop
game_over = False
clock = pygame.time.Clock()
UP = (0, -SNAKE_SIZE)
DOWN = (0, SNAKE_SIZE)
LEFT = (-SNAKE_SIZE, 0)
RIGHT = (SNAKE_SIZE, 0)
direction = RIGHT
score = 0

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # Move the snake
    snake_position[0] += snake_direction[0]
    snake_position[1] += snake_direction[1]
    snake_body.insert(0, list(snake_position))

    # Check for collisions with the food
    if snake_position == food_position:
        score += 10
        food_position = [random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                         random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
        if not power_up_position:
            power_up_position = [random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                                 random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
    else:
        snake_body.pop()

    # Check for collisions with the power-up
    if power_up_position and snake_position == power_up_position:
        score += 20
        snake_body.extend([list(snake_body[-1]), list(snake_body[-1])])
        power_up_position = None

    # Check for collisions with the window boundaries
    if (snake_position[0] < 0 or snake_position[0] >= WINDOW_WIDTH or
        snake_position[1] < 0 or snake_position[1] >= WINDOW_HEIGHT):
        game_over = True

    # Check for collisions with the snake's body
    for body_part in snake_body[1:]:
        if snake_position == body_part:
            game_over = True

    # Clear the window
    window.fill(BACKGROUND_COLOR)

    # Draw the score
    score_text = pygame.font.Font(None, 36).render(f"Score: {score}", True, GREEN)
    window.blit(score_text, (10, 10))

    # Draw the snake
    for position in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(position[0], position[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(window, (0, 255, 0), pygame.Rect(snake_position[0], snake_position[1], SNAKE_SIZE, SNAKE_SIZE))  # Brighter green for the head

    # Draw the food
    pygame.draw.rect(window, RED, pygame.Rect(food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw the power-up
    if power_up_position:
        pygame.draw.rect(window, YELLOW, pygame.Rect(power_up_position[0], power_up_position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(10)

# Quit Pygame
pygame.quit()


# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Set up the game window
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Snake Game")

# # Define colors
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# # Set up the snake
# SNAKE_SIZE = 20
# snake_position = [100, 100]
# snake_body = [[100, 100], [80, 100], [60, 100]]

# # Set up the food
# food_position = [random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
#                  random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]

# # Set up the game loop
# game_over = False
# clock = pygame.time.Clock()

# # Define the movement directions
# UP = (0, -SNAKE_SIZE)
# DOWN = (0, SNAKE_SIZE)
# LEFT = (-SNAKE_SIZE, 0)
# RIGHT = (SNAKE_SIZE, 0)
# direction = RIGHT

# # Game loop
# while not game_over:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and direction != DOWN:
#                 direction = UP
#             elif event.key == pygame.K_DOWN and direction != UP:
#                 direction = DOWN
#             elif event.key == pygame.K_LEFT and direction != RIGHT:
#                 direction = LEFT
#             elif event.key == pygame.K_RIGHT and direction != LEFT:
#                 direction = RIGHT

#     # Move the snake
#     snake_position[0] += direction[0]
#     snake_position[1] += direction[1]
#     snake_body.insert(0, list(snake_position))

#     # Check for collisions with the food
#     if snake_position == food_position:
#         food_position = [random.randrange(1, (WINDOW_WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
#                          random.randrange(1, (WINDOW_HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
#     else:
#         snake_body.pop()

#     # Check for collisions with the window boundaries
#     if (snake_position[0] < 0 or snake_position[0] >= WINDOW_WIDTH or
#         snake_position[1] < 0 or snake_position[1] >= WINDOW_HEIGHT):
#         game_over = True

#     # Check for collisions with the snake's body
#     for body_part in snake_body[1:]:
#         if snake_position == body_part:
#             game_over = True

#     # Clear the window
#     window.fill(BLACK)

#     # Draw the snake
#     for position in snake_body:
#         pygame.draw.rect(window, GREEN, pygame.Rect(position[0], position[1], SNAKE_SIZE, SNAKE_SIZE))

#     # Draw the food
#     pygame.draw.rect(window, RED, pygame.Rect(food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

#     # Update the display
#     pygame.display.update()

#     # Control the frame rate
#     clock.tick(10)

# # Quit Pygame
# pygame.quit()