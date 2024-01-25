import pygame  # Imports the Pygame library --> Used for developing games
import sys  # Imports the sys module
import random


# --APP INITIALIZATIION-- #

# Constants
WIDTH, HEIGHT = 800, 600  # Game window dimensions
BALL_RADIUS = 20  # Radius of the bouncing ball
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 10  # Platform dimensions
FPS = 60  # Frames per second --> Controls the speed of the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)  # For the level indicator

# --CREATING PYGAME INSTANCE-- #

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set title of the window
pygame.display.set_caption("Bouncing Ball")
# Set the font
font = pygame.font.Font(None, 36)

# Clock to control the frame rate
Clock = pygame.time.Clock()

# Initialize variables for the game
ball_position = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]  # Faster starting speed
platform_position = [WIDTH // 2 - PLATFORM_WIDTH // 2, HEIGHT - PLATFORM_HEIGHT - 10]
platform_speed = 10
score = 0
lives = 3
current_level = 1
platform_color = ORANGE  # Initialize platform color

# --GAME SCREEN-- #


# Functions for screens
def start_screen():
    screen.fill(BLACK)
    # Render text
    render_text("Bouncing Ball Game", 50, HEIGHT // 4)
    render_text("Press any key to start...", 30, HEIGHT // 3)
    render_text("Move the platform with arrow keys...", 30, HEIGHT // 2)
    pygame.display.flip()
    wait_for_key()


def game_over_screen():
    screen.fill(BLACK)
    render_text("Game Over!", 50, HEIGHT // 4)
    render_text(f"Your final score: {score}", 30, HEIGHT // 2)
    render_text("Press any key to restart...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()


def victory_screen():
    screen.fill(BLACK)
    render_text("You won!", 50, HEIGHT // 4)
    render_text(f"Your final score: {score}", 30, HEIGHT // 2)
    render_text("Press any key to exit...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()


def wait_for_key():
    waiting = True
    while waiting:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If any key is pressed, start the game
            elif event.type == pygame.KEYDOWN:
                waiting = False


def render_text(text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH // 2, y_position)
    screen.blit(text_surface, text_rect)


def change_platform_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# --MAIN GAME LOOP-- #

# Start screen
start_screen()
game_running = True

while game_running:
    # --EVENT LOOP-- #
    for event in pygame.event.get():
        # If the user wants to quit
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()

    # Move the platform
    platform_position[0] += (
        keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    ) * platform_speed
    platform_position[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * platform_speed

    # Ensure the platform stays within the screen boundaries
    platform_position[0] = max(0, min(platform_position[0], WIDTH - PLATFORM_WIDTH))
    platform_position[1] = max(0, min(platform_position[1], HEIGHT - PLATFORM_HEIGHT))

    # Move the ball
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Bounce off the walls
    if ball_position[0] <= 0 or ball_position[0] >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # Check if the ball hits the platform
    if (
        platform_position[0]
        <= ball_position[0]
        <= platform_position[0] + PLATFORM_WIDTH
        and platform_position[1]
        <= ball_position[1]
        <= platform_position[1] + PLATFORM_HEIGHT
    ):
        ball_speed[1] = -ball_speed[1]
        score += 1
        platform_color = change_platform_color()

    # Check if the player advances to the next level
    if score >= current_level * 10:
        current_level += 1
        ball_position = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]
        platform_color = change_platform_color()

    # Check ifthe ball falls off the screen
    if ball_position[1] >= HEIGHT:
        # Decrease lives
        lives -= 1
        ball_position = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]
        platform_color = change_platform_color()

        # If the player runs out of lives, end the game
        if lives <= 0:
            game_over_screen()
            start_screen()  # Restart the game after game over
            lives = 3
            score = 0
            current_level = 1
        else:
            # If the player still has lives, restart the level
            ball_position = [WIDTH // 2, HEIGHT // 2]
            ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]
            platform_color = change_platform_color()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(
        screen, WHITE, (int(ball_position[0]), int(ball_position[1])), BALL_RADIUS
    )

    # Draw the platform
    pygame.draw.rect(
        screen,
        platform_color,
        (
            int(platform_position[0]),
            int(platform_position[1]),
            PLATFORM_WIDTH,
            PLATFORM_HEIGHT,
        ),
    )

    # Display information
    info_line_y = 10  # Adjust the vertical position as needed
    info_spacing = 75  # Adjust the spacing as needed

    # Draw the score in an orange rectangle at the top left
    score_text = font.render(f"Score: {score}", True, WHITE)
    score_rect = score_text.get_rect(topleft=(10, info_line_y))
    pygame.draw.rect(screen, ORANGE, score_rect.inflate(10, 5))
    screen.blit(score_text, score_rect)

    # Draw the level indicator in a light-blue rectangle at the top left (next to the score)
    level_text = font.render(f"Level: {current_level}", True, WHITE)
    level_rect = level_text.get_rect(
        topleft=(score_rect.topright[0] + info_spacing, info_line_y)
    )
    pygame.draw.rect(screen, LIGHT_BLUE, level_rect.inflate(10, 5))
    screen.blit(level_text, level_rect)

    # Draw the lives indicator in a red rectangle at the top left (next to the level indicator)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    lives_rect = lives_text.get_rect(
        topleft=(level_rect.topright[0] + info_spacing, info_line_y)
    )
    pygame.draw.rect(screen, RED, lives_rect.inflate(10, 5))
    screen.blit(lives_text, lives_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    Clock.tick(FPS)

# Victory screen
victory_screen()

# Quit Pygame
pygame.quit()
