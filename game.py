import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

# Font
FONT = pygame.font.Font(None, 36)

# Define thresholds for ranks
RANKS = [
    ("Bronze", 0),
    ("Silver", 45),
    ("Platinum", 65),
    ("Diamond", 100)
]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Clicker Game")

# Load coin image and resize
coin_image = pygame.image.load("coin.png")  # Update with the correct path to your image
coin_image = pygame.transform.scale(coin_image, (100, 100))  # Resize the image to 100x100 pixels
coin_rect = coin_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Score and rank
score = 0

def get_rank(score):
    for rank, threshold in reversed(RANKS):
        if score >= threshold:
            return rank
    return "Bronze"

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if coin_rect.collidepoint(event.pos):
                score += 1

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the coin
    screen.blit(coin_image, coin_rect)

    # Draw the score and rank
    rank = get_rank(score)
    draw_text(f"Score: {score}", FONT, BLACK, screen, WIDTH // 2, 50)
    draw_text(f"Rank: {rank}", FONT, GOLD, screen, WIDTH // 2, 100)

    # Update the display
    pygame.display.flip()
